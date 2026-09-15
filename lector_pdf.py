import io
import os
import re
import shutil

import pymupdf
import pytesseract

from PIL import Image, ImageOps

from deepseek_lector import interpretar_certificado


# ============================================================
# CONFIGURACIÓN DE TESSERACT
# ============================================================

def configurar_tesseract():
    """Configura Tesseract automáticamente en Windows y Linux/Streamlit Cloud."""
    ruta_windows = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Windows local
    if os.path.exists(ruta_windows):
        pytesseract.pytesseract.tesseract_cmd = ruta_windows
        return ruta_windows

    # Linux / Streamlit Community Cloud / otros sistemas
    ruta_sistema = shutil.which("tesseract")
    if ruta_sistema:
        pytesseract.pytesseract.tesseract_cmd = ruta_sistema
        return ruta_sistema

    raise RuntimeError(
        "Tesseract OCR no está instalado o no se pudo localizar. "
        "En Streamlit Cloud agrega 'tesseract-ocr' y 'tesseract-ocr-spa' a packages.txt."
    )


RUTA_TESSERACT = configurar_tesseract()


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

MINIMO_CARACTERES_TEXTO_DIGITAL = 40


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def leer_pdf(
    archivo_pdf
):
    """
    Lee certificados PDF digitales o escaneados.

    Para PDFs escaneados usa OCR MULTIPASADA:
    1. PSM 6: lectura principal de filas/tablas.
    2. PSM 4: lectura auxiliar por columnas.
    3. recorte central de CALIFICACIÓN: refuerza NRO/LETRA.

    Las tres vistas se entregan a deepseek_lector.py para que
    pueda asociar cada ASIGNATURA con su NOTA sin inventarla.

    IMPORTANTE:
    - lector_pdf.py NO inventa cursos;
    - lector_pdf.py NO inventa notas;
    - si una nota sigue siendo dudosa, queda como None;
    - no se reutiliza la nota de una fila anterior o posterior.
    """

    if archivo_pdf is None:
        raise ValueError(
            "No se recibió ningún archivo PDF."
        )

    try:
        archivo_pdf.seek(
            0
        )
    except Exception:
        pass

    contenido = archivo_pdf.read()

    if not contenido:
        raise ValueError(
            "El archivo PDF está vacío."
        )

    try:
        documento = pymupdf.open(
            stream=contenido,
            filetype="pdf"
        )
    except Exception as error:
        raise ValueError(
            f"No se pudo abrir el PDF: {error}"
        ) from error

    texto_paginas = []
    diagnostico_paginas = []

    # OCR adicional de alto contraste.
    # Se conserva separado porque, además de enviarse a DeepSeek,
    # Python lo usa al final para recuperar notas faltantes del MISMO curso.
    textos_alto_contraste = []

    try:

        for numero_pagina, pagina in enumerate(
            documento,
            start=1
        ):

            texto_digital = extraer_texto_digital(
                pagina
            )

            if texto_digital_util(
                texto_digital
            ):

                texto_pagina = limpiar_texto_extraido(
                    texto_digital
                )

                metodo = "TEXTO DIGITAL"

                texto_paginas.append(
                    (
                        f"--- PÁGINA {numero_pagina} | "
                        f"{metodo} ---\n"
                        f"{texto_pagina}"
                    )
                )

                # Respaldo visual de alto contraste.
                texto_ac = extraer_ocr_alto_contraste(
                    pagina
                )

                if texto_ac:
                    textos_alto_contraste.append(
                        texto_ac
                    )

                    texto_paginas.append(
                        (
                            f"--- PÁGINA {numero_pagina} | "
                            f"OCR ALTO CONTRASTE ---\n"
                            f"{texto_ac}"
                        )
                    )

                diagnostico_paginas.append({
                    "pagina":
                        numero_pagina,
                    "metodo":
                        metodo,
                    "caracteres":
                        len(
                            texto_pagina
                        ),
                    "ocr_principal":
                        0,
                    "ocr_auxiliar":
                        0,
                    "ocr_calificacion":
                        0
                })

                continue

            # ====================================================
            # PDF ESCANEADO: OCR MULTIPASADA
            # ====================================================

            vistas_ocr = extraer_ocr_multivista(
                pagina
            )

            texto_principal = limpiar_texto_extraido(
                vistas_ocr.get(
                    "principal",
                    ""
                )
            )

            texto_auxiliar = limpiar_texto_extraido(
                vistas_ocr.get(
                    "auxiliar",
                    ""
                )
            )

            texto_calificacion = limpiar_texto_extraido(
                vistas_ocr.get(
                    "calificacion",
                    ""
                )
            )

            texto_alto_contraste = extraer_ocr_alto_contraste(
                pagina
            )

            if texto_alto_contraste:
                textos_alto_contraste.append(
                    texto_alto_contraste
                )

            secciones = [
                (
                    f"--- PÁGINA {numero_pagina} | "
                    f"OCR PRINCIPAL PSM6 ---\n"
                    f"{texto_principal}"
                )
            ]

            if texto_auxiliar:
                secciones.append(
                    (
                        f"--- PÁGINA {numero_pagina} | "
                        f"OCR AUXILIAR PSM4 ---\n"
                        f"{texto_auxiliar}"
                    )
                )

            if texto_calificacion:
                secciones.append(
                    (
                        f"--- PÁGINA {numero_pagina} | "
                        f"OCR COLUMNA CALIFICACIÓN ---\n"
                        f"{texto_calificacion}"
                    )
                )

            if texto_alto_contraste:
                secciones.append(
                    (
                        f"--- PÁGINA {numero_pagina} | "
                        f"OCR ALTO CONTRASTE ---\n"
                        f"{texto_alto_contraste}"
                    )
                )

            texto_paginas.append(
                "\n\n".join(
                    secciones
                )
            )

            diagnostico_paginas.append({
                "pagina":
                    numero_pagina,
                "metodo":
                    "OCR MULTIPASADA",
                "caracteres":
                    (
                        len(texto_principal)
                        + len(texto_auxiliar)
                        + len(texto_calificacion)
                    ),
                "ocr_principal":
                    len(
                        texto_principal
                    ),
                "ocr_auxiliar":
                    len(
                        texto_auxiliar
                    ),
                "ocr_calificacion":
                    len(
                        texto_calificacion
                    )
            })

    finally:

        documento.close()

    texto_completo = "\n\n".join(
        texto_paginas
    ).strip()

    if not texto_completo:
        raise ValueError(
            "No se pudo extraer texto del certificado."
        )

    # ========================================================
    # DEEPSEEK INTERPRETA LAS VISTAS OCR
    # ========================================================

    datos = interpretar_certificado(
        texto_completo
    )

    datos = normalizar_resultado_interpretacion(
        datos
    )

    # ========================================================
    # RESCATE DETERMINÍSTICO DE NOTAS FALTANTES
    #
    # Solo completa nota=None cuando encuentra el MISMO nombre de
    # curso y una nota válida en la MISMA línea del OCR.
    # Nunca copia una nota de otro curso.
    # ========================================================

    datos = recuperar_notas_desde_ocr_alto_contraste(
        datos=datos,
        textos_ocr=textos_alto_contraste
    )

    # ========================================================
    # DIAGNÓSTICO
    # ========================================================

    datos[
        "texto_completo"
    ] = texto_completo

    datos[
        "diagnostico_lectura"
    ] = diagnostico_paginas

    datos[
        "cantidad_paginas"
    ] = len(
        diagnostico_paginas
    )

    datos[
        "cantidad_cursos_detectados"
    ] = len(
        datos.get(
            "cursos",
            []
        )
    )

    return datos


# ============================================================
# OCR DE ALTO CONTRASTE
# ============================================================

def extraer_ocr_alto_contraste(
    pagina
):
    """
    Vista especializada para certificados escaneados con tablas.

    A diferencia del OCR normal:
    - renderiza a 4x;
    - convierte a escala de grises;
    - aplica autocontraste;
    - aplica umbral binario.

    En certificados con fondo de seguridad esta vista suele recuperar
    filas que el OCR normal pierde, por ejemplo:
        LENGUA 12 3
        MATEMATICA BASICA 12 4
        DIBUJO EN INGENIERIA 17 2

    Esta función solo devuelve TEXTO. La validación curso-nota se hace
    posteriormente y exige que ambos aparezcan en la MISMA línea.
    """

    try:
        pix = pagina.get_pixmap(
            matrix=pymupdf.Matrix(
                4.0,
                4.0
            ),
            alpha=False
        )

        imagen = Image.open(
            io.BytesIO(
                pix.tobytes(
                    "png"
                )
            )
        )

        imagen = ImageOps.grayscale(
            imagen
        )

        imagen = ImageOps.autocontrast(
            imagen
        )

        # 170 funcionó mejor en certificados con tramado/fondo verde
        # porque conserva letras y números pequeños sin arrastrar
        # demasiado ruido del fondo.
        imagen = imagen.point(
            lambda pixel: (
                0
                if pixel < 170
                else 255
            )
        )

        texto = pytesseract.image_to_string(
            imagen,
            lang="spa",
            config="--oem 3 --psm 6"
        )

        return limpiar_texto_extraido(
            texto
            or ""
        )

    except pytesseract.TesseractNotFoundError as error:
        raise RuntimeError(
            "Tesseract OCR no está disponible en este entorno. "
            f"Ruta configurada: {getattr(pytesseract.pytesseract, 'tesseract_cmd', 'no detectada')}"
        ) from error

    except Exception:
        # Es una vista de respaldo. Si falla, las otras vistas
        # continúan funcionando.
        return ""


# ============================================================
# NORMALIZACIÓN AUXILIAR PARA BÚSQUEDA EN OCR
# ============================================================

def normalizar_para_busqueda(
    texto
):
    if texto is None:
        return ""

    import unicodedata

    texto = unicodedata.normalize(
        "NFD",
        str(
            texto
        )
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(
            caracter
        ) != "Mn"
    )

    texto = texto.upper()

    texto = re.sub(
        r"[^A-Z0-9 ]+",
        " ",
        texto
    )

    return " ".join(
        texto.split()
    )


def extraer_nota_despues_del_curso(
    curso,
    linea
):
    """
    Busca una nota únicamente DESPUÉS del nombre del mismo curso
    dentro de la misma línea.

    Ejemplo:
        curso = MATEMATICA BASICA
        linea = MATEMATICA BASICA 12 4
        => 12

    El segundo número (4) corresponde normalmente a créditos y no se usa.
    """

    curso_n = normalizar_para_busqueda(
        curso
    )

    linea_n = normalizar_para_busqueda(
        linea
    )

    if not curso_n or not linea_n:
        return None

    posicion = linea_n.find(
        curso_n
    )

    if posicion < 0:
        return None

    resto = linea_n[
        posicion
        + len(
            curso_n
        ):
    ].strip()

    # La nota debe aparecer muy cerca del nombre del curso.
    # Esto evita capturar años/ciclos de otra sección de la misma línea.
    primeros_tokens = resto.split()[:4]

    for token in primeros_tokens:
        if not re.fullmatch(
            r"\d{1,2}",
            token
        ):
            continue

        try:
            numero = int(
                token
            )
        except ValueError:
            continue

        if 0 <= numero <= 20:
            return numero

    return None


def recuperar_notas_desde_ocr_alto_contraste(
    datos,
    textos_ocr
):
    """
    Completa exclusivamente notas faltantes.

    Reglas de seguridad:
    - nunca cambia una nota ya detectada;
    - curso y nota deben estar en la MISMA línea;
    - requiere coincidencia textual del nombre del curso;
    - nunca usa la nota de una línea vecina;
    - si no existe evidencia suficiente, conserva None.
    """

    if not isinstance(
        datos,
        dict
    ):
        return datos

    cursos = datos.get(
        "cursos",
        []
    )

    if not isinstance(
        cursos,
        list
    ):
        return datos

    lineas = []

    for texto in textos_ocr or []:
        for linea in str(
            texto
        ).splitlines():
            linea = linea.strip()

            if linea:
                lineas.append(
                    linea
                )

    if not lineas:
        return datos

    cursos_finales = []

    for item in cursos:
        if not isinstance(
            item,
            dict
        ):
            continue

        item_final = dict(
            item
        )

        nota_actual = item_final.get(
            "nota"
        )

        # No alterar notas ya válidas.
        try:
            if nota_actual is not None:
                nota_num = float(
                    nota_actual
                )

                if 0 <= nota_num <= 20:
                    cursos_finales.append(
                        item_final
                    )
                    continue
        except (
            TypeError,
            ValueError
        ):
            pass

        curso = str(
            item_final.get(
                "curso",
                ""
            )
            or ""
        ).strip()

        if not curso:
            cursos_finales.append(
                item_final
            )
            continue

        notas_encontradas = []

        for linea in lineas:
            nota = extraer_nota_despues_del_curso(
                curso=curso,
                linea=linea
            )

            if nota is not None:
                notas_encontradas.append(
                    nota
                )

        # Solo completar si la evidencia es inequívoca.
        notas_unicas = sorted(
            set(
                notas_encontradas
            )
        )

        if len(
            notas_unicas
        ) == 1:
            item_final[
                "nota"
            ] = notas_unicas[
                0
            ]

        cursos_finales.append(
            item_final
        )

    datos_finales = dict(
        datos
    )

    datos_finales[
        "cursos"
    ] = cursos_finales

    return datos_finales


# ============================================================
# EXTRAER TEXTO DIGITAL
# ============================================================

def extraer_texto_digital(
    pagina
):
    """
    Extrae texto digital intentando conservar el orden visual.
    """

    try:

        texto = pagina.get_text(
            "text",
            sort=True
        )

        return (
            texto
            or ""
        ).strip()

    except Exception:

        try:

            return (
                pagina.get_text()
                or ""
            ).strip()

        except Exception:

            return ""


# ============================================================
# DETERMINAR SI EL TEXTO DIGITAL ES ÚTIL
# ============================================================

def texto_digital_util(
    texto
):
    if not texto:
        return False

    texto_limpio = re.sub(
        r"\s+",
        " ",
        texto
    ).strip()

    if len(
        texto_limpio
    ) < MINIMO_CARACTERES_TEXTO_DIGITAL:
        return False

    letras = sum(
        caracter.isalpha()
        for caracter in texto_limpio
    )

    return letras >= 15


# ============================================================
# RENDERIZAR PÁGINA PARA OCR
# ============================================================

def renderizar_pagina_ocr(
    pagina,
    escala=3.0
):
    """
    Renderiza una página con resolución suficiente para tablas
    académicas pequeñas.
    """

    pix = pagina.get_pixmap(
        matrix=pymupdf.Matrix(
            escala,
            escala
        ),
        alpha=False
    )

    imagen = Image.open(
        io.BytesIO(
            pix.tobytes(
                "png"
            )
        )
    )

    imagen = ImageOps.grayscale(
        imagen
    )

    imagen = ImageOps.autocontrast(
        imagen
    )

    return imagen


# ============================================================
# OCR MULTIPASADA
# ============================================================

def extraer_ocr_multivista(
    pagina
):
    """
    Genera tres vistas del mismo certificado.

    PSM 6:
        suele conservar mejor cada fila de una tabla y, en
        certificados como UNSAAC, puede devolver:
        LENGUA Y COMUNICACION 14 CATORCE ...

    PSM 4:
        sirve como respaldo cuando la página tiene columnas.

    COLUMNA CALIFICACIÓN:
        se recorta la zona central donde habitualmente se ubican
        NRO y LETRA. No reemplaza la lectura principal: solo aporta
        evidencia adicional para que DeepSeek valide la nota.

    El recorte de calificación se usa únicamente como VISTA
    AUXILIAR. Por sí solo nunca asigna una nota a un curso.
    """

    try:

        imagen = renderizar_pagina_ocr(
            pagina,
            escala=3.0
        )

        texto_principal = pytesseract.image_to_string(
            imagen,
            lang="spa",
            config="--oem 3 --psm 6"
        )

        texto_auxiliar = pytesseract.image_to_string(
            imagen,
            lang="spa",
            config="--oem 3 --psm 4"
        )

        texto_calificacion = (
            extraer_columna_calificacion(
                imagen
            )
        )

        return {
            "principal":
                texto_principal
                or "",
            "auxiliar":
                texto_auxiliar
                or "",
            "calificacion":
                texto_calificacion
                or ""
        }

    except pytesseract.TesseractNotFoundError as error:

        raise RuntimeError(
            "Tesseract OCR no está disponible en este entorno. "
            f"Ruta configurada: {getattr(pytesseract.pytesseract, 'tesseract_cmd', 'no detectada')}"
        ) from error

    except Exception as error:

        raise RuntimeError(
            f"No se pudo realizar OCR en una página: {error}"
        ) from error


def extraer_columna_calificacion(
    imagen
):
    """
    Vista auxiliar para certificados tabulares.

    En muchos certificados universitarios, incluida la estructura
    probada de UNSAAC, ASIGNATURA ocupa la zona central y las
    columnas NRO/LETRA aparecen inmediatamente a su derecha.

    Se extrae una franja relativamente amplia para capturar:
    - nota numérica;
    - nota escrita en letras;
    - parte de fecha.

    Si el formato es diferente, esta vista puede contener ruido,
    pero no ocasiona una asignación automática porque DeepSeek debe
    contrastarla con la lectura principal.
    """

    try:

        ancho, alto = imagen.size

        izquierda = int(
            ancho * 0.50
        )

        derecha = int(
            ancho * 0.66
        )

        superior = int(
            alto * 0.18
        )

        inferior = int(
            alto * 0.84
        )

        if (
            derecha <= izquierda
            or inferior <= superior
        ):
            return ""

        recorte = imagen.crop(
            (
                izquierda,
                superior,
                derecha,
                inferior
            )
        )

        recorte = ImageOps.autocontrast(
            recorte
        )

        texto = pytesseract.image_to_string(
            recorte,
            lang="spa",
            config="--oem 3 --psm 6"
        )

        return (
            texto
            or ""
        ).strip()

    except Exception:

        # Esta vista es auxiliar. Si falla, no debe impedir que
        # PSM6 + PSM4 procesen el certificado.
        return ""


# ============================================================
# COMPATIBILIDAD: función OCR anterior
# ============================================================

def extraer_texto_ocr(
    pagina
):
    """
    Se conserva por compatibilidad con otros módulos.

    Devuelve la vista principal PSM6 de la nueva OCR multipasada.
    """

    vistas = extraer_ocr_multivista(
        pagina
    )

    return (
        vistas.get(
            "principal",
            ""
        )
        or ""
    ).strip()

# ============================================================
# LIMPIAR TEXTO EXTRAÍDO
# ============================================================

def limpiar_texto_extraido(
    texto
):
    """
    Limpia ruido sin destruir los saltos de línea.

    Es importante conservar los saltos porque DeepSeek necesita
    distinguir filas de curso y nota.
    """

    if texto is None:
        return ""

    texto = str(
        texto
    )

    texto = texto.replace(
        "\x00",
        ""
    )

    texto = texto.replace(
        "\r\n",
        "\n"
    )

    texto = texto.replace(
        "\r",
        "\n"
    )

    lineas = []

    for linea in texto.split(
        "\n"
    ):

        linea = re.sub(
            r"[ \t]+",
            " ",
            linea
        ).strip()

        # Mantener también líneas vacías de forma controlada.
        lineas.append(
            linea
        )

    # Evitar demasiados saltos seguidos.
    resultado = "\n".join(
        lineas
    )

    resultado = re.sub(
        r"\n{4,}",
        "\n\n\n",
        resultado
    )

    return resultado.strip()


# ============================================================
# NORMALIZAR RESPUESTA DE DEEPSEEK
# ============================================================

def normalizar_resultado_interpretacion(
    datos
):
    """
    Unifica la estructura que recibe app.py.

    Esperado:
    {
        "nombre": "",
        "dni": "",
        "institucion": "",
        "carrera": "",
        "cursos": [
            {
                "curso": "...",
                "nota": 15,
                "creditos": 3
            }
        ]
    }
    """

    if not isinstance(
        datos,
        dict
    ):
        datos = {}

    resultado = {
        "nombre":
            limpiar_campo_texto(
                datos.get(
                    "nombre",
                    ""
                )
            ),
        "dni":
            limpiar_campo_texto(
                datos.get(
                    "dni",
                    ""
                )
            ),
        "institucion":
            limpiar_campo_texto(
                datos.get(
                    "institucion",
                    ""
                )
            ),
        "carrera":
            limpiar_campo_texto(
                datos.get(
                    "carrera",
                    ""
                )
            ),
        "telefono":
            limpiar_campo_texto(
                datos.get(
                    "telefono",
                    ""
                )
            ),
        "email":
            limpiar_campo_texto(
                datos.get(
                    "email",
                    ""
                )
            )
    }

    # Aceptar algunas variantes por seguridad.
    cursos_originales = (
        datos.get(
            "cursos"
        )
        or datos.get(
            "asignaturas"
        )
        or datos.get(
            "materias"
        )
        or datos.get(
            "cursos_aprobados"
        )
        or []
    )

    if not isinstance(
        cursos_originales,
        list
    ):
        cursos_originales = []

    cursos_limpios = []

    for item in cursos_originales:

        curso_normalizado = normalizar_curso(
            item
        )

        if curso_normalizado is None:
            continue

        cursos_limpios.append(
            curso_normalizado
        )

    resultado[
        "cursos"
    ] = eliminar_duplicados_cursos(
        cursos_limpios
    )

    return resultado


# ============================================================
# NORMALIZAR UN CURSO
# ============================================================

def normalizar_curso(
    item
):
    """
    Convierte una fila de DeepSeek a:
    {
        "curso": str,
        "nota": int|float|None,
        "creditos": int|float|""
    }

    NUNCA copia una nota desde otra asignatura.
    """

    if isinstance(
        item,
        str
    ):

        curso = item.strip()

        if not curso:
            return None

        return {
            "curso":
                curso,
            "nota":
                None,
            "creditos":
                ""
        }

    if not isinstance(
        item,
        dict
    ):
        return None

    curso = (
        item.get(
            "curso"
        )
        or item.get(
            "asignatura"
        )
        or item.get(
            "materia"
        )
        or item.get(
            "nombre"
        )
        or ""
    )

    curso = limpiar_campo_texto(
        curso
    )

    if not curso:
        return None

    if es_fila_no_academica(
        curso
    ):
        return None

    nota = normalizar_nota(
        item.get(
            "nota",
            None
        )
    )

    creditos = normalizar_creditos(
        item.get(
            "creditos",
            item.get(
                "credito",
                ""
            )
        )
    )

    return {
        "curso":
            curso,
        "nota":
            nota,
        "creditos":
            creditos
    }


# ============================================================
# NORMALIZAR NOTA
# ============================================================

def normalizar_nota(
    valor
):
    """
    Solo acepta una nota individual válida.

    Si la nota no puede interpretarse con seguridad:
    devuelve None.

    Nunca reutiliza la nota anterior.
    """

    if valor is None:
        return None

    if isinstance(
        valor,
        str
    ):

        valor = valor.strip()

        if not valor:
            return None

        # Evitar textos como APROBADO, NSP, etc.
        coincidencia = re.fullmatch(
            r"\d{1,2}(?:[.,]\d+)?",
            valor
        )

        if not coincidencia:
            return None

        valor = valor.replace(
            ",",
            "."
        )

    try:

        numero = float(
            valor
        )

    except (
        TypeError,
        ValueError
    ):

        return None

    if numero < 0 or numero > 20:
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
# NORMALIZAR CRÉDITOS
# ============================================================

def normalizar_creditos(
    valor
):
    if valor is None:
        return ""

    if isinstance(
        valor,
        str
    ):

        valor = valor.strip()

        if not valor:
            return ""

        valor = valor.replace(
            ",",
            "."
        )

    try:

        numero = float(
            valor
        )

    except (
        TypeError,
        ValueError
    ):

        return ""

    if numero < 0 or numero > 30:
        return ""

    if numero.is_integer():
        return int(
            numero
        )

    return round(
        numero,
        2
    )


# ============================================================
# ELIMINAR DUPLICADOS
# ============================================================

def eliminar_duplicados_cursos(
    cursos
):
    """
    Elimina duplicados exactos sin mezclar notas.

    Si el mismo curso aparece dos veces con notas diferentes,
    se conservan ambas filas porque pueden corresponder a
    periodos distintos.
    """

    resultado = []
    vistos = set()

    for item in cursos:

        clave = (
            normalizar_texto_clave(
                item.get(
                    "curso",
                    ""
                )
            ),
            item.get(
                "nota"
            ),
            item.get(
                "creditos"
            )
        )

        if clave in vistos:
            continue

        vistos.add(
            clave
        )

        resultado.append(
            item
        )

    return resultado


# ============================================================
# FILAS QUE NO SON CURSOS
# ============================================================

def es_fila_no_academica(
    curso
):
    texto = normalizar_texto_clave(
        curso
    )

    prohibidos_exactos = {
        "ASIGNATURA",
        "CURSO",
        "CURSOS",
        "MATERIA",
        "MATERIAS",
        "NOTA",
        "NOTAS",
        "CREDITOS",
        "CREDITO",
        "PROMEDIO",
        "PROMEDIO PONDERADO",
        "TOTAL",
        "TOTAL CREDITOS"
    }

    if texto in prohibidos_exactos:
        return True

    if texto.startswith(
        "PROMEDIO "
    ):
        return True

    if texto.startswith(
        "TOTAL "
    ):
        return True

    return False


# ============================================================
# UTILIDADES
# ============================================================

def limpiar_campo_texto(
    valor
):
    if valor is None:
        return ""

    return re.sub(
        r"\s+",
        " ",
        str(
            valor
        )
    ).strip()


def normalizar_texto_clave(
    texto
):
    if texto is None:
        return ""

    texto = str(
        texto
    ).upper()

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()
