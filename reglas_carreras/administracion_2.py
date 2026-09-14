# ============================================================
# REGLAS PARTICULARES - ADMINISTRACIÓN DE EMPRESAS (2 AÑOS)
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:
ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS

Reglas principales:
- evaluación como especialista en Administración;
- convalidación por competencias;
- no repetir cursos del certificado;
- notas reales del certificado;
- nota convalidante máxima 15;
- revisión manual asistida;
- recomendaciones al coordinador;
- no generar CASO ESPECIAL automáticamente solo por superar 7.
"""

NOMBRE_CARRERA = "Administración de Empresas - 2 años"


PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
ADMINISTRACIÓN DE EMPRESAS y convalidación académica por competencias.

Evalúa las equivalencias desde una perspectiva curricular propia
de las Ciencias Empresariales.

Considera especialmente:

- Fundamentos de Administración.
- Administración General.
- Gestión Empresarial.
- Planeamiento Estratégico.
- Organización y Métodos.
- Procesos Administrativos.
- Gestión del Talento Humano.
- Recursos Humanos.
- Comportamiento Organizacional.
- Liderazgo.
- Contabilidad.
- Contabilidad Financiera.
- Contabilidad de Costos.
- Finanzas.
- Matemática Financiera.
- Economía.
- Microeconomía y Macroeconomía.
- Marketing.
- Investigación de Mercados.
- Marketing Digital.
- Gestión Comercial y Ventas.
- Logística.
- Cadena de Suministro.
- Gestión de Operaciones.
- Gestión de la Calidad.
- Emprendimiento.
- Innovación.
- Gestión de Proyectos.
- Derecho Empresarial.
- Estadística.
- Matemática.
- Metodología de la Investigación.
- Responsabilidad Social.
- Ética Profesional.
- Transformación Digital.
- Sistemas de Información Empresarial.

No te limites a comparar palabras.
Evalúa significado, finalidad, competencias, área profesional
y nivel académico.

No fuerces equivalencias solo para reducir suficiencias.
"""


REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS:

1. Usa únicamente cursos REALES del certificado y de la proforma.
2. No inventes cursos.
3. No inventes notas.
4. No inventes sílabos ni contenidos no disponibles.
5. Un curso del certificado puede utilizarse máximo una vez.
6. Un curso UPRIT puede recibir máximo una equivalencia.
7. Prioriza coincidencias exactas.
8. Después evalúa equivalencias académicamente defendibles.
9. Una similitud de palabras no constituye equivalencia.
10. Si requiere comprobar sílabos, marca REQUIERE VALIDACIÓN ACADÉMICA.
11. Las recomendaciones son apoyo al coordinador, no aprobación automática.
12. La nota parcial procede exclusivamente del certificado.
13. La nota convalidante se calcula solo con notas parciales reales.
14. La nota convalidante máxima es 15.
15. No fuerces equivalencias para disminuir artificialmente suficiencias.
"""


EQUIVALENCIAS_ORIENTATIVAS = {
    "FUNDAMENTOS DE LA ADMINISTRACION": [
        "FUNDAMENTOS DE ADMINISTRACION",
        "INTRODUCCION A LA ADMINISTRACION",
        "ADMINISTRACION GENERAL",
        "TEORIA DE LA ADMINISTRACION",
        "PRINCIPIOS DE ADMINISTRACION",
        "PROCESO ADMINISTRATIVO"
    ],
    "ADMINISTRACION GENERAL": [
        "FUNDAMENTOS DE ADMINISTRACION",
        "GESTION EMPRESARIAL",
        "PROCESO ADMINISTRATIVO",
        "ADMINISTRACION DE EMPRESAS"
    ],
    "GESTION EMPRESARIAL": [
        "ADMINISTRACION DE EMPRESAS",
        "GESTION DE EMPRESAS",
        "DIRECCION DE EMPRESAS",
        "GERENCIA EMPRESARIAL"
    ],
    "PLANEAMIENTO ESTRATEGICO": [
        "PLANIFICACION ESTRATEGICA",
        "DIRECCION ESTRATEGICA",
        "GESTION ESTRATEGICA",
        "ADMINISTRACION ESTRATEGICA"
    ],
    "CONTABILIDAD BASICA": [
        "CONTABILIDAD",
        "CONTABILIDAD GENERAL",
        "FUNDAMENTOS DE CONTABILIDAD",
        "INTRODUCCION A LA CONTABILIDAD",
        "CONTABILIDAD I"
    ],
    "CONTABILIDAD FINANCIERA": [
        "CONTABILIDAD II",
        "CONTABILIDAD EMPRESARIAL",
        "CONTABILIDAD FINANCIERA I",
        "ESTADOS FINANCIEROS"
    ],
    "CONTABILIDAD DE COSTOS": [
        "COSTOS",
        "COSTOS Y PRESUPUESTOS",
        "CONTABILIDAD DE COSTOS I",
        "COSTOS EMPRESARIALES"
    ],
    "ECONOMIA": [
        "ECONOMIA GENERAL",
        "FUNDAMENTOS DE ECONOMIA",
        "INTRODUCCION A LA ECONOMIA",
        "PRINCIPIOS DE ECONOMIA"
    ],
    "FINANZAS": [
        "FINANZAS EMPRESARIALES",
        "ADMINISTRACION FINANCIERA",
        "GESTION FINANCIERA",
        "FINANZAS CORPORATIVAS"
    ],
    "MATEMATICA FINANCIERA": [
        "MATEMATICAS FINANCIERAS",
        "CALCULO FINANCIERO",
        "MATEMATICA APLICADA A LAS FINANZAS"
    ],
    "MARKETING": [
        "MERCADOTECNIA",
        "FUNDAMENTOS DE MARKETING",
        "MARKETING I",
        "GESTION DE MARKETING"
    ],
    "INVESTIGACION DE MERCADOS": [
        "ESTUDIO DE MERCADO",
        "INVESTIGACION COMERCIAL",
        "ANALISIS DE MERCADOS"
    ],
    "GESTION DEL TALENTO HUMANO": [
        "RECURSOS HUMANOS",
        "GESTION DE RECURSOS HUMANOS",
        "ADMINISTRACION DE PERSONAL",
        "GESTION DEL CAPITAL HUMANO"
    ],
    "COMPORTAMIENTO ORGANIZACIONAL": [
        "COMPORTAMIENTO HUMANO EN LAS ORGANIZACIONES",
        "CONDUCTA ORGANIZACIONAL",
        "COMPORTAMIENTO Y CULTURA ORGANIZACIONAL"
    ],
    "LIDERAZGO": [
        "LIDERAZGO EMPRESARIAL",
        "LIDERAZGO ORGANIZACIONAL",
        "HABILIDADES DIRECTIVAS",
        "DIRECCION Y LIDERAZGO"
    ],
    "LOGISTICA": [
        "LOGISTICA EMPRESARIAL",
        "GESTION LOGISTICA",
        "ADMINISTRACION LOGISTICA",
        "LOGISTICA Y ABASTECIMIENTO"
    ],
    "GESTION DE OPERACIONES": [
        "ADMINISTRACION DE OPERACIONES",
        "DIRECCION DE OPERACIONES",
        "GESTION DE LA PRODUCCION",
        "PRODUCCION Y OPERACIONES"
    ],
    "GESTION DE LA CALIDAD": [
        "CONTROL DE CALIDAD",
        "CALIDAD TOTAL",
        "SISTEMAS DE GESTION DE CALIDAD",
        "ADMINISTRACION DE LA CALIDAD"
    ],
    "GESTION DE PROYECTOS": [
        "ADMINISTRACION DE PROYECTOS",
        "DIRECCION DE PROYECTOS",
        "FORMULACION Y EVALUACION DE PROYECTOS",
        "PROJECT MANAGEMENT"
    ],
    "EMPRENDIMIENTO": [
        "EMPRENDIMIENTO EMPRESARIAL",
        "CREACION DE EMPRESAS",
        "DESARROLLO EMPRENDEDOR",
        "INICIATIVA EMPRESARIAL"
    ],
    "DERECHO EMPRESARIAL Y DE SOCIEDADES": [
        "DERECHO EMPRESARIAL",
        "DERECHO COMERCIAL",
        "LEGISLACION EMPRESARIAL",
        "DERECHO SOCIETARIO"
    ],
    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICAS BASICAS",
        "MATEMATICA APLICADA"
    ],
    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "PROBABILIDAD Y ESTADISTICA",
        "ESTADISTICA APLICADA"
    ],
    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION"
    ],
    "TECNOLOGIA Y TRANSFORMACION DIGITAL": [
        "TRANSFORMACION DIGITAL",
        "TECNOLOGIAS DIGITALES",
        "TECNOLOGIAS DE INFORMACION",
        "SISTEMAS DE INFORMACION",
        "INNOVACION DIGITAL"
    ],
    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA EMPRESARIAL",
        "DEONTOLOGIA PROFESIONAL"
    ]
}


FALSOS_POSITIVOS = [
    "Administración de medicamentos no equivale a Administración General.",
    "Administración educativa no equivale automáticamente a Gestión Empresarial.",
    "Contabilidad no equivale automáticamente a Finanzas.",
    "Economía no equivale automáticamente a Contabilidad.",
    "Matemática General no equivale automáticamente a Matemática Financiera.",
    "Estadística no equivale automáticamente a Investigación de Mercados.",
    "Psicología General no equivale automáticamente a Comportamiento Organizacional.",
    "Marketing no equivale automáticamente a Investigación de Mercados.",
    "Logística no equivale automáticamente a Gestión de Operaciones.",
    "Derecho General no equivale automáticamente a Derecho Empresarial.",
    "Ofimática no equivale automáticamente a Transformación Digital.",
    "Seguridad Industrial no equivale automáticamente a Gestión de la Calidad."
]


REGLAS = {
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Semáforo institucional de revisión
    "umbral_caso_especial": 5,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # Flujo moderno: revisión manual asistida
    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,
    "generar_caso_especial": False,
    "reevaluar_caso_especial_con_ia": False,

    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    "nombre_especialidad": "ADMINISTRACIÓN DE EMPRESAS",
    "programa": "2 AÑOS",
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

BLOQUEOS Y FALSOS POSITIVOS:
{bloqueos}

La carrera de destino es ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS.

Cuando exista una alternativa académicamente razonable pero no
completamente segura, preséntala como recomendación para revisión
del coordinador.

No inventes cursos ni notas.
No reutilices una asignatura ya empleada.
La decisión final corresponde al coordinador académico.
"""


def obtener_configuracion():
    return {
        "carrera": NOMBRE_CARRERA,
        "programa": "2 AÑOS",
        "reglas": REGLAS,
        "perfil_especialista": PERFIL_ESPECIALISTA,
        "reglas_academicas": REGLAS_ACADEMICAS,
        "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
        "falsos_positivos": FALSOS_POSITIVOS,
        "instrucciones_especialista": obtener_instrucciones_especialista()
    }
