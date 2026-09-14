# ============================================================
# REGLAS PARTICULARES - PSICOLOGÍA
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a la carrera de Psicología.

OBJETIVO:
- mantener la lógica general de convalidación por competencias;
- realizar la evaluación semántica como especialista en Psicología;
- recomendar equivalencias académicamente defendibles;
- evitar falsos positivos frecuentes;
- permitir revisión manual asistida por el coordinador;
- nunca inventar cursos ni notas.
"""

NOMBRE_CARRERA = "Psicología"


# ============================================================
# PERFIL ACADÉMICO DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
PSICOLOGÍA y en procesos de convalidación académica por
competencias.

Debes analizar las equivalencias desde una perspectiva
curricular propia de la formación profesional en Psicología.

Considera especialmente las siguientes áreas:

- Psicología General.
- Historia y fundamentos de la Psicología.
- Psicología del Desarrollo.
- Psicología Evolutiva.
- Desarrollo Humano.
- Psicología del Aprendizaje.
- Procesos Cognitivos.
- Psicología Social.
- Psicología Organizacional.
- Psicología del Trabajo.
- Psicología Educativa.
- Psicología Clínica.
- Psicopatología.
- Evaluación Psicológica.
- Psicometría.
- Teoría de los Tests.
- Personalidad.
- Entrevista Psicológica.
- Técnicas de Intervención.
- Consejería y Orientación.
- Neuropsicología.
- Bases Biológicas de la Conducta.
- Psicofisiología.
- Estadística.
- Metodología de la Investigación.
- Análisis de Datos.
- Ética profesional.
- Investigación psicológica.

No te limites únicamente a comparar palabras.

Debes analizar:

1. significado académico;
2. área psicológica;
3. finalidad de la asignatura;
4. competencias desarrolladas;
5. nivel académico;
6. relación real con la formación profesional en Psicología.

No fuerces equivalencias únicamente para reducir pendientes
o suficiencias.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA PSICOLOGÍA:

1. Usa únicamente cursos REALES presentes en las listas recibidas.
2. No inventes cursos.
3. No inventes notas.
4. No inventes contenidos de sílabos.
5. Un curso del certificado puede utilizarse como máximo una vez.
6. Un curso UPRIT puede recibir como máximo una equivalencia.
7. Prioriza coincidencias exactas y equivalencias académicamente
   defendibles.
8. Una semejanza de palabras no implica equivalencia.
9. Si la relación requiere comprobar contenidos, indicar
   REQUIERE VALIDACIÓN ACADÉMICA.
10. Las recomendaciones son solo apoyo al coordinador.
11. Toda nota parcial debe proceder exclusivamente del certificado.
12. La nota convalidante se calcula únicamente con notas reales.
13. La nota convalidante máxima es 15.
14. No convertir automáticamente cursos médicos o clínicos en
    cursos psicológicos si no existe una correspondencia clara.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    "PSICOLOGIA GENERAL": [
        "INTRODUCCION A LA PSICOLOGIA",
        "FUNDAMENTOS DE PSICOLOGIA",
        "BASES DE LA PSICOLOGIA",
        "PSICOLOGIA I"
    ],

    "PSICOLOGIA DEL DESARROLLO": [
        "PSICOLOGIA EVOLUTIVA",
        "DESARROLLO HUMANO",
        "DESARROLLO PSICOLOGICO",
        "CICLO VITAL"
    ],

    "PSICOLOGIA DEL DESARROLLO I": [
        "PSICOLOGIA EVOLUTIVA I",
        "DESARROLLO HUMANO I",
        "DESARROLLO PSICOLOGICO I"
    ],

    "PSICOLOGIA DEL DESARROLLO II": [
        "PSICOLOGIA EVOLUTIVA II",
        "DESARROLLO HUMANO II",
        "DESARROLLO PSICOLOGICO II"
    ],

    "PSICOLOGIA SOCIAL": [
        "COMPORTAMIENTO SOCIAL",
        "PROCESOS PSICOSOCIALES",
        "PSICOLOGIA DE GRUPOS",
        "PSICOLOGIA Y SOCIEDAD"
    ],

    "PSICOLOGIA ORGANIZACIONAL": [
        "PSICOLOGIA DEL TRABAJO",
        "PSICOLOGIA LABORAL",
        "COMPORTAMIENTO ORGANIZACIONAL",
        "PSICOLOGIA DE LAS ORGANIZACIONES"
    ],

    "PSICOLOGIA EDUCATIVA": [
        "PSICOLOGIA DEL APRENDIZAJE",
        "PSICOLOGIA ESCOLAR",
        "ORIENTACION EDUCATIVA",
        "PROCESOS DE APRENDIZAJE"
    ],

    "PSICOMETRIA": [
        "MEDICION PSICOLOGICA",
        "TEORIA DE LOS TESTS",
        "CONSTRUCCION DE PRUEBAS",
        "EVALUACION PSICOMETRICA"
    ],

    "PSICOPATOLOGIA": [
        "PSICOLOGIA ANORMAL",
        "TRASTORNOS PSICOLOGICOS",
        "PSICOPATOLOGIA GENERAL"
    ],

    "EVALUACION PSICOLOGICA": [
        "DIAGNOSTICO PSICOLOGICO",
        "EVALUACION PSICODIAGNOSTICA",
        "TECNICAS DE EVALUACION PSICOLOGICA"
    ],

    "PERSONALIDAD": [
        "PSICOLOGIA DE LA PERSONALIDAD",
        "TEORIAS DE LA PERSONALIDAD"
    ],

    "NEUROPSICOLOGIA": [
        "BASES NEUROPSICOLOGICAS",
        "NEUROCIENCIAS Y CONDUCTA",
        "NEUROPSICOLOGIA CLINICA"
    ],

    "BASES BIOLOGICAS DE LA CONDUCTA": [
        "PSICOBIOLOGIA",
        "BIOLOGIA DE LA CONDUCTA",
        "BASES BIOLOGICAS DEL COMPORTAMIENTO",
        "PSICOFISIOLOGIA"
    ],

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION"
    ],

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "ESTADISTICA APLICADA",
        "PROBABILIDAD Y ESTADISTICA"
    ],

    "ANALISIS DE DATOS": [
        "ANALISIS ESTADISTICO",
        "PROCESAMIENTO DE DATOS",
        "ESTADISTICA APLICADA"
    ],

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "DEONTOLOGIA",
        "ETICA Y DEONTOLOGIA"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [
    "Psiquiatría no equivale automáticamente a Psicología Clínica.",
    "Psiquiatría no equivale automáticamente a Psicopatología.",
    "Psiquiatría no equivale automáticamente a Evaluación Psicológica.",
    "Neurología no equivale automáticamente a Neuropsicología.",
    "Anatomía no equivale automáticamente a Bases Biológicas de la Conducta.",
    "Medicina no equivale automáticamente a Psicología General.",
    "Coaching no equivale automáticamente a Psicoterapia.",
    "Recursos Humanos no equivale automáticamente a Psicología Organizacional.",
    "Estadística no equivale automáticamente a Psicometría.",
    "Educación Física no equivale a Psicología ni a cursos clínicos.",
    "Trabajo Social no equivale automáticamente a Psicología Social.",
    "Orientación Vocacional no equivale automáticamente a Psicología Educativa.",
]


# ============================================================
# REGLAS QUE LEE CONVALIDACIONES.PY
# ============================================================

REGLAS = {

    # Competencias
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Revisión manual asistida
    "umbral_caso_especial": 7,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # Igual que Industrial:
    # no generar Word de CASO ESPECIAL solo por superar 7.
    "reevaluar_caso_especial_con_ia": False,
    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,
    "generar_caso_especial": False,

    # Ajustar según la estructura de la proforma.
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # Perfil especializado
    "nombre_especialidad": "PSICOLOGÍA",
    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS,
}


# ============================================================
# INSTRUCCIONES COMPLETAS DEL ESPECIALISTA
# ============================================================

def obtener_instrucciones_especialista():

    bloqueos = "\n".join(
        f"- {item}"
        for item in FALSOS_POSITIVOS
    )

    return f"""
{PERFIL_ESPECIALISTA}

{REGLAS_ACADEMICAS}

BLOQUEOS ESPECÍFICOS:

{bloqueos}

RECUERDA:

La carrera de destino es PSICOLOGÍA.

Analiza las equivalencias desde la perspectiva curricular,
científica y profesional de la Psicología.

No conviertas automáticamente asignaturas médicas,
psiquiátricas, educativas, sociales o administrativas en
cursos psicológicos si no existe una correspondencia
académica defendible.

No inventes asignaturas ni notas.

No reutilices una misma asignatura del certificado.

Cuando exista duda, presenta la opción como recomendación para
que el coordinador realice la evaluación final.
"""


def obtener_configuracion():

    return {
        "carrera":
            NOMBRE_CARRERA,

        "reglas":
            REGLAS,

        "perfil_especialista":
            PERFIL_ESPECIALISTA,

        "reglas_academicas":
            REGLAS_ACADEMICAS,

        "equivalencias_orientativas":
            EQUIVALENCIAS_ORIENTATIVAS,

        "falsos_positivos":
            FALSOS_POSITIVOS,

        "instrucciones_especialista":
            obtener_instrucciones_especialista()
    }