# ============================================================
# REGLAS PARTICULARES
# EDUCACIÓN SECUNDARIA CON MENCIÓN EN IDIOMAS EXTRANJEROS
# PROGRAMA 1 AÑO
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

EDUCACIÓN SECUNDARIA CON MENCIÓN EN IDIOMAS EXTRANJEROS - 2.5 AÑOS

Formato especial de Educación:
1. Convalidación por competencias.
2. Asignaturas no convalidadas.
3. Resumen final de modalidad.

Modalidades:
- POR COMPETENCIA
- EXAMEN DE SUFICIENCIA
"""

NOMBRE_CARRERA = (
    "Educación Secundaria con mención en Idiomas Extranjeros - 2.5 años"
)

PROGRAMA = "2.5 AÑOS"


# ============================================================
# PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
EDUCACIÓN SECUNDARIA CON MENCIÓN EN IDIOMAS EXTRANJEROS,
formación docente, lingüística aplicada, enseñanza de lenguas
extranjeras y convalidación académica por competencias.

Debes evaluar las equivalencias desde una perspectiva pedagógica,
lingüística, comunicativa e intercultural.

Considera especialmente:

- Inglés I, II, III y niveles superiores.
- Gramática Inglesa.
- Fonética y Fonología Inglesa.
- Comprensión Oral.
- Comprensión Escrita.
- Producción Oral.
- Producción Escrita.
- Conversación.
- Pronunciación.
- Lingüística General.
- Lingüística Aplicada.
- Sociolingüística.
- Semántica y Pragmática.
- Metodología de Enseñanza de Idiomas.
- Didáctica del Inglés.
- Didáctica de Lenguas Extranjeras.
- Evaluación del Aprendizaje de Idiomas.
- Literatura Inglesa y Norteamericana.
- Cultura y Civilización.
- Traducción básica.
- Pedagogía General.
- Didáctica General.
- Psicología General.
- Psicología Educativa.
- Currículo.
- Programación Curricular.
- Evaluación Educativa.
- TIC aplicadas a la Educación.
- E-learning.
- Inteligencia Artificial en Educación.
- Práctica Preprofesional Pedagógica.
- Metodología de la Investigación.
- Investigación Educativa.
- Ética y Responsabilidad Profesional.

No te limites a comparar palabras.

Debes analizar:
1. idioma y nivel lingüístico;
2. finalidad pedagógica;
3. competencia comunicativa;
4. componente oral o escrito;
5. contenido lingüístico;
6. nivel académico;
7. relación con la enseñanza secundaria;
8. correspondencia real con la asignatura UPRIT.

No fuerces equivalencias únicamente para reducir suficiencias.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS:

1. Usa únicamente cursos REALES del certificado y de la proforma.
2. No inventes cursos.
3. No inventes notas.
4. No inventes sílabos ni contenidos no disponibles.
5. Un curso del certificado puede utilizarse máximo una vez.
6. Un curso UPRIT puede recibir máximo una equivalencia.
7. Prioriza coincidencias exactas.
8. Luego evalúa equivalencias por idioma, nivel, finalidad y competencia.
9. Una semejanza de palabras no demuestra equivalencia.
10. Si requiere revisar sílabos, marcar REQUIERE VALIDACIÓN ACADÉMICA.
11. Las recomendaciones son apoyo al coordinador.
12. Toda nota parcial procede exclusivamente del certificado.
13. La nota convalidante se calcula solo con notas reales.
14. La nota convalidante máxima es 15.
15. Inglés Técnico no equivale automáticamente a Comunicación.
16. Inglés General no equivale automáticamente a Didáctica del Inglés.
17. Fonética del español no equivale automáticamente a Fonética Inglesa.
18. Traducción no equivale automáticamente a Gramática Inglesa.
19. Literatura Universal no equivale automáticamente a Literatura Inglesa.
20. Lingüística General no equivale automáticamente a Lingüística Aplicada.
21. Práctica profesional no docente no equivale automáticamente a Práctica Preprofesional Pedagógica.
22. La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    "INGLES I": [
        "INGLES",
        "INGLES I",
        "IDIOMA INGLES I",
        "INGLES BASICO"
    ],

    "INGLES II": [
        "INGLES II",
        "IDIOMA INGLES II",
        "INGLES PREINTERMEDIO"
    ],

    "INGLES III": [
        "INGLES III",
        "IDIOMA INGLES III",
        "INGLES INTERMEDIO"
    ],

    "INGLES IV": [
        "INGLES IV",
        "IDIOMA INGLES IV",
        "INGLES INTERMEDIO AVANZADO"
    ],

    "GRAMATICA INGLESA": [
        "GRAMATICA DEL INGLES",
        "GRAMATICA INGLESA",
        "ENGLISH GRAMMAR"
    ],

    "FONETICA Y FONOLOGIA INGLESA": [
        "FONETICA INGLESA",
        "FONOLOGIA INGLESA",
        "FONETICA Y FONOLOGIA DEL INGLES",
        "ENGLISH PHONETICS"
    ],

    "COMPRENSION ORAL": [
        "LISTENING",
        "COMPRENSION AUDITIVA",
        "COMPRENSION ORAL EN INGLES"
    ],

    "COMPRENSION ESCRITA": [
        "READING",
        "COMPRENSION LECTORA EN INGLES",
        "LECTURA EN INGLES"
    ],

    "PRODUCCION ORAL": [
        "SPEAKING",
        "EXPRESION ORAL EN INGLES",
        "COMUNICACION ORAL EN INGLES"
    ],

    "PRODUCCION ESCRITA": [
        "WRITING",
        "REDACCION EN INGLES",
        "EXPRESION ESCRITA EN INGLES"
    ],

    "CONVERSACION EN INGLES": [
        "CONVERSACION",
        "ENGLISH CONVERSATION",
        "COMUNICACION ORAL EN INGLES"
    ],

    "PRONUNCIACION INGLESA": [
        "PRONUNCIACION",
        "ENGLISH PRONUNCIATION",
        "PRONUNCIACION DEL INGLES"
    ],

    "LINGUISTICA GENERAL": [
        "LINGUISTICA",
        "LINGUISTICA GENERAL",
        "INTRODUCCION A LA LINGUISTICA"
    ],

    "LINGUISTICA APLICADA": [
        "LINGUISTICA APLICADA",
        "LINGUISTICA APLICADA A LA ENSENANZA DE IDIOMAS",
        "APPLIED LINGUISTICS"
    ],

    "SOCIOLINGUISTICA": [
        "SOCIOLINGUISTICA",
        "LENGUA Y SOCIEDAD",
        "VARIACION LINGUISTICA"
    ],

    "SEMANTICA Y PRAGMATICA": [
        "SEMANTICA",
        "PRAGMATICA",
        "SEMANTICA Y PRAGMATICA"
    ],

    "DIDACTICA DEL INGLES": [
        "DIDACTICA DEL IDIOMA INGLES",
        "ENSENANZA DEL INGLES",
        "METODOLOGIA DE LA ENSENANZA DEL INGLES",
        "ELT METHODOLOGY"
    ],

    "DIDACTICA DE IDIOMAS EXTRANJEROS": [
        "DIDACTICA DE LENGUAS EXTRANJERAS",
        "METODOLOGIA DE ENSENANZA DE IDIOMAS",
        "FOREIGN LANGUAGE TEACHING"
    ],

    "EVALUACION DEL APRENDIZAJE DE IDIOMAS": [
        "EVALUACION EN LA ENSENANZA DE IDIOMAS",
        "LANGUAGE ASSESSMENT",
        "EVALUACION DEL INGLES"
    ],

    "LITERATURA INGLESA": [
        "LITERATURA EN INGLES",
        "LITERATURA INGLESA",
        "ENGLISH LITERATURE"
    ],

    "LITERATURA NORTEAMERICANA": [
        "LITERATURA AMERICANA",
        "LITERATURA NORTEAMERICANA",
        "AMERICAN LITERATURE"
    ],

    "CULTURA Y CIVILIZACION ANGLOSAJONA": [
        "CULTURA INGLESA",
        "CIVILIZACION ANGLOSAJONA",
        "CULTURA DE PAISES DE HABLA INGLESA"
    ],

    "TRADUCCION BASICA": [
        "TRADUCCION",
        "TRADUCCION INGLES ESPANOL",
        "INTRODUCCION A LA TRADUCCION"
    ],

    "PEDAGOGIA GENERAL": [
        "PEDAGOGIA",
        "PEDAGOGIA GENERAL",
        "FUNDAMENTOS DE PEDAGOGIA"
    ],

    "DIDACTICA GENERAL": [
        "DIDACTICA",
        "DIDACTICA GENERAL",
        "TEORIA DE LA ENSENANZA"
    ],

    "PSICOLOGIA GENERAL": [
        "PSICOLOGIA",
        "PSICOLOGIA GENERAL",
        "INTRODUCCION A LA PSICOLOGIA"
    ],

    "PSICOLOGIA EDUCATIVA": [
        "PSICOLOGIA DE LA EDUCACION",
        "PSICOLOGIA DEL APRENDIZAJE",
        "PSICOLOGIA ESCOLAR"
    ],

    "CURRICULO GENERAL": [
        "CURRICULO",
        "CURRICULO GENERAL",
        "TEORIA CURRICULAR",
        "DISENO CURRICULAR"
    ],

    "PROGRAMACION CURRICULAR": [
        "PLANIFICACION CURRICULAR",
        "PROGRAMACION CURRICULAR",
        "DIVERSIFICACION CURRICULAR"
    ],

    "EVALUACION EDUCATIVA": [
        "EVALUACION DEL APRENDIZAJE",
        "EVALUACION EDUCACIONAL",
        "EVALUACION PEDAGOGICA"
    ],

    "TIC APLICADAS A LA EDUCACION": [
        "TIC EN EDUCACION",
        "TECNOLOGIAS EDUCATIVAS",
        "INFORMATICA EDUCATIVA"
    ],

    "E-LEARNING EN ENSENANZA Y APRENDIZAJE VIRTUAL": [
        "E-LEARNING",
        "EDUCACION VIRTUAL",
        "APRENDIZAJE VIRTUAL",
        "ENTORNOS VIRTUALES DE APRENDIZAJE"
    ],

    "INTELIGENCIA ARTIFICIAL EN EDUCACION": [
        "INTELIGENCIA ARTIFICIAL APLICADA A LA EDUCACION",
        "IA EN EDUCACION"
    ],

    "PRACTICA PREPROFESIONAL PEDAGOGICA I": [
        "PRACTICA PREPROFESIONAL I",
        "PRACTICA PEDAGOGICA I",
        "PRACTICA DOCENTE I"
    ],

    "PRACTICA PREPROFESIONAL PEDAGOGICA II": [
        "PRACTICA PREPROFESIONAL II",
        "PRACTICA PEDAGOGICA II",
        "PRACTICA DOCENTE II"
    ],

    "PRACTICA PREPROFESIONAL PEDAGOGICA III": [
        "PRACTICA PREPROFESIONAL III",
        "PRACTICA PEDAGOGICA III",
        "PRACTICA DOCENTE III"
    ],

    "PRACTICA PREPROFESIONAL PEDAGOGICA IV": [
        "PRACTICA PREPROFESIONAL IV",
        "PRACTICA PEDAGOGICA IV",
        "PRACTICA DOCENTE IV"
    ],

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION"
    ],

    "INVESTIGACION EDUCATIVA": [
        "INVESTIGACION PEDAGOGICA",
        "INVESTIGACION EN EDUCACION",
        "METODOLOGIA DE INVESTIGACION EDUCATIVA"
    ],

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA Y DEONTOLOGIA"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [
    "Inglés Técnico no equivale automáticamente a Comunicación.",
    "Inglés General no equivale automáticamente a Didáctica del Inglés.",
    "Fonética del español no equivale automáticamente a Fonética Inglesa.",
    "Traducción no equivale automáticamente a Gramática Inglesa.",
    "Literatura Universal no equivale automáticamente a Literatura Inglesa.",
    "Lingüística General no equivale automáticamente a Lingüística Aplicada.",
    "Comunicación no equivale automáticamente a Inglés.",
    "Práctica profesional no docente no equivale automáticamente a Práctica Preprofesional Pedagógica.",
    "Programación informática no equivale a Programación Curricular.",
    "Inteligencia Artificial general no equivale automáticamente a Inteligencia Artificial en Educación."
]


# ============================================================
# REGLAS DEL MOTOR
# ============================================================

REGLAS = {

    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    "umbral_caso_especial": 5,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,
    "generar_caso_especial": False,
    "reevaluar_caso_especial_con_ia": False,

    "programa": PROGRAMA,

    "formato_educacion_tres_bloques": True,
    "usar_bloque_competencias": True,
    "actualizar_asignaturas_no_convalidadas": True,
    "usar_resumen_modalidad": True,

    "modalidad_competencia": "POR COMPETENCIA",
    "modalidad_suficiencia": "EXAMEN DE SUFICIENCIA",

    "respetar_marca_asterisco_suficiencia": True,
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    "nombre_especialidad":
        "EDUCACIÓN SECUNDARIA CON MENCIÓN EN IDIOMAS EXTRANJEROS",

    "perfil_especialista":
        PERFIL_ESPECIALISTA,

    "reglas_academicas_especialista":
        REGLAS_ACADEMICAS,

    "equivalencias_orientativas":
        EQUIVALENCIAS_ORIENTATIVAS,

    "falsos_positivos_especialidad":
        FALSOS_POSITIVOS
}


def obtener_instrucciones_especialista():

    bloqueos = "\n".join(
        f"- {item}"
        for item in FALSOS_POSITIVOS
    )

    return f"""
{PERFIL_ESPECIALISTA}

{REGLAS_ACADEMICAS}

BLOQUEOS Y FALSOS POSITIVOS:
{bloqueos}

La carrera de destino es:

EDUCACIÓN SECUNDARIA CON MENCIÓN EN IDIOMAS EXTRANJEROS - 2.5 AÑOS.

El formato institucional utiliza:
1. CONVALIDACIÓN POR COMPETENCIAS.
2. ASIGNATURAS NO CONVALIDADAS.
3. RESUMEN FINAL DE MODALIDAD.

Si existe equivalencia:
MODALIDAD = POR COMPETENCIA.

Si el curso queda para examen:
MODALIDAD = EXAMEN DE SUFICIENCIA.

No inventes cursos.
No inventes notas.
No reutilices cursos del certificado.
No fuerces equivalencias.

La decisión final corresponde al coordinador académico.
"""


def obtener_configuracion():
    return {
        "carrera": NOMBRE_CARRERA,
        "programa": PROGRAMA,
        "reglas": REGLAS,
        "perfil_especialista": PERFIL_ESPECIALISTA,
        "reglas_academicas": REGLAS_ACADEMICAS,
        "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
        "falsos_positivos": FALSOS_POSITIVOS,
        "instrucciones_especialista": obtener_instrucciones_especialista()
    }
