# ============================================================
# REGLAS PARTICULARES - CONTABILIDAD (2.5 AÑOS)
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:
CONTABILIDAD - 2.5 AÑOS

Mantiene:
- análisis como especialista en Contabilidad;
- convalidación por competencias;
- uso único de cada curso del certificado;
- notas reales del certificado;
- nota convalidante máxima 15;
- revisión manual asistida;
- recomendaciones al coordinador;
- control de falsos positivos contables.
"""

NOMBRE_CARRERA = "Contabilidad - 2.5 años"

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en CONTABILIDAD
y procesos de convalidación académica por competencias.

La carrera de destino es CONTABILIDAD - 2.5 AÑOS.

Evalúa las equivalencias desde las Ciencias Contables, Financieras,
Tributarias y Empresariales. Considera especialmente Contabilidad
General, Contabilidad Financiera, Contabilidad Intermedia y Avanzada,
Costos, Presupuestos, Contabilidad de Sociedades, Contabilidad
Gubernamental, Contabilidad Gerencial, Estados Financieros, Finanzas,
Matemática Financiera, Tributación, Auditoría, NIIF/NIC, Control
Interno, Sistemas de Información Contable, Economía, Administración,
Derecho Empresarial, Estadística, Investigación y Ética Profesional.

No compares únicamente palabras. Evalúa finalidad, competencias,
área profesional, nivel académico y aplicación contable.

No fuerces equivalencias solo para reducir suficiencias.
"""

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA CONTABILIDAD - 2.5 AÑOS:

1. Usa únicamente cursos reales del certificado y de la proforma.
2. No inventes cursos, notas ni contenidos de sílabos.
3. Un curso del certificado puede utilizarse como máximo una vez.
4. Un curso UPRIT puede recibir como máximo una equivalencia.
5. Prioriza coincidencias exactas.
6. Luego evalúa equivalencias académicamente defendibles.
7. La similitud de palabras no basta para convalidar.
8. Si requiere revisar sílabos, indica REQUIERE VALIDACIÓN ACADÉMICA.
9. Toda nota parcial debe proceder del certificado.
10. La nota convalidante se calcula solo con notas parciales reales.
11. La nota convalidante máxima es 15.
12. No reutilices asignaturas ya empleadas.
13. No fuerces equivalencias para disminuir suficiencias.
14. La recomendación automática no constituye aprobación.
15. La decisión final corresponde al coordinador académico.
"""

EQUIVALENCIAS_ORIENTATIVAS = {
    "CONTABILIDAD BASICA": [
        "CONTABILIDAD", "CONTABILIDAD GENERAL",
        "FUNDAMENTOS DE CONTABILIDAD", "INTRODUCCION A LA CONTABILIDAD",
        "CONTABILIDAD I", "PRINCIPIOS DE CONTABILIDAD"
    ],
    "CONTABILIDAD GENERAL": [
        "CONTABILIDAD I", "CONTABILIDAD BASICA",
        "FUNDAMENTOS DE CONTABILIDAD", "CONTABILIDAD FINANCIERA I"
    ],
    "CONTABILIDAD FINANCIERA": [
        "CONTABILIDAD II", "CONTABILIDAD FINANCIERA I",
        "CONTABILIDAD EMPRESARIAL", "ESTADOS FINANCIEROS",
        "CONTABILIDAD INTERMEDIA"
    ],
    "CONTABILIDAD FINANCIERA II": [
        "CONTABILIDAD III", "CONTABILIDAD INTERMEDIA II",
        "CONTABILIDAD AVANZADA", "CONTABILIDAD FINANCIERA II"
    ],
    "CONTABILIDAD DE COSTOS": [
        "COSTOS", "CONTABILIDAD DE COSTOS I", "COSTOS Y PRESUPUESTOS",
        "COSTOS EMPRESARIALES", "COSTOS INDUSTRIALES"
    ],
    "COSTOS Y PRESUPUESTOS": [
        "CONTABILIDAD DE COSTOS", "PRESUPUESTOS",
        "PRESUPUESTOS EMPRESARIALES", "GESTION PRESUPUESTARIA",
        "COSTOS EMPRESARIALES"
    ],
    "CONTABILIDAD DE SOCIEDADES": [
        "CONTABILIDAD SOCIETARIA", "CONTABILIDAD DE EMPRESAS",
        "CONTABILIDAD DE SOCIEDADES I", "SOCIEDADES MERCANTILES"
    ],
    "CONTABILIDAD GUBERNAMENTAL": [
        "CONTABILIDAD PUBLICA", "CONTABILIDAD DEL SECTOR PUBLICO",
        "CONTABILIDAD ESTATAL", "CONTABILIDAD GUBERNAMENTAL I"
    ],
    "CONTABILIDAD GERENCIAL": [
        "CONTABILIDAD ADMINISTRATIVA",
        "CONTABILIDAD PARA LA TOMA DE DECISIONES",
        "GESTION CONTABLE", "INFORMACION CONTABLE PARA LA GESTION"
    ],
    "ESTADOS FINANCIEROS": [
        "ANALISIS DE ESTADOS FINANCIEROS",
        "ELABORACION DE ESTADOS FINANCIEROS",
        "INFORMACION FINANCIERA", "PRESENTACION DE ESTADOS FINANCIEROS"
    ],
    "ANALISIS FINANCIERO": [
        "ANALISIS DE ESTADOS FINANCIEROS",
        "INTERPRETACION DE ESTADOS FINANCIEROS",
        "DIAGNOSTICO FINANCIERO", "ANALISIS E INTERPRETACION FINANCIERA"
    ],
    "FINANZAS": [
        "FINANZAS EMPRESARIALES", "ADMINISTRACION FINANCIERA",
        "GESTION FINANCIERA", "FINANZAS CORPORATIVAS"
    ],
    "MATEMATICA FINANCIERA": [
        "MATEMATICAS FINANCIERAS", "CALCULO FINANCIERO",
        "MATEMATICA APLICADA A LAS FINANZAS", "OPERACIONES FINANCIERAS"
    ],
    "TRIBUTACION": [
        "LEGISLACION TRIBUTARIA", "DERECHO TRIBUTARIO",
        "SISTEMA TRIBUTARIO", "TRIBUTACION I", "IMPUESTOS"
    ],
    "TRIBUTACION I": [
        "LEGISLACION TRIBUTARIA", "DERECHO TRIBUTARIO",
        "SISTEMA TRIBUTARIO PERUANO", "IMPUESTO A LA RENTA"
    ],
    "TRIBUTACION II": [
        "TRIBUTACION AVANZADA", "IMPUESTOS II",
        "FISCALIDAD EMPRESARIAL", "TRIBUTACION EMPRESARIAL"
    ],
    "AUDITORIA": [
        "AUDITORIA FINANCIERA", "AUDITORIA CONTABLE",
        "FUNDAMENTOS DE AUDITORIA", "AUDITORIA I"
    ],
    "AUDITORIA FINANCIERA": [
        "AUDITORIA II", "AUDITORIA DE ESTADOS FINANCIEROS",
        "AUDITORIA CONTABLE", "AUDITORIA EXTERNA"
    ],
    "AUDITORIA INTERNA": [
        "CONTROL INTERNO", "AUDITORIA OPERATIVA",
        "AUDITORIA INTERNA Y CONTROL"
    ],
    "NORMAS INTERNACIONALES DE INFORMACION FINANCIERA": [
        "NIIF", "NORMAS INTERNACIONALES DE CONTABILIDAD",
        "NIC", "NORMATIVA CONTABLE INTERNACIONAL",
        "CONTABILIDAD INTERNACIONAL"
    ],
    "SISTEMAS CONTABLES": [
        "SISTEMAS DE INFORMACION CONTABLE", "SOFTWARE CONTABLE",
        "CONTABILIDAD COMPUTARIZADA", "SISTEMAS DE CONTABILIDAD"
    ],
    "CONTABILIDAD COMPUTARIZADA": [
        "SOFTWARE CONTABLE", "SISTEMAS CONTABLES",
        "APLICACIONES CONTABLES", "INFORMATICA CONTABLE"
    ],
    "ECONOMIA": [
        "ECONOMIA GENERAL", "FUNDAMENTOS DE ECONOMIA",
        "INTRODUCCION A LA ECONOMIA", "PRINCIPIOS DE ECONOMIA"
    ],
    "FUNDAMENTOS DE LA ADMINISTRACION": [
        "FUNDAMENTOS DE ADMINISTRACION", "ADMINISTRACION GENERAL",
        "INTRODUCCION A LA ADMINISTRACION", "TEORIA ADMINISTRATIVA",
        "PROCESO ADMINISTRATIVO"
    ],
    "DERECHO EMPRESARIAL Y DE SOCIEDADES": [
        "DERECHO EMPRESARIAL", "DERECHO COMERCIAL",
        "DERECHO SOCIETARIO", "LEGISLACION EMPRESARIAL",
        "LEGISLACION COMERCIAL"
    ],
    "MATEMATICA BASICA": [
        "MATEMATICA", "MATEMATICA GENERAL",
        "MATEMATICAS BASICAS", "MATEMATICA APLICADA"
    ],
    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA", "ESTADISTICA GENERAL",
        "PROBABILIDAD Y ESTADISTICA", "ESTADISTICA APLICADA"
    ],
    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION", "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION", "SEMINARIO DE INVESTIGACION"
    ],
    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA", "ETICA PROFESIONAL", "ETICA DEL CONTADOR",
        "DEONTOLOGIA PROFESIONAL", "ETICA Y DEONTOLOGIA"
    ],
    "TECNOLOGIA Y TRANSFORMACION DIGITAL": [
        "TRANSFORMACION DIGITAL", "TECNOLOGIAS DE INFORMACION",
        "INNOVACION DIGITAL", "SISTEMAS DE INFORMACION",
        "TECNOLOGIAS DIGITALES"
    ]
}

FALSOS_POSITIVOS = [
    "Contabilidad no equivale automáticamente a Finanzas.",
    "Contabilidad no equivale automáticamente a Economía.",
    "Economía no equivale automáticamente a Contabilidad.",
    "Matemática General no equivale automáticamente a Matemática Financiera.",
    "Cálculo de Costos no equivale a Cálculo matemático.",
    "Auditoría de Sistemas no equivale automáticamente a Auditoría Financiera.",
    "Auditoría Informática no equivale automáticamente a Auditoría Contable.",
    "Informática no equivale automáticamente a Sistemas Contables.",
    "Ofimática no equivale automáticamente a Contabilidad Computarizada.",
    "Sistemas Operativos no equivale a Sistemas Contables.",
    "Base de Datos no equivale automáticamente a Sistemas Contables.",
    "Derecho Constitucional no equivale automáticamente a Derecho Tributario.",
    "Administración Pública no equivale automáticamente a Contabilidad Gubernamental.",
    "Tributación no equivale automáticamente a Derecho Empresarial.",
    "Contabilidad de Costos no equivale automáticamente a Presupuestos.",
    "Finanzas no equivale automáticamente a Análisis de Estados Financieros."
]

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

    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    "nombre_especialidad": "CONTABILIDAD",
    "programa": "2.5 AÑOS",
    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS
}

def obtener_instrucciones_especialista():
    bloqueos = "\n".join(
        f"- {item}"
        for item in FALSOS_POSITIVOS
    )

    return f"""
{PERFIL_ESPECIALISTA}

{REGLAS_ACADEMICAS}

FALSOS POSITIVOS Y BLOQUEOS:
{bloqueos}

La carrera de destino es CONTABILIDAD - 2.5 AÑOS.

Prioriza coincidencias exactas y después equivalencias
académicamente defendibles. Si existe una alternativa razonable
pero requiere revisión de contenidos, recomiéndala al coordinador.

No inventes cursos ni notas.
No reutilices una asignatura del certificado.
La decisión final corresponde al coordinador académico.
"""

def obtener_configuracion():
    return {
        "carrera": NOMBRE_CARRERA,
        "programa": "2.5 AÑOS",
        "reglas": REGLAS,
        "perfil_especialista": PERFIL_ESPECIALISTA,
        "reglas_academicas": REGLAS_ACADEMICAS,
        "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
        "falsos_positivos": FALSOS_POSITIVOS,
        "instrucciones_especialista": obtener_instrucciones_especialista()
    }
