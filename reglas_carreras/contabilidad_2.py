# ============================================================
# REGLAS PARTICULARES - CONTABILIDAD (2 AÑOS)
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

CONTABILIDAD - 2 AÑOS

Objetivos:
- evaluar equivalencias como especialista en Contabilidad;
- mantener la lógica general de convalidación por competencias;
- no repetir cursos del certificado;
- utilizar exclusivamente notas reales del certificado;
- mantener nota convalidante máxima de 15;
- usar revisión manual asistida por el coordinador;
- recomendar equivalencias académicamente defendibles;
- evitar falsos positivos propios del área contable.
"""


NOMBRE_CARRERA = "Contabilidad - 2 años"


# ============================================================
# PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
CONTABILIDAD y en procesos de convalidación académica por
competencias.

La carrera de destino es CONTABILIDAD - 2 AÑOS.

Debes evaluar las posibles equivalencias desde una perspectiva
curricular y profesional propia de las Ciencias Contables,
Financieras, Tributarias y Empresariales.

Considera especialmente las siguientes áreas:

- Contabilidad General.
- Fundamentos de Contabilidad.
- Contabilidad Financiera.
- Contabilidad Intermedia.
- Contabilidad Avanzada.
- Contabilidad de Costos.
- Costos Empresariales.
- Costos Industriales.
- Presupuestos.
- Contabilidad de Sociedades.
- Contabilidad Gubernamental.
- Contabilidad Gerencial.
- Estados Financieros.
- Análisis e Interpretación de Estados Financieros.
- Finanzas.
- Finanzas Empresariales.
- Matemática Financiera.
- Tributación.
- Legislación Tributaria.
- Derecho Tributario.
- Impuesto a la Renta.
- Impuesto General a las Ventas.
- Auditoría.
- Auditoría Financiera.
- Auditoría Tributaria.
- Auditoría Interna.
- Normas Internacionales de Información Financiera.
- NIIF.
- NIC.
- Sistemas de Información Contable.
- Software Contable.
- Economía.
- Administración.
- Derecho Empresarial.
- Derecho Comercial.
- Estadística.
- Matemática.
- Investigación Científica.
- Ética Profesional.
- Responsabilidad Profesional.
- Gestión Empresarial.
- Control Interno.

No debes limitarte únicamente a comparar palabras.

Debes analizar:

1. significado académico;
2. finalidad de la asignatura;
3. área contable o empresarial;
4. competencias desarrolladas;
5. nivel de profundidad;
6. aplicación profesional;
7. relación con el perfil de formación de Contabilidad.

No fuerces equivalencias únicamente para reducir la cantidad de
cursos pendientes o exámenes de suficiencia.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA CONTABILIDAD - 2 AÑOS:

1. Utiliza únicamente cursos REALES presentes en el certificado
   y en la proforma.

2. No inventes nombres de asignaturas.

3. No inventes notas.

4. No inventes contenidos de sílabos.

5. Un curso del certificado puede utilizarse como máximo una vez.

6. Un curso UPRIT puede recibir como máximo una equivalencia.

7. Prioriza las coincidencias exactas.

8. Luego analiza equivalencias académicamente defendibles por
   significado, contenido habitual, finalidad y competencia.

9. Una similitud de palabras no constituye una equivalencia.

10. Si una relación requiere comprobar sílabos, debe indicarse:
    REQUIERE VALIDACIÓN ACADÉMICA.

11. Las recomendaciones automáticas son únicamente apoyo para el
    coordinador.

12. Una recomendación no constituye aprobación automática.

13. Toda nota parcial debe proceder exclusivamente del certificado.

14. Si una nota no está disponible, no la inventes.

15. La nota convalidante se calcula solo con notas parciales reales.

16. La nota convalidante máxima es 15.

17. No reutilices una asignatura ya usada en otra convalidación.

18. No fuerces equivalencias para disminuir artificialmente los
    cursos de suficiencia.

19. La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # --------------------------------------------------------
    # CONTABILIDAD GENERAL
    # --------------------------------------------------------

    "CONTABILIDAD BASICA": [
        "CONTABILIDAD",
        "CONTABILIDAD GENERAL",
        "FUNDAMENTOS DE CONTABILIDAD",
        "INTRODUCCION A LA CONTABILIDAD",
        "CONTABILIDAD I",
        "PRINCIPIOS DE CONTABILIDAD"
    ],

    "CONTABILIDAD GENERAL": [
        "CONTABILIDAD I",
        "CONTABILIDAD BASICA",
        "FUNDAMENTOS DE CONTABILIDAD",
        "CONTABILIDAD FINANCIERA I"
    ],


    # --------------------------------------------------------
    # CONTABILIDAD FINANCIERA
    # --------------------------------------------------------

    "CONTABILIDAD FINANCIERA": [
        "CONTABILIDAD II",
        "CONTABILIDAD FINANCIERA I",
        "CONTABILIDAD EMPRESARIAL",
        "ESTADOS FINANCIEROS",
        "CONTABILIDAD INTERMEDIA"
    ],

    "CONTABILIDAD FINANCIERA II": [
        "CONTABILIDAD III",
        "CONTABILIDAD INTERMEDIA II",
        "CONTABILIDAD AVANZADA",
        "CONTABILIDAD FINANCIERA II"
    ],


    # --------------------------------------------------------
    # COSTOS
    # --------------------------------------------------------

    "CONTABILIDAD DE COSTOS": [
        "COSTOS",
        "CONTABILIDAD DE COSTOS I",
        "COSTOS Y PRESUPUESTOS",
        "COSTOS EMPRESARIALES",
        "COSTOS INDUSTRIALES"
    ],

    "COSTOS Y PRESUPUESTOS": [
        "CONTABILIDAD DE COSTOS",
        "PRESUPUESTOS",
        "PRESUPUESTOS EMPRESARIALES",
        "GESTION PRESUPUESTARIA",
        "COSTOS EMPRESARIALES"
    ],


    # --------------------------------------------------------
    # SOCIEDADES
    # --------------------------------------------------------

    "CONTABILIDAD DE SOCIEDADES": [
        "CONTABILIDAD SOCIETARIA",
        "CONTABILIDAD DE EMPRESAS",
        "CONTABILIDAD DE SOCIEDADES I",
        "SOCIEDADES MERCANTILES"
    ],


    # --------------------------------------------------------
    # CONTABILIDAD GUBERNAMENTAL
    # --------------------------------------------------------

    "CONTABILIDAD GUBERNAMENTAL": [
        "CONTABILIDAD PUBLICA",
        "CONTABILIDAD DEL SECTOR PUBLICO",
        "CONTABILIDAD ESTATAL",
        "CONTABILIDAD GUBERNAMENTAL I"
    ],


    # --------------------------------------------------------
    # CONTABILIDAD GERENCIAL
    # --------------------------------------------------------

    "CONTABILIDAD GERENCIAL": [
        "CONTABILIDAD ADMINISTRATIVA",
        "CONTABILIDAD PARA LA TOMA DE DECISIONES",
        "GESTION CONTABLE",
        "INFORMACION CONTABLE PARA LA GESTION"
    ],


    # --------------------------------------------------------
    # ESTADOS FINANCIEROS
    # --------------------------------------------------------

    "ESTADOS FINANCIEROS": [
        "ANALISIS DE ESTADOS FINANCIEROS",
        "ELABORACION DE ESTADOS FINANCIEROS",
        "INFORMACION FINANCIERA",
        "PRESENTACION DE ESTADOS FINANCIEROS"
    ],

    "ANALISIS FINANCIERO": [
        "ANALISIS DE ESTADOS FINANCIEROS",
        "INTERPRETACION DE ESTADOS FINANCIEROS",
        "DIAGNOSTICO FINANCIERO",
        "ANALISIS E INTERPRETACION FINANCIERA"
    ],


    # --------------------------------------------------------
    # FINANZAS
    # --------------------------------------------------------

    "FINANZAS": [
        "FINANZAS EMPRESARIALES",
        "ADMINISTRACION FINANCIERA",
        "GESTION FINANCIERA",
        "FINANZAS CORPORATIVAS"
    ],

    "MATEMATICA FINANCIERA": [
        "MATEMATICAS FINANCIERAS",
        "CALCULO FINANCIERO",
        "MATEMATICA APLICADA A LAS FINANZAS",
        "OPERACIONES FINANCIERAS"
    ],


    # --------------------------------------------------------
    # TRIBUTACIÓN
    # --------------------------------------------------------

    "TRIBUTACION": [
        "LEGISLACION TRIBUTARIA",
        "DERECHO TRIBUTARIO",
        "SISTEMA TRIBUTARIO",
        "TRIBUTACION I",
        "IMPUESTOS"
    ],

    "TRIBUTACION I": [
        "LEGISLACION TRIBUTARIA",
        "DERECHO TRIBUTARIO",
        "SISTEMA TRIBUTARIO PERUANO",
        "IMPUESTO A LA RENTA"
    ],

    "TRIBUTACION II": [
        "TRIBUTACION AVANZADA",
        "IMPUESTOS II",
        "FISCALIDAD EMPRESARIAL",
        "TRIBUTACION EMPRESARIAL"
    ],


    # --------------------------------------------------------
    # AUDITORÍA
    # --------------------------------------------------------

    "AUDITORIA": [
        "AUDITORIA FINANCIERA",
        "AUDITORIA CONTABLE",
        "FUNDAMENTOS DE AUDITORIA",
        "AUDITORIA I"
    ],

    "AUDITORIA FINANCIERA": [
        "AUDITORIA II",
        "AUDITORIA DE ESTADOS FINANCIEROS",
        "AUDITORIA CONTABLE",
        "AUDITORIA EXTERNA"
    ],

    "AUDITORIA INTERNA": [
        "CONTROL INTERNO",
        "AUDITORIA OPERATIVA",
        "AUDITORIA INTERNA Y CONTROL"
    ],


    # --------------------------------------------------------
    # NIIF / NIC
    # --------------------------------------------------------

    "NORMAS INTERNACIONALES DE INFORMACION FINANCIERA": [
        "NIIF",
        "NORMAS INTERNACIONALES DE CONTABILIDAD",
        "NIC",
        "NORMATIVA CONTABLE INTERNACIONAL",
        "CONTABILIDAD INTERNACIONAL"
    ],


    # --------------------------------------------------------
    # SISTEMAS CONTABLES
    # --------------------------------------------------------

    "SISTEMAS CONTABLES": [
        "SISTEMAS DE INFORMACION CONTABLE",
        "SOFTWARE CONTABLE",
        "CONTABILIDAD COMPUTARIZADA",
        "SISTEMAS DE CONTABILIDAD"
    ],

    "CONTABILIDAD COMPUTARIZADA": [
        "SOFTWARE CONTABLE",
        "SISTEMAS CONTABLES",
        "APLICACIONES CONTABLES",
        "INFORMATICA CONTABLE"
    ],


    # --------------------------------------------------------
    # ECONOMÍA
    # --------------------------------------------------------

    "ECONOMIA": [
        "ECONOMIA GENERAL",
        "FUNDAMENTOS DE ECONOMIA",
        "INTRODUCCION A LA ECONOMIA",
        "PRINCIPIOS DE ECONOMIA"
    ],


    # --------------------------------------------------------
    # ADMINISTRACIÓN
    # --------------------------------------------------------

    "FUNDAMENTOS DE LA ADMINISTRACION": [
        "FUNDAMENTOS DE ADMINISTRACION",
        "ADMINISTRACION GENERAL",
        "INTRODUCCION A LA ADMINISTRACION",
        "TEORIA ADMINISTRATIVA",
        "PROCESO ADMINISTRATIVO"
    ],


    # --------------------------------------------------------
    # DERECHO
    # --------------------------------------------------------

    "DERECHO EMPRESARIAL Y DE SOCIEDADES": [
        "DERECHO EMPRESARIAL",
        "DERECHO COMERCIAL",
        "DERECHO SOCIETARIO",
        "LEGISLACION EMPRESARIAL",
        "LEGISLACION COMERCIAL"
    ],


    # --------------------------------------------------------
    # MATEMÁTICA
    # --------------------------------------------------------

    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICAS BASICAS",
        "MATEMATICA APLICADA"
    ],


    # --------------------------------------------------------
    # ESTADÍSTICA
    # --------------------------------------------------------

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "PROBABILIDAD Y ESTADISTICA",
        "ESTADISTICA APLICADA"
    ],


    # --------------------------------------------------------
    # INVESTIGACIÓN
    # --------------------------------------------------------

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION",
        "SEMINARIO DE INVESTIGACION"
    ],


    # --------------------------------------------------------
    # ÉTICA
    # --------------------------------------------------------

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA DEL CONTADOR",
        "DEONTOLOGIA PROFESIONAL",
        "ETICA Y DEONTOLOGIA"
    ],


    # --------------------------------------------------------
    # TRANSFORMACIÓN DIGITAL
    # --------------------------------------------------------

    "TECNOLOGIA Y TRANSFORMACION DIGITAL": [
        "TRANSFORMACION DIGITAL",
        "TECNOLOGIAS DE INFORMACION",
        "INNOVACION DIGITAL",
        "SISTEMAS DE INFORMACION",
        "TECNOLOGIAS DIGITALES"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [

    "Contabilidad no equivale automáticamente a Finanzas.",

    "Contabilidad no equivale automáticamente a Economía.",

    "Economía no equivale automáticamente a Contabilidad.",

    "Matemática General no equivale automáticamente a Matemática Financiera.",

    "Cálculo de Costos no equivale a Cálculo matemático.",

    "Costos no equivale automáticamente a Matemática Financiera.",

    "Auditoría de Sistemas no equivale automáticamente a Auditoría Financiera.",

    "Auditoría Informática no equivale automáticamente a Auditoría Contable.",

    "Seguridad Informática no equivale a Control Interno.",

    "Informática no equivale automáticamente a Sistemas Contables.",

    "Ofimática no equivale automáticamente a Contabilidad Computarizada.",

    "Sistemas Operativos no equivale a Sistemas Contables.",

    "Base de Datos no equivale automáticamente a Sistemas Contables.",

    "Derecho Constitucional no equivale automáticamente a Derecho Tributario.",

    "Derecho Penal no equivale automáticamente a Derecho Empresarial.",

    "Administración Pública no equivale automáticamente a Contabilidad Gubernamental.",

    "Gestión Pública no equivale automáticamente a Contabilidad Gubernamental.",

    "Tributación no equivale automáticamente a Derecho Empresarial.",

    "Contabilidad de Costos no equivale automáticamente a Presupuestos.",

    "Estadística no equivale automáticamente a Análisis Financiero.",

    "Finanzas no equivale automáticamente a Análisis de Estados Financieros."
]


# ============================================================
# REGLAS QUE LEE CONVALIDACIONES.PY
# ============================================================

REGLAS = {

    # --------------------------------------------------------
    # CONVALIDACIÓN POR COMPETENCIAS
    # --------------------------------------------------------

    "permitir_un_faltante_en_competencia": True,

    "faltantes_para_suficiencia": 2,

    "tope_nota_convalidante": 15,


    # --------------------------------------------------------
    # SUFICIENCIAS
    # --------------------------------------------------------

    "umbral_caso_especial": 5,

    "maximo_suficiencias": 7,

    "maximo_suficiencias_final": 7,


    # --------------------------------------------------------
    # REVISIÓN MANUAL ASISTIDA
    # --------------------------------------------------------

    "revision_manual_asistida": True,

    "autoseleccionar_recomendaciones": True,

    "generar_caso_especial": False,

    "reevaluar_caso_especial_con_ia": False,


    # --------------------------------------------------------
    # ESTRUCTURA DE PROFORMA
    # --------------------------------------------------------

    "detectar_competencia_a_la_izquierda_de_asignatura": True,


    # --------------------------------------------------------
    # PERFIL
    # --------------------------------------------------------

    "nombre_especialidad":
        "CONTABILIDAD",

    "programa":
        "2 AÑOS",

    "perfil_especialista":
        PERFIL_ESPECIALISTA,

    "reglas_academicas_especialista":
        REGLAS_ACADEMICAS,

    "equivalencias_orientativas":
        EQUIVALENCIAS_ORIENTATIVAS,

    "falsos_positivos_especialidad":
        FALSOS_POSITIVOS
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

FALSOS POSITIVOS Y BLOQUEOS:

{bloqueos}

RECUERDA:

La carrera de destino es CONTABILIDAD - 2 AÑOS.

Analiza las equivalencias desde la perspectiva contable,
financiera, tributaria, empresarial y de auditoría.

Prioriza las coincidencias exactas.

Después revisa equivalencias académicamente defendibles.

Si existe una alternativa razonable pero requiere revisión
de contenidos, puede recomendarse al coordinador.

No inventes cursos.

No inventes notas.

No reutilices una asignatura del certificado.

No conviertas automáticamente asignaturas administrativas,
informáticas, jurídicas o financieras en cursos contables si
no existe correspondencia académica suficiente.

La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# CONFIGURACIÓN COMPLETA
# ============================================================

def obtener_configuracion():

    return {

        "carrera":
            NOMBRE_CARRERA,

        "programa":
            "2 AÑOS",

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