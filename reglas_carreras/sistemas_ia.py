# ============================================================
# REGLAS PARTICULARES
# INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL

OBJETIVOS:
- mantener la lógica general de convalidación por competencias;
- realizar el análisis como especialista en Ingeniería de Sistemas
  e Inteligencia Artificial;
- reconocer denominaciones equivalentes de informática,
  computación, software, datos e inteligencia artificial;
- evitar falsos positivos entre cursos con nombres parecidos;
- utilizar únicamente cursos y notas reales del certificado;
- permitir revisión manual asistida por el coordinador.
"""


NOMBRE_CARRERA = (
    "Ingeniería de Sistemas e Inteligencia Artificial"
)


# ============================================================
# PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL y en procesos
de convalidación académica por competencias.

Debes evaluar las asignaturas desde una perspectiva curricular,
tecnológica y profesional propia de Ingeniería de Sistemas,
Computación, Software, Ciencias de Datos e Inteligencia Artificial.

Considera especialmente las siguientes áreas:

- Introducción a la Ingeniería de Sistemas.
- Fundamentos de Computación.
- Pensamiento computacional.
- Algoritmos.
- Programación.
- Programación estructurada.
- Programación orientada a objetos.
- Estructuras de Datos.
- Análisis y Diseño de Algoritmos.
- Arquitectura del Computador.
- Organización de Computadores.
- Sistemas Operativos.
- Redes de Computadoras.
- Comunicaciones de Datos.
- Base de Datos.
- Diseño y administración de bases de datos.
- Desarrollo de Software.
- Ingeniería de Software.
- Análisis y Diseño de Sistemas.
- Requerimientos de Software.
- Arquitectura de Software.
- Desarrollo Web.
- Desarrollo Móvil.
- Desarrollo de Aplicaciones.
- Sistemas Distribuidos.
- Computación en la Nube.
- Virtualización.
- Ciberseguridad.
- Seguridad Informática.
- Seguridad de la Información.
- Auditoría de Sistemas.
- Inteligencia Artificial.
- Machine Learning.
- Aprendizaje Automático.
- Deep Learning.
- Redes Neuronales.
- Ciencia de Datos.
- Minería de Datos.
- Big Data.
- Análisis de Datos.
- Visión Artificial.
- Procesamiento de Lenguaje Natural.
- Sistemas Expertos.
- Robótica.
- Internet de las Cosas.
- Automatización.
- Gestión de Proyectos de Tecnología.
- Transformación Digital.
- Investigación de Operaciones.
- Matemática.
- Cálculo.
- Álgebra Lineal.
- Matemática Discreta.
- Lógica.
- Estadística y Probabilidades.
- Métodos Numéricos.
- Investigación Científica.

No debes limitarte a comparar palabras.

Debes evaluar también:

1. significado académico;
2. área tecnológica;
3. finalidad de la asignatura;
4. competencias desarrolladas;
5. nivel de abstracción;
6. herramientas y fundamentos habituales;
7. relación curricular con Ingeniería de Sistemas e IA.

No fuerces equivalencias solamente para disminuir los cursos
pendientes o los exámenes de suficiencia.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA INGENIERÍA DE SISTEMAS E IA:

1. Usa exclusivamente cursos REALES presentes en las listas.

2. No inventes nombres de asignaturas.

3. No inventes notas.

4. No inventes sílabos, contenidos o competencias no disponibles.

5. Un curso del certificado puede utilizarse como máximo una vez.

6. Un curso UPRIT puede recibir como máximo una equivalencia.

7. Prioriza:
   - coincidencia exacta;
   - equivalencia académica directa;
   - denominaciones utilizadas habitualmente en carreras de
     Sistemas, Computación, Software e Informática.

8. Una palabra coincidente no demuestra equivalencia.

9. Si la relación depende de comprobar contenidos, indicar:
   REQUIERE VALIDACIÓN ACADÉMICA.

10. Los créditos diferentes no impiden automáticamente una
    equivalencia, pero pueden justificar revisión de sílabo.

11. Las recomendaciones NO constituyen aprobación automática.

12. La nota parcial siempre debe proceder del certificado.

13. La nota convalidante se calcula únicamente utilizando notas
    parciales reales.

14. La nota convalidante máxima es 15.

15. No utilizar cursos de ofimática básica para convalidar
    automáticamente asignaturas de programación o software.

16. No convertir cursos administrativos que contienen la palabra
    "sistemas" en cursos informáticos.

17. No confundir seguridad industrial con seguridad informática.

18. La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # --------------------------------------------------------
    # PROGRAMACIÓN
    # --------------------------------------------------------

    "FUNDAMENTOS DE PROGRAMACION": [
        "PROGRAMACION",
        "PROGRAMACION I",
        "INTRODUCCION A LA PROGRAMACION",
        "FUNDAMENTOS DE PROGRAMACION",
        "ALGORITMOS Y PROGRAMACION",
        "LOGICA DE PROGRAMACION",
        "PROGRAMACION ESTRUCTURADA"
    ],

    "PROGRAMACION ORIENTADA A OBJETOS": [
        "PROGRAMACION ORIENTADA A OBJETOS",
        "PROGRAMACION II",
        "POO",
        "PROGRAMACION CON OBJETOS",
        "DESARROLLO ORIENTADO A OBJETOS"
    ],

    "ESTRUCTURA DE DATOS": [
        "ESTRUCTURAS DE DATOS",
        "ALGORITMOS Y ESTRUCTURAS DE DATOS",
        "ESTRUCTURA DE DATOS",
        "PROGRAMACION Y ESTRUCTURA DE DATOS"
    ],

    "ALGORITMOS": [
        "ALGORITMOS",
        "DISENO DE ALGORITMOS",
        "ANALISIS DE ALGORITMOS",
        "ALGORITMOS COMPUTACIONALES"
    ],


    # --------------------------------------------------------
    # BASE DE DATOS
    # --------------------------------------------------------

    "BASE DE DATOS I": [
        "BASE DE DATOS",
        "BASES DE DATOS",
        "FUNDAMENTOS DE BASE DE DATOS",
        "SISTEMAS DE BASE DE DATOS",
        "DISENO DE BASE DE DATOS"
    ],

    "BASE DE DATOS II": [
        "BASE DE DATOS II",
        "BASES DE DATOS AVANZADAS",
        "ADMINISTRACION DE BASE DE DATOS",
        "GESTION DE BASE DE DATOS",
        "BASE DE DATOS DISTRIBUIDAS"
    ],


    # --------------------------------------------------------
    # REDES / SISTEMAS OPERATIVOS
    # --------------------------------------------------------

    "REDES Y SISTEMAS OPERATIVOS": [
        "REDES DE COMPUTADORAS",
        "REDES INFORMATICAS",
        "REDES Y COMUNICACIONES",
        "COMUNICACIONES DE DATOS",
        "SISTEMAS OPERATIVOS",
        "REDES Y SISTEMAS OPERATIVOS"
    ],

    "REDES DE COMPUTADORAS": [
        "REDES",
        "REDES INFORMATICAS",
        "REDES DE COMPUTADORES",
        "COMUNICACIONES DE DATOS",
        "REDES Y COMUNICACIONES"
    ],

    "SISTEMAS OPERATIVOS": [
        "SISTEMA OPERATIVO",
        "SISTEMAS OPERATIVOS",
        "ADMINISTRACION DE SISTEMAS OPERATIVOS",
        "SISTEMAS OPERATIVOS I"
    ],


    # --------------------------------------------------------
    # ARQUITECTURA
    # --------------------------------------------------------

    "ARQUITECTURA DEL COMPUTADOR": [
        "ARQUITECTURA DE COMPUTADORAS",
        "ARQUITECTURA DE COMPUTADORES",
        "ORGANIZACION DE COMPUTADORES",
        "ORGANIZACION Y ARQUITECTURA DE COMPUTADORES",
        "HARDWARE DE COMPUTADORAS"
    ],


    # --------------------------------------------------------
    # SOFTWARE
    # --------------------------------------------------------

    "INGENIERIA DE SOFTWARE": [
        "INGENIERIA DEL SOFTWARE",
        "DESARROLLO DE SOFTWARE",
        "PROCESOS DE SOFTWARE",
        "METODOLOGIAS DE DESARROLLO DE SOFTWARE"
    ],

    "ANALISIS Y DISENO DE SISTEMAS": [
        "ANALISIS DE SISTEMAS",
        "DISENO DE SISTEMAS",
        "ANALISIS Y DISENO DE SISTEMAS DE INFORMACION",
        "MODELAMIENTO DE SISTEMAS"
    ],

    "ARQUITECTURA DE SOFTWARE": [
        "DISENO DE SOFTWARE",
        "ARQUITECTURA DEL SOFTWARE",
        "ARQUITECTURA DE APLICACIONES"
    ],

    "DESARROLLO WEB": [
        "PROGRAMACION WEB",
        "DESARROLLO DE APLICACIONES WEB",
        "TECNOLOGIAS WEB",
        "APLICACIONES WEB"
    ],

    "DESARROLLO DE APLICACIONES MOVILES": [
        "PROGRAMACION MOVIL",
        "DESARROLLO MOVIL",
        "APLICACIONES MOVILES",
        "DESARROLLO DE SOFTWARE MOVIL"
    ],


    # --------------------------------------------------------
    # INTELIGENCIA ARTIFICIAL
    # --------------------------------------------------------

    "INTELIGENCIA ARTIFICIAL": [
        "FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL",
        "INTRODUCCION A LA INTELIGENCIA ARTIFICIAL",
        "SISTEMAS INTELIGENTES",
        "INTELIGENCIA COMPUTACIONAL"
    ],

    "APRENDIZAJE AUTOMATICO": [
        "MACHINE LEARNING",
        "APRENDIZAJE DE MAQUINA",
        "APRENDIZAJE AUTOMATICO",
        "APRENDIZAJE COMPUTACIONAL"
    ],

    "REDES NEURONALES": [
        "REDES NEURONALES ARTIFICIALES",
        "DEEP LEARNING",
        "APRENDIZAJE PROFUNDO",
        "MODELOS NEURONALES"
    ],

    "MINERIA DE DATOS": [
        "DATA MINING",
        "DESCUBRIMIENTO DE CONOCIMIENTO",
        "MINERIA DE INFORMACION",
        "ANALISIS Y MINERIA DE DATOS"
    ],

    "CIENCIA DE DATOS": [
        "DATA SCIENCE",
        "ANALISIS DE DATOS",
        "ANALITICA DE DATOS",
        "CIENCIA Y ANALISIS DE DATOS"
    ],

    "BIG DATA": [
        "DATOS MASIVOS",
        "ANALITICA DE BIG DATA",
        "PROCESAMIENTO DE GRANDES VOLUMENES DE DATOS"
    ],

    "VISION ARTIFICIAL": [
        "VISION POR COMPUTADOR",
        "VISION COMPUTACIONAL",
        "PROCESAMIENTO DIGITAL DE IMAGENES"
    ],

    "PROCESAMIENTO DE LENGUAJE NATURAL": [
        "PROCESAMIENTO DEL LENGUAJE NATURAL",
        "NLP",
        "LINGUISTICA COMPUTACIONAL"
    ],


    # --------------------------------------------------------
    # SEGURIDAD
    # --------------------------------------------------------

    "SEGURIDAD INFORMATICA": [
        "CIBERSEGURIDAD",
        "SEGURIDAD DE LA INFORMACION",
        "SEGURIDAD COMPUTACIONAL",
        "SEGURIDAD EN REDES"
    ],

    "AUDITORIA DE SISTEMAS": [
        "AUDITORIA INFORMATICA",
        "AUDITORIA DE TECNOLOGIAS DE INFORMACION",
        "AUDITORIA TI"
    ],


    # --------------------------------------------------------
    # INFRAESTRUCTURA / CLOUD
    # --------------------------------------------------------

    "COMPUTACION EN LA NUBE": [
        "CLOUD COMPUTING",
        "SERVICIOS EN LA NUBE",
        "INFRAESTRUCTURA CLOUD"
    ],

    "SISTEMAS DISTRIBUIDOS": [
        "COMPUTACION DISTRIBUIDA",
        "ARQUITECTURAS DISTRIBUIDAS",
        "SISTEMAS DISTRIBUIDOS"
    ],

    "INTERNET DE LAS COSAS": [
        "IOT",
        "INTERNET OF THINGS",
        "SISTEMAS IOT",
        "DISPOSITIVOS CONECTADOS"
    ],


    # --------------------------------------------------------
    # MATEMÁTICA / ESTADÍSTICA
    # --------------------------------------------------------

    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICAS BASICAS"
    ],

    "LOGICA GENERAL": [
        "LOGICA",
        "LOGICA MATEMATICA",
        "LOGICA COMPUTACIONAL"
    ],

    "MATEMATICA DISCRETA": [
        "MATEMATICAS DISCRETAS",
        "ESTRUCTURAS DISCRETAS",
        "MATEMATICA PARA COMPUTACION"
    ],

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "PROBABILIDAD Y ESTADISTICA",
        "ESTADISTICA GENERAL",
        "ESTADISTICA APLICADA"
    ],

    "ESTADISTICA INFERENCIAL": [
        "INFERENCIA ESTADISTICA",
        "ESTADISTICA II",
        "ESTADISTICA AVANZADA"
    ],


    # --------------------------------------------------------
    # INVESTIGACIÓN DE OPERACIONES
    # --------------------------------------------------------

    "INVESTIGACION DE OPERACIONES I": [
        "INVESTIGACION DE OPERACIONES",
        "PROGRAMACION LINEAL",
        "OPTIMIZACION",
        "METODOS CUANTITATIVOS"
    ],

    "INVESTIGACION DE OPERACIONES II": [
        "INVESTIGACION DE OPERACIONES II",
        "OPTIMIZACION AVANZADA",
        "MODELOS DE REDES",
        "TEORIA DE COLAS",
        "SIMULACION"
    ],


    # --------------------------------------------------------
    # TRANSFORMACIÓN DIGITAL / PROYECTOS
    # --------------------------------------------------------

    "TECNOLOGIA Y TRANSFORMACION DIGITAL": [
        "TRANSFORMACION DIGITAL",
        "TECNOLOGIAS DIGITALES",
        "INNOVACION DIGITAL",
        "TECNOLOGIAS DE INFORMACION"
    ],

    "GESTION DE PROYECTOS PMBOK": [
        "GESTION DE PROYECTOS",
        "DIRECCION DE PROYECTOS",
        "ADMINISTRACION DE PROYECTOS",
        "PROJECT MANAGEMENT",
        "PMBOK"
    ],

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [

    # PROGRAMACIÓN
    "Programación Neurolingüística no equivale a Programación informática.",

    # REDES
    "Redes Sociales no equivale a Redes de Computadoras.",
    "Redes Sociales no equivale a Redes Informáticas.",

    # IA
    "Inteligencia Emocional no equivale a Inteligencia Artificial.",
    "Inteligencia Comercial no equivale a Inteligencia Artificial.",

    # SEGURIDAD
    "Seguridad Industrial no equivale a Seguridad Informática.",
    "Seguridad y Salud en el Trabajo no equivale a Ciberseguridad.",

    # SISTEMAS
    "Sistemas de Gestión de Calidad no equivale a Sistemas Operativos.",
    "Sistemas Administrativos no equivale automáticamente a Sistemas de Información.",

    # ARQUITECTURA
    "Arquitectura de Edificaciones no equivale a Arquitectura del Computador.",
    "Arquitectura Civil no equivale a Arquitectura de Software.",

    # BASE DE DATOS
    "Base de Datos Bibliográfica no equivale automáticamente a Base de Datos informática.",

    # MINERÍA
    "Minería extractiva no equivale a Minería de Datos.",

    # CLOUD
    "Nube como concepto meteorológico no equivale a Computación en la Nube.",

    # DISEÑO
    "Diseño Gráfico no equivale automáticamente a Diseño de Software.",

    # CÁLCULO
    "Cálculo de Costos no equivale a Cálculo matemático.",

    # COMUNICACIÓN
    "Comunicación no equivale automáticamente a Redes y Comunicaciones.",

    # ROBÓTICA
    "Mecánica general no equivale automáticamente a Robótica.",

    # OFIMÁTICA
    "Ofimática no equivale automáticamente a Programación.",
    "Microsoft Office no equivale a Ingeniería de Software."
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
    # REVISIÓN MANUAL ASISTIDA
    # --------------------------------------------------------

    "umbral_caso_especial": 7,

    "maximo_suficiencias": 7,

    "maximo_suficiencias_final": 7,

    # No queremos generar CASO ESPECIAL automáticamente.
    "reevaluar_caso_especial_con_ia": False,

    "revision_manual_asistida": True,

    "autoseleccionar_recomendaciones": True,

    "generar_caso_especial": False,


    # --------------------------------------------------------
    # ESTRUCTURA DE PROFORMA
    # --------------------------------------------------------

    "detectar_competencia_a_la_izquierda_de_asignatura": True,


    # --------------------------------------------------------
    # PERFIL ESPECIALIZADO
    # --------------------------------------------------------

    "nombre_especialidad":
        "INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL",

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
# INSTRUCCIONES DEL ESPECIALISTA
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

La carrera de destino es:

INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL.

Evalúa las equivalencias desde la perspectiva curricular
de Sistemas, Computación, Software, Datos e Inteligencia
Artificial.

No confundas cursos que comparten palabras como:

- sistemas;
- redes;
- seguridad;
- inteligencia;
- arquitectura;
- programación;
- minería;
- diseño.

Estas palabras pueden tener significados completamente distintos
dependiendo del área académica.

No inventes cursos.

No inventes notas.

No reutilices una misma asignatura del certificado.

Cuando exista una relación académica razonable pero no completamente
segura, preséntala como recomendación para revisión del coordinador.

Cuando la relación no sea académicamente defendible, no la propongas.
"""


# ============================================================
# CONFIGURACIÓN COMPLETA
# ============================================================

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