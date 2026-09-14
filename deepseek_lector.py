import json
import re
import unicodedata

import streamlit as st
from openai import OpenAI


# ============================================================
# CLIENTE DEEPSEEK
# ============================================================

client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)


# ============================================================
# CONFIGURACIÓN
# ============================================================

MODELO_DEEPSEEK = "deepseek-chat"


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def interpretar_certificado(texto_ocr):
    """
    Interpreta un certificado de estudios.

    Objetivo principal:
    devolver cada asignatura con SU nota real, sin propagar notas
    entre filas y sin confundir créditos, códigos, horas o periodos
    con notas.

    Flujo:
    1. extracción estructurada;
    2. auditoría independiente contra el texto fuente;
    3. fusión conservadora para no perder notas válidas;
    4. rescate final exclusivo de notas faltantes;
    5. limpieza determinística en Python.

    Salida:
    {
        "nombre": "",
        "institucion": "",
        "carrera": "",
        "dni": "",
        "telefono": "",
        "email": "",
        "cursos": [
            {
                "curso": "...",
                "nota": 15,
                "creditos": 3
            }
        ]
    }
    """

    if texto_ocr is None:
        texto_ocr = ""

    texto_ocr = str(
        texto_ocr
    ).strip()

    if not texto_ocr:
        return estructura_vacia()

    # --------------------------------------------------------
    # 1. EXTRACCIÓN PRINCIPAL
    # --------------------------------------------------------

    datos_principales = intento_principal(
        texto_ocr
    )

    resultado_principal = limpiar_resultado(
        datos_principales
    )

    # --------------------------------------------------------
    # 2. RESCATE SI NO HAY CURSOS
    # --------------------------------------------------------

    if not resultado_principal["cursos"]:

        datos_rescate = intento_rescate(
            texto_ocr
        )

        resultado_rescate = limpiar_resultado(
            datos_rescate
        )

        if resultado_rescate["cursos"]:

            resultado_rescate = conservar_datos_generales(
                principal=resultado_principal,
                secundario=resultado_rescate
            )

            resultado_principal = resultado_rescate

    # --------------------------------------------------------
    # 3. AUDITORÍA DE CURSO + NOTA
    #
    # La auditoría se realiza cuando sí existen cursos.
    # Es la parte que evita que una nota detectada en una fila
    # termine siendo repetida indebidamente en otras asignaturas.
    # --------------------------------------------------------

    if resultado_principal["cursos"]:

        datos_auditados = auditar_cursos_y_notas(
            texto_ocr=texto_ocr,
            cursos_extraidos=resultado_principal["cursos"]
        )

        cursos_auditados = limpiar_lista_cursos(
            datos_auditados.get(
                "cursos",
                []
            )
            if isinstance(
                datos_auditados,
                dict
            )
            else []
        )

        if cursos_auditados:

            resultado_principal[
                "cursos"
            ] = fusionar_auditoria_sin_perder_notas_validas(
                originales=resultado_principal["cursos"],
                auditados=cursos_auditados
            )

    # --------------------------------------------------------
    # 4. RESCATE FINAL SOLO DE NOTAS QUE SIGUEN EN NULL
    # --------------------------------------------------------

    if resultado_principal["cursos"]:

        faltan_notas = any(
            item.get("nota") is None
            for item in resultado_principal["cursos"]
        )

        if faltan_notas:

            datos_rescate_notas = rescatar_notas_faltantes(
                texto_ocr=texto_ocr,
                cursos_extraidos=resultado_principal["cursos"]
            )

            cursos_rescatados = limpiar_lista_cursos(
                datos_rescate_notas.get(
                    "cursos",
                    []
                )
                if isinstance(
                    datos_rescate_notas,
                    dict
                )
                else []
            )

            if cursos_rescatados:

                resultado_principal[
                    "cursos"
                ] = fusionar_notas_rescatadas(
                    originales=resultado_principal["cursos"],
                    rescatados=cursos_rescatados
                )

    # --------------------------------------------------------
    # 5. RESCATE DETERMINÍSTICO DE NOTAS EN LETRAS
    # --------------------------------------------------------
    resultado_principal = completar_notas_en_letras_desde_ocr(
        resultado=resultado_principal,
        texto_ocr=texto_ocr
    )

    return resultado_principal



# ============================================================
# RESCATE DETERMINÍSTICO DE NOTAS EN LETRAS
# ============================================================

MAPA_NOTAS_LETRAS = {
    "DIEZ": 10,
    "ONCE": 11,
    "DOCE": 12,
    "TRECE": 13,
    "CATORCE": 14,
    "QUINCE": 15,
    "DIECISEIS": 16,
    "DIECISIETE": 17,
    "DIECIOCHO": 18,
    "DIECINUEVE": 19,
    "VEINTE": 20,
}


def extraer_nota_cercana_del_texto(texto_ocr, nombre_curso):
    """
    Busca una nota únicamente alrededor del MISMO nombre de curso.
    No utiliza créditos ni números de otras filas.
    """
    if not texto_ocr or not nombre_curso:
        return None

    curso_norm = normalizar_curso(nombre_curso)
    if not curso_norm:
        return None

    lineas = [limpiar_texto(x) for x in str(texto_ocr).splitlines()]

    for i, linea in enumerate(lineas):
        linea_norm = normalizar_curso(linea)
        if not linea_norm:
            continue

        contiene = curso_norm in linea_norm

        if not contiene:
            palabras = [p for p in curso_norm.split() if len(p) >= 3]
            if palabras:
                aciertos = sum(1 for p in palabras if p in linea_norm)
                contiene = (aciertos / len(palabras)) >= 0.90

        if not contiene:
            continue

        # Nota escrita en letras en la misma línea.
        tokens = linea_norm.split()
        for palabra, nota in MAPA_NOTAS_LETRAS.items():
            if palabra in tokens:
                return nota

        # Nota numérica 10-20 en la misma línea.
        numeros = re.findall(r"(?<!\d)(20|1[0-9])(?!\d)", linea_norm)
        numeros_unicos = list(dict.fromkeys(numeros))
        if len(numeros_unicos) == 1:
            return int(numeros_unicos[0])

        # Como respaldo, revisar solo las dos líneas inmediatamente siguientes,
        # pero únicamente notas escritas en letras.
        for j in range(i + 1, min(i + 3, len(lineas))):
            prox_norm = normalizar_curso(lineas[j])
            tokens_prox = prox_norm.split()

            for palabra, nota in MAPA_NOTAS_LETRAS.items():
                if palabra in tokens_prox:
                    return nota

    return None


def completar_notas_en_letras_desde_ocr(resultado, texto_ocr):
    """
    Completa solo notas que siguen en None.
    Nunca reemplaza una nota ya detectada.
    """
    if not isinstance(resultado, dict):
        return resultado

    cursos = resultado.get("cursos", [])
    if not isinstance(cursos, list):
        return resultado

    nuevos = []

    for item in cursos:
        if not isinstance(item, dict):
            continue

        fila = dict(item)

        if fila.get("nota") is None:
            nota = extraer_nota_cercana_del_texto(
                texto_ocr=texto_ocr,
                nombre_curso=fila.get("curso", "")
            )
            if nota is not None:
                fila["nota"] = nota

        nuevos.append(fila)

    resultado = dict(resultado)
    resultado["cursos"] = nuevos
    return resultado


# ============================================================
# PRIMER INTENTO
# ============================================================

def intento_principal(texto_ocr):

    prompt_sistema = """
Eres especialista en TRANSCRIPCIÓN Y EXTRACCIÓN ESTRUCTURADA de
certificados de estudios universitarios, institutos y centros de
educación superior.

NO debes hacer convalidaciones.
NO debes evaluar afinidad académica.
NO debes completar información faltante por sentido común.

Tu trabajo es LEER el documento.

OBJETIVO CRÍTICO:
Cada asignatura debe quedar vinculada únicamente con la NOTA que
realmente pertenece a esa misma asignatura en el certificado.

REGLAS OBLIGATORIAS PARA CURSOS Y NOTAS:

1. Extrae TODOS los cursos/asignaturas/unidades didácticas reales.

2. Mantén el nombre del curso lo más fiel posible al certificado.
   Puedes unir palabras si el nombre quedó partido en varias líneas.

3. Para cada curso, identifica su nota final solamente si existe
   evidencia suficiente de que esa nota pertenece a esa fila/curso.

4. NUNCA copies la nota de la fila anterior o siguiente.

5. NUNCA uses una misma nota como valor por defecto para varias filas.

6. Es perfectamente posible que dos cursos tengan la misma nota
   realmente. En ese caso puedes repetirla SOLO si el documento
   respalda ambas notas de forma independiente.

7. Si no puedes establecer con seguridad qué nota corresponde a
   una asignatura, usa null.

8. NO confundas con NOTA:
   - créditos;
   - horas;
   - códigos de curso;
   - número de orden;
   - ciclo;
   - semestre;
   - año;
   - periodo académico;
   - fechas.

9. Una nota válida debe encontrarse en la escala 0 a 20.
   No deduzcas una nota a partir del crédito.

10. Si el documento presenta nota numérica y nota en letras,
    verifica que sean consistentes.

11. Extrae créditos únicamente si están claramente vinculados
    a la misma asignatura. Si no son claros, usa null.

12. No conviertas en cursos:
    - encabezados;
    - subtítulos;
    - módulos;
    - periodos;
    - firmas;
    - nombres de autoridades;
    - promedios;
    - totales;
    - leyendas;
    - códigos aislados.

13. No inventes DNI, nombre, institución, carrera, teléfono o email.

14. Devuelve ÚNICAMENTE JSON válido, sin explicación adicional.
"""

    prompt_usuario = f"""
Lee cuidadosamente el siguiente texto extraído de un certificado
de estudios.

Devuelve EXACTAMENTE esta estructura:

{{
  "nombre": "",
  "institucion": "",
  "carrera": "",
  "dni": "",
  "telefono": "",
  "email": "",
  "cursos": [
    {{
      "curso": "",
      "nota": null,
      "creditos": null
    }}
  ]
}}

IMPORTANTE:
- "nota" corresponde exclusivamente al mismo "curso".
- Si la nota de esa fila no es segura: null.
- No rellenes notas faltantes usando la nota de otro curso.
- "creditos" no es "nota".
- Conserva todos los cursos reales detectables.

TEXTO DEL CERTIFICADO:

{texto_ocr}
"""

    return llamar_deepseek(
        prompt_sistema,
        prompt_usuario
    )


# ============================================================
# SEGUNDO INTENTO / RESCATE
# ============================================================

def intento_rescate(texto_ocr):

    prompt_sistema = """
Tu única tarea es reconstruir la TABLA DE CURSOS de un certificado
de estudios desde texto extraído de PDF/OCR.

Debes ser extremadamente conservador con las notas.

REGLAS:

1. Busca curso + nota + créditos como una FILA LÓGICA.
2. Si un curso ocupa varias líneas, une solo esas líneas.
3. No arrastres una nota hacia cursos vecinos.
4. Si la relación curso-nota no es segura, nota=null.
5. No confundas créditos con notas.
6. No confundas códigos con notas.
7. No confundas números de ciclo/semestre con notas.
8. No inventes cursos ni notas.
9. No uses 0 ni ninguna otra nota como valor por defecto.
10. Puede haber notas iguales entre cursos, pero solo si cada una
    está respaldada individualmente por el documento.
11. Extrae créditos solo si son claros.
12. Excluye encabezados, módulos, periodos, firmas, fechas,
    promedios, totales y textos administrativos.
13. Devuelve únicamente JSON válido.
"""

    prompt_usuario = f"""
Reconstruye todos los cursos reales del certificado.

Devuelve:

{{
  "nombre": "",
  "institucion": "",
  "carrera": "",
  "dni": "",
  "telefono": "",
  "email": "",
  "cursos": [
    {{
      "curso": "",
      "nota": null,
      "creditos": null
    }}
  ]
}}

TEXTO:

{texto_ocr}
"""

    return llamar_deepseek(
        prompt_sistema,
        prompt_usuario
    )


# ============================================================
# AUDITORÍA INDEPENDIENTE DE CURSOS Y NOTAS
# ============================================================

def auditar_cursos_y_notas(
    texto_ocr,
    cursos_extraidos
):
    """
    Segunda revisión con DeepSeek.

    El modelo recibe:
    - el texto fuente;
    - la primera lista de cursos.

    Debe corregir asociaciones curso-nota dudosas.
    """

    prompt_sistema = """
Actúa como AUDITOR de una extracción de certificado de estudios.

No estás haciendo una nueva convalidación.
Debes comparar una lista preliminar de cursos contra el TEXTO FUENTE.

Tu prioridad absoluta es evitar asociaciones incorrectas entre
asignatura y nota.

REGLAS:

1. Conserva solo cursos que realmente estén respaldados por el texto.

2. Para cada curso revisa de nuevo cuál es SU nota.

3. Si la nota propuesta puede verificarse en CUALQUIERA de las vistas OCR
   del mismo documento, CONSÉRVALA. Solo reemplázala por null cuando exista
   contradicción clara o ausencia real de evidencia.

4. No copies una nota desde cursos contiguos.

5. No uses una nota repetida simplemente porque aparece cerca de varias
   asignaturas.

6. Dos o más cursos pueden tener legítimamente la misma nota, pero
   debes mantenerla repetida solo cuando exista respaldo independiente
   para cada curso.

7. Créditos, horas, códigos, ciclos, semestres y años NO son notas.
   Cuando una nota numérica aparece junto con su equivalente en letras
   (por ejemplo 14 CATORCE, 11 ONCE, 15 QUINCE), considéralo evidencia
   fuerte de que esa calificación pertenece a esa fila.

8. Corrige el nombre del curso únicamente si el texto fuente muestra
   claramente que fue cortado o mal reconstruido.

9. Puedes recuperar un curso omitido únicamente si está claramente
   visible en el texto.

10. Si los créditos son dudosos, usa null.

11. Devuelve exclusivamente JSON válido.
"""

    prompt_usuario = f"""
TEXTO FUENTE DEL CERTIFICADO:

{texto_ocr}

LISTA PRELIMINAR EXTRAÍDA:

{json.dumps(
    cursos_extraidos,
    ensure_ascii=False,
    indent=2
)}

Devuelve:

{{
  "cursos": [
    {{
      "curso": "",
      "nota": null,
      "creditos": null
    }}
  ]
}}
"""

    return llamar_deepseek(
        prompt_sistema,
        prompt_usuario
    )



# ============================================================
# FUSIONAR AUDITORÍA SIN PERDER NOTAS YA VÁLIDAS
# ============================================================

def fusionar_auditoria_sin_perder_notas_validas(
    originales,
    auditados
):
    """
    La auditoría puede corregir errores, pero no debe borrar una nota
    válida que ya estaba asociada correctamente al mismo curso salvo
    que la auditoría entregue otra nota válida.

    Esto evita que una segunda llamada demasiado conservadora convierta
    notas correctas en None.
    """

    mapa_auditados = {}

    for item in auditados:

        curso = normalizar_curso(
            item.get(
                "curso",
                ""
            )
        )

        if not curso:
            continue

        mapa_auditados[
            curso
        ] = item

    resultado = []

    for original in originales:

        curso_original = normalizar_curso(
            original.get(
                "curso",
                ""
            )
        )

        auditado = mapa_auditados.get(
            curso_original
        )

        if auditado is None:
            resultado.append(
                dict(original)
            )
            continue

        item_final = dict(
            original
        )

        nota_original = convertir_nota(
            original.get(
                "nota"
            )
        )

        nota_auditada = convertir_nota(
            auditado.get(
                "nota"
            )
        )

        # Si la auditoría trae una nota válida, se usa.
        # Si trae None, se conserva la nota original válida.
        if nota_auditada is not None:
            item_final[
                "nota"
            ] = nota_auditada
        elif nota_original is not None:
            item_final[
                "nota"
            ] = nota_original
        else:
            item_final[
                "nota"
            ] = None

        creditos_original = convertir_creditos(
            original.get(
                "creditos"
            )
        )

        creditos_auditados = convertir_creditos(
            auditado.get(
                "creditos"
            )
        )

        if creditos_auditados is not None:
            item_final[
                "creditos"
            ] = creditos_auditados
        else:
            item_final[
                "creditos"
            ] = creditos_original

        # Mantener el nombre original salvo corrección clara.
        nombre_auditado = limpiar_texto(
            auditado.get(
                "curso",
                ""
            )
        )

        if nombre_auditado:
            item_final[
                "curso"
            ] = nombre_auditado

        resultado.append(
            item_final
        )

    return resultado


# ============================================================
# RESCATE FINAL DE NOTAS FALTANTES
# ============================================================

def rescatar_notas_faltantes(
    texto_ocr,
    cursos_extraidos
):
    """
    Tercer pase especializado exclusivamente en recuperar NOTAS
    que siguen en null.

    No crea equivalencias.
    No inventa cursos nuevos.
    No modifica notas ya confirmadas.
    """

    cursos_sin_nota = [
        {
            "curso":
                item.get(
                    "curso",
                    ""
                ),
            "nota":
                None,
            "creditos":
                item.get(
                    "creditos",
                    None
                )
        }
        for item in cursos_extraidos
        if item.get(
            "nota"
        ) is None
    ]

    if not cursos_sin_nota:
        return {
            "cursos": []
        }

    prompt_sistema = """
Eres especialista en recuperar CALIFICACIONES desde certificados
académicos escaneados.

Tu única tarea es completar la NOTA de cursos que ya fueron detectados
pero todavía tienen nota=null.

El texto puede contener varias lecturas OCR de la MISMA página:
- OCR PRINCIPAL PSM6
- OCR AUXILIAR PSM4
- OCR COLUMNA CALIFICACIÓN

Estas vistas son repeticiones del mismo documento.

REGLAS OBLIGATORIAS:

1. Mantén EXACTAMENTE los nombres de curso recibidos.
2. No agregues cursos nuevos.
3. Busca evidencia de la MISMA FILA del curso.
4. Una evidencia especialmente fuerte es:
   NOMBRE DEL CURSO + NOTA NUMÉRICA + NOTA EN LETRAS.

Ejemplos:
LENGUA Y COMUNICACION 14 CATORCE
GEOLOGIA GENERAL 11 ONCE
QUIMICA GENERAL E INORGANICA 13 TRECE

5. Equivalencias número/letra válidas:
   10 DIEZ
   11 ONCE
   12 DOCE
   13 TRECE
   14 CATORCE
   15 QUINCE
   16 DIECISEIS
   17 DIECISIETE
   18 DIECIOCHO
   19 DIECINUEVE
   20 VEINTE

6. También puedes aceptar una nota numérica sola si aparece claramente
   en la misma fila del curso y la estructura de tabla es inequívoca.

7. NO confundas la nota con:
   créditos, código, fecha, semestre, año, periodo o número de orden.

8. Los créditos suelen ser valores pequeños como 2, 3, 4 o 5.
   No los conviertas en nota.

9. No copies la nota de la fila anterior o posterior.

10. Si no puedes verificar con seguridad la nota, devuelve null.

Devuelve solamente JSON válido.
"""

    prompt_usuario = f"""
TEXTO OCR COMPLETO:

{texto_ocr}

CURSOS CON NOTA FALTANTE:

{json.dumps(
    cursos_sin_nota,
    ensure_ascii=False,
    indent=2
)}

Devuelve exactamente:

{{
  "cursos": [
    {{
      "curso": "",
      "nota": null,
      "creditos": null
    }}
  ]
}}
"""

    return llamar_deepseek(
        prompt_sistema,
        prompt_usuario
    )


def fusionar_notas_rescatadas(
    originales,
    rescatados
):
    """
    Completa únicamente notas y créditos faltantes.

    Nunca sobrescribe una nota ya existente.
    """

    mapa_rescatados = {}

    for item in rescatados:

        curso = normalizar_curso(
            item.get(
                "curso",
                ""
            )
        )

        if not curso:
            continue

        mapa_rescatados[
            curso
        ] = {
            "nota":
                convertir_nota(
                    item.get(
                        "nota"
                    )
                ),
            "creditos":
                convertir_creditos(
                    item.get(
                        "creditos"
                    )
                )
        }

    resultado = []

    for original in originales:

        item_final = dict(
            original
        )

        curso_original = normalizar_curso(
            original.get(
                "curso",
                ""
            )
        )

        recuperado = mapa_rescatados.get(
            curso_original
        )

        if recuperado:

            if (
                item_final.get(
                    "nota"
                ) is None
                and recuperado.get(
                    "nota"
                ) is not None
            ):
                item_final[
                    "nota"
                ] = recuperado[
                    "nota"
                ]

            if (
                item_final.get(
                    "creditos"
                ) in (
                    None,
                    ""
                )
                and recuperado.get(
                    "creditos"
                ) is not None
            ):
                item_final[
                    "creditos"
                ] = recuperado[
                    "creditos"
                ]

        resultado.append(
            item_final
        )

    return resultado


# ============================================================
# LLAMADA A DEEPSEEK
# ============================================================

def llamar_deepseek(
    prompt_sistema,
    prompt_usuario
):

    try:

        respuesta = client.chat.completions.create(
            model=MODELO_DEEPSEEK,
            messages=[
                {
                    "role":
                        "system",
                    "content":
                        prompt_sistema
                },
                {
                    "role":
                        "user",
                    "content":
                        prompt_usuario
                }
            ],
            response_format={
                "type":
                    "json_object"
            },
            temperature=0
        )

        contenido = (
            respuesta
            .choices[0]
            .message
            .content
        )

        return convertir_json(
            contenido
        )

    except Exception:
        # Si DeepSeek falla, no fabricamos resultados.
        return estructura_vacia()


# ============================================================
# CONVERTIR JSON
# ============================================================

def convertir_json(
    contenido
):

    if not contenido:
        return estructura_vacia()

    contenido = str(
        contenido
    ).strip()

    contenido = contenido.replace(
        "```json",
        ""
    )

    contenido = contenido.replace(
        "```JSON",
        ""
    )

    contenido = contenido.replace(
        "```",
        ""
    ).strip()

    try:

        datos = json.loads(
            contenido
        )

        if isinstance(
            datos,
            dict
        ):
            return datos

    except json.JSONDecodeError:
        pass

    # Intento mínimo de recuperar el primer objeto JSON.
    inicio = contenido.find(
        "{"
    )

    fin = contenido.rfind(
        "}"
    )

    if (
        inicio >= 0
        and fin > inicio
    ):

        fragmento = contenido[
            inicio:
            fin + 1
        ]

        try:

            datos = json.loads(
                fragmento
            )

            if isinstance(
                datos,
                dict
            ):
                return datos

        except json.JSONDecodeError:
            pass

    return estructura_vacia()


# ============================================================
# LIMPIAR RESULTADO COMPLETO
# ============================================================

def limpiar_resultado(
    datos
):

    resultado = estructura_vacia()

    if not isinstance(
        datos,
        dict
    ):
        return resultado

    resultado[
        "nombre"
    ] = limpiar_texto(
        datos.get(
            "nombre",
            ""
        )
    )

    resultado[
        "institucion"
    ] = limpiar_texto(
        datos.get(
            "institucion",
            ""
        )
    )

    resultado[
        "carrera"
    ] = limpiar_texto(
        datos.get(
            "carrera",
            ""
        )
    )

    resultado[
        "dni"
    ] = limpiar_texto(
        datos.get(
            "dni",
            ""
        )
    )

    resultado[
        "telefono"
    ] = limpiar_texto(
        datos.get(
            "telefono",
            ""
        )
    )

    resultado[
        "email"
    ] = limpiar_texto(
        datos.get(
            "email",
            ""
        )
    )

    resultado[
        "cursos"
    ] = limpiar_lista_cursos(
        datos.get(
            "cursos",
            []
        )
    )

    return resultado


# ============================================================
# LIMPIAR LISTA DE CURSOS
# ============================================================

def limpiar_lista_cursos(
    cursos
):

    if not isinstance(
        cursos,
        list
    ):
        return []

    cursos_limpios = []
    filas_vistas = set()

    for item in cursos:

        if isinstance(
            item,
            str
        ):

            curso = limpiar_texto(
                item
            )

            nota = None
            creditos = None

        elif isinstance(
            item,
            dict
        ):

            curso = limpiar_texto(
                item.get(
                    "curso",
                    item.get(
                        "asignatura",
                        item.get(
                            "materia",
                            ""
                        )
                    )
                )
            )

            nota = convertir_nota(
                item.get(
                    "nota",
                    None
                )
            )

            creditos = convertir_creditos(
                item.get(
                    "creditos",
                    item.get(
                        "credito",
                        None
                    )
                )
            )

        else:
            continue

        if not curso:
            continue

        if es_texto_invalido(
            curso
        ):
            continue

        clave_curso = normalizar_curso(
            curso
        )

        if not clave_curso:
            continue

        # No eliminamos automáticamente el mismo nombre de curso
        # cuando la nota/crédito son diferentes. Puede existir en
        # más de un periodo.
        clave_fila = (
            clave_curso,
            nota,
            creditos
        )

        if clave_fila in filas_vistas:
            continue

        filas_vistas.add(
            clave_fila
        )

        cursos_limpios.append({
            "curso":
                curso,
            "nota":
                nota,
            "creditos":
                creditos
        })

    return cursos_limpios


# ============================================================
# CONVERTIR NOTA - ESTRICTO
# ============================================================

def convertir_nota(
    valor
):
    """
    Conversión estricta.

    Diferencia fundamental respecto a la versión anterior:
    NO busca cualquier número dentro de un texto largo.

    Así evitamos interpretar:
    "3 créditos" -> nota 3
    "código 13" -> nota 13
    "semestre 2" -> nota 2
    """

    if valor is None:
        return None

    if isinstance(
        valor,
        bool
    ):
        return None

    if isinstance(
        valor,
        int
    ):

        if 0 <= valor <= 20:
            return valor

        return None

    if isinstance(
        valor,
        float
    ):

        if 0 <= valor <= 20:

            if valor.is_integer():
                return int(
                    valor
                )

            return round(
                valor,
                2
            )

        return None

    texto = limpiar_texto(
        valor
    )

    if not texto:
        return None

    texto_normal = quitar_tildes(
        texto.upper()
    )

    mapa = {
        "CERO": 0,
        "UNO": 1,
        "DOS": 2,
        "TRES": 3,
        "CUATRO": 4,
        "CINCO": 5,
        "SEIS": 6,
        "SIETE": 7,
        "OCHO": 8,
        "NUEVE": 9,
        "DIEZ": 10,
        "ONCE": 11,
        "DOCE": 12,
        "TRECE": 13,
        "CATORCE": 14,
        "QUINCE": 15,
        "DIECISEIS": 16,
        "DIECISIETE": 17,
        "DIECIOCHO": 18,
        "DIECINUEVE": 19,
        "VEINTE": 20
    }

    # Solo aceptar palabra de nota si TODO el campo es la palabra.
    if texto_normal in mapa:
        return mapa[
            texto_normal
        ]

    # Solo aceptar un número si TODO el campo representa la nota.
    coincidencia = re.fullmatch(
        r"\s*(20|1[0-9]|[0-9])(?:[.,](\d+))?\s*",
        texto
    )

    if not coincidencia:
        return None

    try:

        numero = float(
            texto.replace(
                ",",
                "."
            )
        )

    except ValueError:
        return None

    if not 0 <= numero <= 20:
        return None

    if numero.is_integer():
        return int(
            numero
        )

    return round(
        numero,
        2
    )


# ============================================================
# CONVERTIR CRÉDITOS
# ============================================================

def convertir_creditos(
    valor
):

    if valor is None:
        return None

    if isinstance(
        valor,
        bool
    ):
        return None

    if isinstance(
        valor,
        (
            int,
            float
        )
    ):

        numero = float(
            valor
        )

    else:

        texto = limpiar_texto(
            valor
        )

        if not texto:
            return None

        coincidencia = re.fullmatch(
            r"\d{1,2}(?:[.,]\d+)?",
            texto
        )

        if not coincidencia:
            return None

        try:

            numero = float(
                texto.replace(
                    ",",
                    "."
                )
            )

        except ValueError:
            return None

    if numero < 0 or numero > 30:
        return None

    if numero.is_integer():
        return int(
            numero
        )

    return round(
        numero,
        2
    )


# ============================================================
# CONSERVAR DATOS GENERALES
# ============================================================

def conservar_datos_generales(
    principal,
    secundario
):

    resultado = dict(
        secundario
    )

    for campo in [
        "nombre",
        "institucion",
        "carrera",
        "dni",
        "telefono",
        "email"
    ]:

        if (
            principal.get(
                campo
            )
            and not resultado.get(
                campo
            )
        ):

            resultado[
                campo
            ] = principal[
                campo
            ]

    return resultado


# ============================================================
# DESCARTAR TEXTOS QUE NO SON CURSOS
# ============================================================

def es_texto_invalido(
    texto
):

    normal = normalizar_curso(
        texto
    )

    if not normal:
        return True

    exactos_invalidos = {
        "ASIGNATURA",
        "ASIGNATURAS",
        "CURSO",
        "CURSOS",
        "MATERIA",
        "MATERIAS",
        "NOTA",
        "NOTAS",
        "CREDITO",
        "CREDITOS",
        "PROMEDIO",
        "PROMEDIO PONDERADO",
        "TOTAL",
        "TOTAL DE CREDITOS"
    }

    if normal in exactos_invalidos:
        return True

    frases_invalidas = [
        "CERTIFICADO DE ESTUDIOS",
        "DIRECTOR GENERAL",
        "MINISTERIO DE EDUCACION",
        "PERIODO ACADEMICO",
        "FIRMADO DIGITALMENTE",
        "TOTAL DE CREDITOS",
        "PROMEDIO PONDERADO",
        "PAGINA "
    ]

    for frase in frases_invalidas:

        if frase in normal:
            return True

    # Un módulo puede ser un encabezado y no una asignatura.
    if normal.startswith(
        "MODULO FORMATIVO"
    ):
        return True

    if normal.startswith(
        "MODULO PROFESIONAL"
    ):
        return True

    if len(
        normal
    ) < 3:
        return True

    # Evitar una fila constituida solo por números.
    if re.fullmatch(
        r"\d+",
        normal
    ):
        return True

    return False


# ============================================================
# LIMPIAR TEXTO
# ============================================================

def limpiar_texto(
    texto
):

    if texto is None:
        return ""

    texto = str(
        texto
    ).strip()

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto


# ============================================================
# NORMALIZAR CURSO
# ============================================================

def normalizar_curso(
    texto
):

    texto = limpiar_texto(
        texto
    )

    texto = quitar_tildes(
        texto.upper()
    )

    texto = re.sub(
        r"[^A-Z0-9 ]",
        " ",
        texto
    )

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()


# ============================================================
# QUITAR TILDES
# ============================================================

def quitar_tildes(
    texto
):

    texto = unicodedata.normalize(
        "NFD",
        str(
            texto
        )
    )

    return "".join(
        caracter
        for caracter in texto
        if unicodedata.category(
            caracter
        ) != "Mn"
    )


# ============================================================
# ESTRUCTURA VACÍA
# ============================================================

def estructura_vacia():

    return {
        "nombre":
            "",
        "institucion":
            "",
        "carrera":
            "",
        "dni":
            "",
        "telefono":
            "",
        "email":
            "",
        "cursos":
            []
    }
