# ============================================================
# REGLAS PARTICULARES - ADMINISTRACIÓN DE EMPRESAS (2.5 AÑOS)
# Universidad Privada de Trujillo - UPRIT
# ============================================================
#
# OBJETIVO:
# Configuración académica especializada para la evaluación de
# convalidaciones de Administración de Empresas - 2.5 años.
#
# PRINCIPIOS:
# - evaluación por competencias;
# - análisis global antes de asignar;
# - no repetir cursos del certificado;
# - utilizar notas reales;
# - priorizar equivalencias directas;
# - admitir afinidades académicas defendibles;
# - segunda revisión antes de suficiencia;
# - no inventar cursos, notas, sílabos ni contenidos;
# - decisión final del coordinador académico.
# ============================================================


NOMBRE_CARRERA = "Administración de Empresas - 2.5 años"


# ============================================================
# 1. NIVELES DE AFINIDAD
# ============================================================

NIVELES_AFINIDAD = {
    "DIRECTA": 100,
    "ALTA": 85,
    "MEDIA": 65,
    "BAJA": 40,
    "INCOMPATIBLE": 0,
}


# ============================================================
# 2. PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
ADMINISTRACIÓN DE EMPRESAS y en procesos de convalidación
académica por competencias.

Tu función es analizar integralmente las asignaturas cursadas por
el estudiante y compararlas con las asignaturas de la carrera
ADMINISTRACIÓN DE EMPRESAS - 2.5 AÑOS de la Universidad Privada
de Trujillo (UPRIT).

La evaluación NO debe limitarse a comparar palabras.

Debes analizar:

- denominación de las asignaturas;
- área académica;
- finalidad formativa;
- competencias previsibles a partir de la denominación disponible;
- nivel académico;
- relación disciplinar;
- especialidad de origen;
- posibles equivalencias académicamente defendibles.

Considera especialmente las siguientes áreas:

- Administración.
- Gestión empresarial.
- Planeamiento estratégico.
- Organización y métodos.
- Procesos administrativos.
- Gestión del talento humano.
- Recursos humanos.
- Comportamiento organizacional.
- Liderazgo.
- Contabilidad.
- Costos.
- Finanzas.
- Matemática financiera.
- Economía.
- Marketing.
- Investigación de mercados.
- Gestión comercial.
- Logística.
- Cadena de suministro.
- Operaciones.
- Calidad.
- Emprendimiento.
- Innovación.
- Gestión de proyectos.
- Derecho empresarial.
- Estadística.
- Matemática.
- Investigación científica.
- Responsabilidad social.
- Ética profesional.
- Sistemas de información.
- Transformación digital.

El objetivo es encontrar la MEJOR DISTRIBUCIÓN GLOBAL de las
asignaturas disponibles.

No debes realizar la convalidación simplemente siguiendo el orden
en el que aparecen los cursos.

No fuerces equivalencias únicamente para reducir exámenes de
suficiencia.

Sin embargo, tampoco declares una suficiencia prematuramente
cuando exista una alternativa académicamente razonable.
"""


# ============================================================
# 3. REGLAS ACADÉMICAS GENERALES
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS ACADÉMICAS OBLIGATORIAS

1. Utiliza únicamente cursos REALES presentes en el certificado
   y en la proforma UPRIT.

2. No inventes asignaturas.

3. No inventes notas.

4. No inventes sílabos.

5. No atribuyas contenidos específicos que no se encuentren
   disponibles.

6. Conserva siempre el nombre ORIGINAL del curso del certificado
   en el resultado final.

7. Conserva siempre la nota ORIGINAL del certificado.

8. Un curso del certificado puede utilizarse como máximo UNA VEZ.

9. Un curso UPRIT puede recibir como máximo UNA equivalencia.

10. Una vez utilizado un curso de origen, queda BLOQUEADO para
    cualquier otra asignatura UPRIT.

11. Analiza TODOS los cursos disponibles antes de confirmar las
    asignaciones.

12. No trabajes exclusivamente curso por curso de manera aislada.

13. Prioriza la calidad de la distribución global.

14. Prioriza las equivalencias en este orden:

    DIRECTA
    ALTA
    MEDIA
    BAJA
    SUFICIENCIA

15. Una coincidencia textual NO constituye por sí sola una
    equivalencia académica.

16. Una diferencia de nombre tampoco implica automáticamente que
    dos asignaturas sean incompatibles.

17. Evalúa el significado académico y el área profesional.

18. Cuando exista una alternativa académicamente razonable pero
    no completamente segura, clasifícala como:

    REQUIERE VALIDACIÓN ACADÉMICA

19. La afinidad BAJA solamente puede utilizarse cuando exista una
    relación académica identificable y defendible.

20. Está prohibido utilizar afinidad BAJA cuando la relación solo
    pueda justificarse inventando contenidos.

21. No sacrifiques una equivalencia DIRECTA o ALTA para producir
    varias equivalencias débiles o artificiales.

22. Reserva los cursos altamente específicos para las asignaturas
    UPRIT altamente específicas.

23. Antes de determinar suficiencias realiza obligatoriamente una
    SEGUNDA PASADA.

24. En la segunda pasada revisa:

    - cursos de origen todavía disponibles;
    - cursos UPRIT todavía sin equivalencia;
    - posibles afinidades altas;
    - posibles afinidades medias;
    - posibles afinidades bajas defendibles;
    - intercambios entre asignaciones anteriores.

25. Si un intercambio mejora la distribución global sin reducir
    injustificadamente la calidad académica, reorganiza las
    asignaciones.

26. Una suficiencia es el ÚLTIMO recurso, no el primero.

27. No generes suficiencia solamente porque el nombre de una
    asignatura sea diferente.

28. No convalides solamente para disminuir artificialmente el
    número de suficiencias.

29. La nota parcial procede exclusivamente del certificado.

30. La nota convalidante se calcula exclusivamente a partir de
    notas reales.

31. La nota convalidante máxima permitida es 15.

32. Las recomendaciones constituyen apoyo técnico al coordinador
    académico y no una aprobación automática.

33. La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 4. EQUIVALENCIAS POR NIVEL DE AFINIDAD
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # --------------------------------------------------------
    # ADMINISTRACIÓN
    # --------------------------------------------------------

    "FUNDAMENTOS DE LA ADMINISTRACION": {
        "DIRECTA": [
            "FUNDAMENTOS DE ADMINISTRACION",
            "INTRODUCCION A LA ADMINISTRACION",
            "PRINCIPIOS DE ADMINISTRACION",
        ],
        "ALTA": [
            "ADMINISTRACION GENERAL",
            "TEORIA DE LA ADMINISTRACION",
            "PROCESO ADMINISTRATIVO",
            "PROCESOS ADMINISTRATIVOS",
        ],
        "MEDIA": [
            "GESTION EMPRESARIAL",
            "ADMINISTRACION DE EMPRESAS",
            "GESTION DE EMPRESAS",
            "ORGANIZACION EMPRESARIAL",
        ],
        "BAJA": [
            "FORMACION DE MONITORES DE EMPRESA",
            "ORGANIZACION Y CONSTITUCION DE EMPRESAS",
            "GESTION ADMINISTRATIVA",
        ],
    },

    "ADMINISTRACION GENERAL": {
        "DIRECTA": [
            "ADMINISTRACION GENERAL",
            "ADMINISTRACION DE EMPRESAS",
        ],
        "ALTA": [
            "FUNDAMENTOS DE ADMINISTRACION",
            "PROCESO ADMINISTRATIVO",
            "PROCESOS ADMINISTRATIVOS",
            "GESTION EMPRESARIAL",
        ],
        "MEDIA": [
            "GESTION DE EMPRESAS",
            "DIRECCION DE EMPRESAS",
            "GERENCIA EMPRESARIAL",
            "GESTION ADMINISTRATIVA",
        ],
        "BAJA": [
            "ORGANIZACION EMPRESARIAL",
            "ORGANIZACION Y CONSTITUCION DE EMPRESAS",
        ],
    },

    "GESTION EMPRESARIAL": {
        "DIRECTA": [
            "GESTION EMPRESARIAL",
            "GESTION DE EMPRESAS",
        ],
        "ALTA": [
            "ADMINISTRACION DE EMPRESAS",
            "DIRECCION DE EMPRESAS",
            "GERENCIA EMPRESARIAL",
            "GESTION ADMINISTRATIVA",
        ],
        "MEDIA": [
            "ADMINISTRACION GENERAL",
            "PROCESO ADMINISTRATIVO",
            "GESTION DE NEGOCIOS",
            "DIRECCION EMPRESARIAL",
        ],
        "BAJA": [
            "FORMACION DE MONITORES DE EMPRESA",
            "ORGANIZACION Y CONSTITUCION DE EMPRESAS",
        ],
    },

    "PLANEAMIENTO ESTRATEGICO": {
        "DIRECTA": [
            "PLANEAMIENTO ESTRATEGICO",
            "PLANIFICACION ESTRATEGICA",
        ],
        "ALTA": [
            "DIRECCION ESTRATEGICA",
            "GESTION ESTRATEGICA",
            "ADMINISTRACION ESTRATEGICA",
        ],
        "MEDIA": [
            "PLANEAMIENTO EMPRESARIAL",
            "PLANIFICACION EMPRESARIAL",
            "GESTION EMPRESARIAL",
            "DIRECCION EMPRESARIAL",
        ],
        "BAJA": [
            "GESTION DE PROYECTOS",
            "FORMULACION Y EVALUACION DE PROYECTOS",
        ],
    },

    "ORGANIZACION Y METODOS": {
        "DIRECTA": [
            "ORGANIZACION Y METODOS",
            "ORGANIZACION Y METODOS DE TRABAJO",
        ],
        "ALTA": [
            "ORGANIZACION EMPRESARIAL",
            "METODOS DE TRABAJO",
            "MEJORA DE METODOS EN EL TRABAJO",
        ],
        "MEDIA": [
            "PROCESOS ADMINISTRATIVOS",
            "GESTION DE PROCESOS",
            "PROCESOS EMPRESARIALES",
        ],
        "BAJA": [
            "CALIDAD TOTAL",
            "GESTION DE LA CALIDAD",
        ],
    },


    # --------------------------------------------------------
    # CONTABILIDAD
    # --------------------------------------------------------

    "CONTABILIDAD BASICA": {
        "DIRECTA": [
            "CONTABILIDAD BASICA",
            "CONTABILIDAD",
            "CONTABILIDAD GENERAL",
            "FUNDAMENTOS DE CONTABILIDAD",
            "INTRODUCCION A LA CONTABILIDAD",
            "CONTABILIDAD I",
        ],
        "ALTA": [
            "CONTABILIDAD EMPRESARIAL",
            "CONTABILIDAD FINANCIERA I",
        ],
        "MEDIA": [
            "REGISTROS CONTABLES",
            "PROCESOS CONTABLES",
        ],
        "BAJA": [
            "ANALISIS DE ESTADOS FINANCIEROS",
        ],
    },

    "CONTABILIDAD FINANCIERA": {
        "DIRECTA": [
            "CONTABILIDAD FINANCIERA",
            "CONTABILIDAD FINANCIERA I",
            "CONTABILIDAD II",
        ],
        "ALTA": [
            "CONTABILIDAD EMPRESARIAL",
            "ESTADOS FINANCIEROS",
            "ANALISIS DE ESTADOS FINANCIEROS",
        ],
        "MEDIA": [
            "CONTABILIDAD GENERAL",
            "CONTABILIDAD",
        ],
        "BAJA": [
            "FINANZAS EMPRESARIALES",
        ],
    },

    "CONTABILIDAD DE COSTOS": {
        "DIRECTA": [
            "CONTABILIDAD DE COSTOS",
            "CONTABILIDAD DE COSTOS I",
            "COSTOS",
        ],
        "ALTA": [
            "COSTOS Y PRESUPUESTOS",
            "COSTOS EMPRESARIALES",
            "GESTION DE COSTOS",
        ],
        "MEDIA": [
            "PRESUPUESTOS",
            "CONTABILIDAD GERENCIAL",
        ],
        "BAJA": [
            "CONTABILIDAD EMPRESARIAL",
        ],
    },


    # --------------------------------------------------------
    # ECONOMÍA Y FINANZAS
    # --------------------------------------------------------

    "ECONOMIA": {
        "DIRECTA": [
            "ECONOMIA",
            "ECONOMIA GENERAL",
            "FUNDAMENTOS DE ECONOMIA",
            "INTRODUCCION A LA ECONOMIA",
            "PRINCIPIOS DE ECONOMIA",
        ],
        "ALTA": [
            "MICROECONOMIA",
            "MACROECONOMIA",
            "MICROECONOMIA Y MACROECONOMIA",
        ],
        "MEDIA": [
            "ECONOMIA EMPRESARIAL",
            "ENTORNO ECONOMICO",
        ],
        "BAJA": [
            "SOCIEDAD Y ECONOMIA",
            "REALIDAD ECONOMICA",
        ],
    },

    "FINANZAS": {
        "DIRECTA": [
            "FINANZAS",
            "FINANZAS EMPRESARIALES",
            "FINANZAS CORPORATIVAS",
        ],
        "ALTA": [
            "ADMINISTRACION FINANCIERA",
            "GESTION FINANCIERA",
            "DIRECCION FINANCIERA",
        ],
        "MEDIA": [
            "ANALISIS FINANCIERO",
            "GESTION ECONOMICA Y FINANCIERA",
        ],
        "BAJA": [
            "CONTABILIDAD FINANCIERA",
            "PRESUPUESTOS",
        ],
    },

    "MATEMATICA FINANCIERA": {
        "DIRECTA": [
            "MATEMATICA FINANCIERA",
            "MATEMATICAS FINANCIERAS",
            "CALCULO FINANCIERO",
        ],
        "ALTA": [
            "MATEMATICA APLICADA A LAS FINANZAS",
            "MATEMATICA PARA LAS FINANZAS",
        ],
        "MEDIA": [
            "MATEMATICA EMPRESARIAL",
            "MATEMATICA APLICADA",
        ],
        "BAJA": [
            "MATEMATICA GENERAL",
            "MATEMATICA",
        ],
    },


    # --------------------------------------------------------
    # MARKETING Y COMERCIAL
    # --------------------------------------------------------

    "MARKETING": {
        "DIRECTA": [
            "MARKETING",
            "MERCADOTECNIA",
            "FUNDAMENTOS DE MARKETING",
            "MARKETING I",
        ],
        "ALTA": [
            "GESTION DE MARKETING",
            "MARKETING EMPRESARIAL",
            "DIRECCION DE MARKETING",
        ],
        "MEDIA": [
            "MARKETING DIGITAL",
            "GESTION COMERCIAL",
            "COMERCIALIZACION",
        ],
        "BAJA": [
            "VENTAS",
            "GESTION DE VENTAS",
        ],
    },

    "INVESTIGACION DE MERCADOS": {
        "DIRECTA": [
            "INVESTIGACION DE MERCADOS",
            "ESTUDIO DE MERCADO",
            "INVESTIGACION COMERCIAL",
        ],
        "ALTA": [
            "ANALISIS DE MERCADOS",
            "ESTUDIOS DE MERCADO",
        ],
        "MEDIA": [
            "MARKETING E INVESTIGACION DE MERCADOS",
            "INTELIGENCIA DE MERCADOS",
        ],
        "BAJA": [
            "MARKETING",
            "GESTION COMERCIAL",
        ],
    },

    "GESTION COMERCIAL Y VENTAS": {
        "DIRECTA": [
            "GESTION COMERCIAL Y VENTAS",
            "GESTION DE VENTAS",
            "ADMINISTRACION DE VENTAS",
        ],
        "ALTA": [
            "GESTION COMERCIAL",
            "DIRECCION COMERCIAL",
            "TECNICAS DE VENTAS",
        ],
        "MEDIA": [
            "COMERCIALIZACION",
            "MARKETING Y VENTAS",
        ],
        "BAJA": [
            "MARKETING",
            "ATENCION AL CLIENTE",
        ],
    },


    # --------------------------------------------------------
    # TALENTO HUMANO Y ORGANIZACIONES
    # --------------------------------------------------------

    "GESTION DEL TALENTO HUMANO": {
        "DIRECTA": [
            "GESTION DEL TALENTO HUMANO",
            "GESTION DE RECURSOS HUMANOS",
            "RECURSOS HUMANOS",
        ],
        "ALTA": [
            "ADMINISTRACION DE PERSONAL",
            "GESTION DEL CAPITAL HUMANO",
            "ADMINISTRACION DE RECURSOS HUMANOS",
        ],
        "MEDIA": [
            "DESARROLLO DEL TALENTO HUMANO",
            "RELACIONES HUMANAS",
            "GESTION DE PERSONAS",
        ],
        "BAJA": [
            "DESARROLLO HUMANO",
            "LIDERAZGO",
        ],
    },

    "COMPORTAMIENTO ORGANIZACIONAL": {
        "DIRECTA": [
            "COMPORTAMIENTO ORGANIZACIONAL",
            "COMPORTAMIENTO HUMANO EN LAS ORGANIZACIONES",
            "CONDUCTA ORGANIZACIONAL",
            "COMPORTAMIENTO Y CULTURA ORGANIZACIONAL",
        ],
        "ALTA": [
            "CULTURA ORGANIZACIONAL",
            "PSICOLOGIA ORGANIZACIONAL",
            "DESARROLLO ORGANIZACIONAL",
        ],
        "MEDIA": [
            "RELACIONES HUMANAS",
            "GESTION DEL TALENTO HUMANO",
            "RECURSOS HUMANOS",
        ],
        "BAJA": [
            "PSICOLOGIA GENERAL",
            "DESARROLLO HUMANO",
            "LIDERAZGO",
        ],
    },

    "LIDERAZGO": {
        "DIRECTA": [
            "LIDERAZGO",
            "LIDERAZGO EMPRESARIAL",
            "LIDERAZGO ORGANIZACIONAL",
        ],
        "ALTA": [
            "HABILIDADES DIRECTIVAS",
            "DIRECCION Y LIDERAZGO",
            "LIDERAZGO Y TRABAJO EN EQUIPO",
        ],
        "MEDIA": [
            "DESARROLLO PERSONAL Y TALLER DE LIDERAZGO",
            "TRABAJO EN EQUIPO",
            "HABILIDADES GERENCIALES",
        ],
        "BAJA": [
            "DESARROLLO PERSONAL",
            "FORMACION DE MONITORES DE EMPRESA",
        ],
    },


    # --------------------------------------------------------
    # LOGÍSTICA Y OPERACIONES
    # --------------------------------------------------------

    "LOGISTICA": {
        "DIRECTA": [
            "LOGISTICA",
            "LOGISTICA EMPRESARIAL",
            "GESTION LOGISTICA",
            "ADMINISTRACION LOGISTICA",
        ],
        "ALTA": [
            "LOGISTICA Y ABASTECIMIENTO",
            "GESTION DE ABASTECIMIENTO",
            "CADENA DE SUMINISTRO",
            "SUPPLY CHAIN MANAGEMENT",
        ],
        "MEDIA": [
            "GESTION DE ALMACENES",
            "ALMACENES E INVENTARIOS",
            "GESTION DE INVENTARIOS",
        ],
        "BAJA": [
            "GESTION DE OPERACIONES",
            "ADMINISTRACION DE OPERACIONES",
        ],
    },

    "GESTION DE OPERACIONES": {
        "DIRECTA": [
            "GESTION DE OPERACIONES",
            "ADMINISTRACION DE OPERACIONES",
            "DIRECCION DE OPERACIONES",
        ],
        "ALTA": [
            "GESTION DE LA PRODUCCION",
            "PRODUCCION Y OPERACIONES",
            "ADMINISTRACION DE LA PRODUCCION",
        ],
        "MEDIA": [
            "PLANEAMIENTO Y CONTROL DE LA PRODUCCION",
            "GESTION DE PROCESOS",
            "PROCESOS PRODUCTIVOS",
        ],
        "BAJA": [
            "LOGISTICA",
            "MEJORA DE METODOS EN EL TRABAJO",
        ],
    },

    "GESTION DE LA CALIDAD": {
        "DIRECTA": [
            "GESTION DE LA CALIDAD",
            "SISTEMAS DE GESTION DE CALIDAD",
            "ADMINISTRACION DE LA CALIDAD",
        ],
        "ALTA": [
            "CONTROL DE CALIDAD",
            "CALIDAD TOTAL",
            "ASEGURAMIENTO DE LA CALIDAD",
        ],
        "MEDIA": [
            "GESTION INTEGRADA DE LA CALIDAD",
            "MEJORA CONTINUA",
        ],
        "BAJA": [
            "MEJORA DE PROCESOS",
            "MEJORA DE METODOS EN EL TRABAJO",
        ],
    },


    # --------------------------------------------------------
    # PROYECTOS, EMPRENDIMIENTO E INNOVACIÓN
    # --------------------------------------------------------

    "GESTION DE PROYECTOS": {
        "DIRECTA": [
            "GESTION DE PROYECTOS",
            "ADMINISTRACION DE PROYECTOS",
            "DIRECCION DE PROYECTOS",
            "PROJECT MANAGEMENT",
        ],
        "ALTA": [
            "FORMULACION Y EVALUACION DE PROYECTOS",
            "FORMULACION DE PROYECTOS",
            "EVALUACION DE PROYECTOS",
        ],
        "MEDIA": [
            "PROYECTOS EMPRESARIALES",
            "PROYECTO EMPRESARIAL",
            "PROYECTOS DE INVERSION",
        ],
        "BAJA": [
            "EMPRENDIMIENTO",
            "PLAN DE NEGOCIOS",
        ],
    },

    "EMPRENDIMIENTO": {
        "DIRECTA": [
            "EMPRENDIMIENTO",
            "EMPRENDIMIENTO EMPRESARIAL",
            "DESARROLLO EMPRENDEDOR",
        ],
        "ALTA": [
            "CREACION DE EMPRESAS",
            "INICIATIVA EMPRESARIAL",
            "GESTION DE EMPRENDIMIENTOS",
        ],
        "MEDIA": [
            "PLAN DE NEGOCIOS",
            "PROYECTO EMPRESARIAL",
            "ORGANIZACION Y CONSTITUCION DE EMPRESAS",
        ],
        "BAJA": [
            "GESTION EMPRESARIAL",
            "INNOVACION",
        ],
    },

    "GESTION DE LA INNOVACION": {
        "DIRECTA": [
            "GESTION DE LA INNOVACION",
            "INNOVACION EMPRESARIAL",
            "GESTION DE INNOVACION",
        ],
        "ALTA": [
            "INNOVACION",
            "INNOVACION Y EMPRENDIMIENTO",
            "GESTION DE LA TECNOLOGIA E INNOVACION",
        ],
        "MEDIA": [
            "EMPRENDIMIENTO",
            "TRANSFORMACION DIGITAL",
            "INNOVACION DIGITAL",
        ],
        "BAJA": [
            "SOFTWARE Y PROTOTIPADO",
            "PROTOTIPADO",
            "PROYECTOS TECNOLOGICOS",
        ],
    },

    "ELECTIVO I: GESTION DE LA INNOVACION": {
        "DIRECTA": [
            "GESTION DE LA INNOVACION",
            "INNOVACION EMPRESARIAL",
        ],
        "ALTA": [
            "INNOVACION",
            "INNOVACION Y EMPRENDIMIENTO",
            "GESTION DE LA TECNOLOGIA E INNOVACION",
        ],
        "MEDIA": [
            "TRANSFORMACION DIGITAL",
            "EMPRENDIMIENTO",
            "INNOVACION DIGITAL",
        ],
        "BAJA": [
            "PROYECTOS TECNOLOGICOS",
            "SOFTWARE Y PROTOTIPADO",
        ],
    },


    # --------------------------------------------------------
    # DERECHO
    # --------------------------------------------------------

    "DERECHO EMPRESARIAL Y DE SOCIEDADES": {
        "DIRECTA": [
            "DERECHO EMPRESARIAL Y DE SOCIEDADES",
            "DERECHO EMPRESARIAL",
            "DERECHO SOCIETARIO",
        ],
        "ALTA": [
            "DERECHO COMERCIAL",
            "LEGISLACION EMPRESARIAL",
            "LEGISLACION COMERCIAL",
        ],
        "MEDIA": [
            "DERECHO LABORAL Y EMPRESARIAL",
            "LEGISLACION LABORAL",
            "LEGISLACION E INSERCION LABORAL",
        ],
        "BAJA": [
            "DERECHO",
            "LEGISLACION",
            "FORMACION PRACTICA EN EMPRESA",
        ],
    },


    # --------------------------------------------------------
    # MATEMÁTICA Y ESTADÍSTICA
    # --------------------------------------------------------

    "MATEMATICA BASICA": {
        "DIRECTA": [
            "MATEMATICA BASICA",
            "MATEMATICA",
            "MATEMATICA GENERAL",
            "MATEMATICAS BASICAS",
        ],
        "ALTA": [
            "MATEMATICA APLICADA",
            "MATEMATICA I",
            "FUNDAMENTOS DE MATEMATICA",
        ],
        "MEDIA": [
            "LOGICA Y FUNCIONES",
            "ALGEBRA",
            "ALGEBRA Y GEOMETRIA",
        ],
        "BAJA": [
            "MATEMATICA FINANCIERA",
            "CALCULO I",
        ],
    },

    "ESTADISTICA Y PROBABILIDADES": {
        "DIRECTA": [
            "ESTADISTICA Y PROBABILIDADES",
            "PROBABILIDAD Y ESTADISTICA",
            "ESTADISTICA GENERAL",
            "ESTADISTICA",
        ],
        "ALTA": [
            "ESTADISTICA APLICADA",
            "ESTADISTICA DESCRIPTIVA",
            "PROBABILIDADES",
        ],
        "MEDIA": [
            "METODOS ESTADISTICOS",
            "ANALISIS ESTADISTICO",
            "ESTADISTICA EMPRESARIAL",
        ],
        "BAJA": [
            "ANALISIS DE DATOS",
            "BIG DATA Y MACHINE LEARNING",
        ],
    },

    "ESTADISTICA INFERENCIAL": {
        "DIRECTA": [
            "ESTADISTICA INFERENCIAL",
            "INFERENCIA ESTADISTICA",
        ],
        "ALTA": [
            "ESTADISTICA II",
            "ESTADISTICA APLICADA",
            "METODOS ESTADISTICOS",
        ],
        "MEDIA": [
            "ANALISIS ESTADISTICO",
            "ANALISIS DE DATOS",
            "METODOS CUANTITATIVOS",
        ],
        "BAJA": [
            "INTELIGENCIA DE NEGOCIOS",
            "INTELIGENCIA DE NEGOCIOS Y DATAWARE",
            "BIG DATA Y MACHINE LEARNING",
        ],
    },


    # --------------------------------------------------------
    # INVESTIGACIÓN
    # --------------------------------------------------------

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": {
        "DIRECTA": [
            "METODOLOGIA DE LA INVESTIGACION CIENTIFICA",
            "METODOLOGIA DE LA INVESTIGACION",
            "INVESTIGACION CIENTIFICA",
            "METODOS DE INVESTIGACION",
        ],
        "ALTA": [
            "METODOLOGIA DE INVESTIGACION",
            "TALLER DE INVESTIGACION",
            "INVESTIGACION TECNOLOGICA",
        ],
        "MEDIA": [
            "PROYECTO DE INVESTIGACION",
            "SEMINARIO DE INVESTIGACION",
            "TALLER DE INVESTIGACION I",
        ],
        "BAJA": [
            "SEMINARIO DE COMPLEMENTACION PRACTICA",
            "PROYECTO DE INVESTIGACION E INNOVACION TECNOLOGICA",
        ],
    },


    # --------------------------------------------------------
    # TECNOLOGÍA
    # --------------------------------------------------------

    "TECNOLOGIA Y TRANSFORMACION DIGITAL": {
        "DIRECTA": [
            "TECNOLOGIA Y TRANSFORMACION DIGITAL",
            "TRANSFORMACION DIGITAL",
        ],
        "ALTA": [
            "TECNOLOGIAS DIGITALES",
            "TECNOLOGIAS DE INFORMACION",
            "SISTEMAS DE INFORMACION",
            "INNOVACION DIGITAL",
        ],
        "MEDIA": [
            "TECNOLOGIAS DE LA INFORMACION",
            "SISTEMAS DE INFORMACION EMPRESARIAL",
            "COMPETENCIAS DIGITALES",
        ],
        "BAJA": [
            "OFIMATICA",
            "INTRODUCCION A LAS TECNOLOGIAS DE LA INFORMACION",
        ],
    },


    # --------------------------------------------------------
    # ÉTICA Y RESPONSABILIDAD
    # --------------------------------------------------------

    "ETICA Y RESPONSABILIDAD PROFESIONAL": {
        "DIRECTA": [
            "ETICA Y RESPONSABILIDAD PROFESIONAL",
            "ETICA PROFESIONAL",
            "ETICA EMPRESARIAL",
        ],
        "ALTA": [
            "ETICA",
            "DEONTOLOGIA PROFESIONAL",
            "ETICA Y DEONTOLOGIA",
        ],
        "MEDIA": [
            "RESPONSABILIDAD SOCIAL",
            "RESPONSABILIDAD SOCIAL EMPRESARIAL",
            "CIUDADANIA Y ETICA",
        ],
        "BAJA": [
            "SEGURIDAD E HIGIENE INDUSTRIAL",
            "FORMACION Y ORIENTACION LABORAL",
        ],
    },


    # --------------------------------------------------------
    # NEGOCIACIÓN
    # --------------------------------------------------------

    "ELECTIVO II: NEGOCIACION Y ADMINISTRACION DE CONFLICTOS": {
        "DIRECTA": [
            "NEGOCIACION Y ADMINISTRACION DE CONFLICTOS",
            "NEGOCIACION Y MANEJO DE CONFLICTOS",
            "NEGOCIACION",
        ],
        "ALTA": [
            "RESOLUCION DE CONFLICTOS",
            "MANEJO DE CONFLICTOS",
            "NEGOCIACION EMPRESARIAL",
        ],
        "MEDIA": [
            "LIDERAZGO Y TRABAJO EN EQUIPO",
            "HABILIDADES DIRECTIVAS",
            "HABILIDADES GERENCIALES",
        ],
        "BAJA": [
            "DESARROLLO PERSONAL Y TALLER DE LIDERAZGO",
            "RELACIONES HUMANAS",
            "COMUNICACION EFECTIVA",
        ],
    },


    # --------------------------------------------------------
    # COMUNICACIÓN
    # --------------------------------------------------------

    "COMUNICACION": {
        "DIRECTA": [
            "COMUNICACION",
            "LENGUAJE Y COMUNICACION",
            "TECNICAS DE COMUNICACION",
        ],
        "ALTA": [
            "COMUNICACION ORAL Y ESCRITA",
            "COMUNICACION EMPRESARIAL",
            "LENGUAJE",
        ],
        "MEDIA": [
            "REDACCION",
            "EXPRESION ORAL Y ESCRITA",
            "COMUNICACION EFECTIVA",
        ],
        "BAJA": [
            "LENGUAJE I",
            "LENGUAJE II",
        ],
    },


    # --------------------------------------------------------
    # REALIDAD NACIONAL / RESPONSABILIDAD SOCIAL
    # --------------------------------------------------------

    "REALIDAD NACIONAL Y DERECHOS HUMANOS": {
        "DIRECTA": [
            "REALIDAD NACIONAL Y DERECHOS HUMANOS",
            "REALIDAD NACIONAL",
            "REALIDAD E IDENTIDAD NACIONAL",
        ],
        "ALTA": [
            "DERECHOS HUMANOS",
            "REALIDAD SOCIAL",
            "REALIDAD NACIONAL Y REGIONAL",
        ],
        "MEDIA": [
            "SOCIEDAD Y ECONOMIA",
            "CIUDADANIA",
            "DESARROLLO HUMANO",
        ],
        "BAJA": [
            "RESPONSABILIDAD SOCIAL",
            "DESARROLLO PERSONAL",
        ],
    },

    "RESPONSABILIDAD SOCIAL": {
        "DIRECTA": [
            "RESPONSABILIDAD SOCIAL",
            "RESPONSABILIDAD SOCIAL EMPRESARIAL",
        ],
        "ALTA": [
            "RESPONSABILIDAD SOCIAL Y DESARROLLO SOSTENIBLE",
            "GESTION DE RESPONSABILIDAD SOCIAL",
        ],
        "MEDIA": [
            "DESARROLLO SOSTENIBLE",
            "CIUDADANIA Y RESPONSABILIDAD SOCIAL",
        ],
        "BAJA": [
            "DESARROLLO HUMANO",
            "ETICA",
        ],
    },
}


# ============================================================
# 5. FALSOS POSITIVOS / BLOQUEOS
# ============================================================

FALSOS_POSITIVOS = [
    "Administración de medicamentos no equivale a Administración General.",
    "Administración educativa no equivale automáticamente a Gestión Empresarial.",
    "Administración de redes no equivale a Administración General.",
    "Administración de base de datos no equivale a Administración General.",

    "Contabilidad no equivale automáticamente a Finanzas.",
    "Economía no equivale automáticamente a Contabilidad.",
    "Matemática General no equivale automáticamente a Matemática Financiera.",
    "Estadística no equivale automáticamente a Investigación de Mercados.",

    "Psicología General no equivale automáticamente a Comportamiento Organizacional.",
    "Marketing no equivale automáticamente a Investigación de Mercados.",
    "Logística no equivale automáticamente a Gestión de Operaciones.",
    "Derecho General no equivale automáticamente a Derecho Empresarial.",

    "Ofimática no equivale automáticamente a Transformación Digital.",
    "Seguridad Industrial no equivale automáticamente a Gestión de la Calidad.",

    "Educación Física no equivale a Física.",
    "Cultura Física no equivale a Física.",
    "Cultura Física y Deporte no equivale a Física.",
    "Actividad Física no equivale a Física.",
    "Deporte no equivale a Física.",

    "Matemática Financiera no equivale automáticamente a Análisis Matemático.",
    "Informática no equivale automáticamente a Arquitectura del Computador.",

    "Desarrollo Personal no equivale automáticamente a Gestión del Talento Humano.",
    "Liderazgo no equivale automáticamente a Comportamiento Organizacional.",
    "Proyecto de Investigación no equivale automáticamente a Gestión de Proyectos.",

    "Formación Práctica en Empresa no equivale automáticamente a Derecho Empresarial.",
    "Seminario de Complementación Práctica no equivale automáticamente a Metodología de la Investigación.",

    "Big Data no equivale automáticamente a Estadística Inferencial.",
    "Machine Learning no equivale automáticamente a Estadística y Probabilidades.",

    "Seguridad e Higiene Industrial no equivale automáticamente a Ética Profesional.",
]


# ============================================================
# 6. REGLAS DE OPTIMIZACIÓN GLOBAL
# ============================================================

REGLAS_OPTIMIZACION = """

PROCEDIMIENTO OBLIGATORIO DE OPTIMIZACIÓN GLOBAL

FASE 1 - LECTURA

Lee la totalidad de:

A. cursos UPRIT que deben evaluarse;
B. cursos presentes en el certificado;
C. notas reales disponibles.

No realices todavía ninguna asignación definitiva.


FASE 2 - GENERACIÓN DE CANDIDATOS

Para cada curso UPRIT identifica todos los cursos de origen
potencialmente compatibles.

Clasifica cada candidato como:

DIRECTA = 100
ALTA = 85
MEDIA = 65
BAJA = 40
INCOMPATIBLE = 0


FASE 3 - RESERVA DE CURSOS ESPECÍFICOS

Antes de asignar, identifica los cursos de origen altamente
específicos.

Ejemplos:

- Matemática Financiera debe reservarse preferentemente para
  Matemática Financiera.

- Contabilidad de Costos debe reservarse preferentemente para
  Contabilidad de Costos.

- Investigación de Mercados debe reservarse preferentemente para
  Investigación de Mercados.

- Gestión del Talento Humano debe reservarse preferentemente para
  Gestión del Talento Humano.

- Planeamiento Estratégico debe reservarse preferentemente para
  Planeamiento Estratégico.

No consumas un curso altamente específico en una asignatura
genérica cuando exista otro curso de origen razonable para la
asignatura genérica.


FASE 4 - PRIMERA ASIGNACIÓN

Asigna primero:

1. DIRECTAS
2. ALTAS
3. MEDIAS

Las afinidades BAJAS deben quedar inicialmente pendientes.


FASE 5 - CONTROL DE DUPLICIDAD

Verifica que:

- ningún curso de origen aparezca dos veces;
- ningún curso UPRIT tenga dos equivalencias;
- nombre y nota correspondan al mismo curso real.


FASE 6 - SEGUNDA PASADA

Antes de declarar suficiencia:

1. Obtén todos los cursos UPRIT todavía vacíos.
2. Obtén todos los cursos del certificado todavía libres.
3. Vuelve a compararlos.
4. Busca afinidades altas omitidas.
5. Busca afinidades medias omitidas.
6. Evalúa afinidades bajas defendibles.
7. Analiza intercambios con asignaciones existentes.


FASE 7 - INTERCAMBIO

Si existe:

UPRIT A -> ORIGEN X = MEDIA
UPRIT B -> SIN CURSO

pero:

UPRIT A -> ORIGEN Y = MEDIA
UPRIT B -> ORIGEN X = ALTA

entonces reorganiza:

UPRIT A -> ORIGEN Y
UPRIT B -> ORIGEN X

siempre que ORIGEN Y esté libre.

El objetivo es mejorar la solución GLOBAL.


FASE 8 - AFINIDAD BAJA

Una afinidad BAJA puede proponerse solamente cuando:

- exista relación disciplinar;
- exista relación profesional;
- sea académicamente defendible;
- no dependa únicamente de una palabra coincidente;
- no exista una alternativa mejor;
- el curso de origen siga disponible.

Debe marcarse como:

REQUIERE VALIDACIÓN ACADÉMICA


FASE 9 - SUFICIENCIA

Solamente después de completar las fases anteriores se puede
declarar:

CANDIDATO A EXAMEN DE SUFICIENCIA

No declares suficiencia durante la primera búsqueda.


FASE 10 - REVISIÓN FINAL

Realiza una última auditoría:

- cursos repetidos;
- notas inventadas;
- nombres modificados;
- falsos positivos;
- equivalencias débiles innecesarias;
- cursos libres que podrían evitar una suficiencia;
- oportunidades de intercambio.

Solo entonces presenta el resultado.
"""


# ============================================================
# 7. REGLAS DEL SISTEMA
# ============================================================

REGLAS = {

    # --------------------------------------------------------
    # Convalidación
    # --------------------------------------------------------

    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # --------------------------------------------------------
    # Afinidad
    # --------------------------------------------------------

    "usar_niveles_afinidad": True,

    "puntaje_directa": 100,
    "puntaje_alta": 85,
    "puntaje_media": 65,
    "puntaje_baja": 40,
    "puntaje_incompatible": 0,

    "permitir_afinidad_directa": True,
    "permitir_afinidad_alta": True,
    "permitir_afinidad_media": True,
    "permitir_afinidad_baja": True,

    "afinidad_baja_requiere_revision": True,

    # --------------------------------------------------------
    # Optimización global
    # --------------------------------------------------------

    "analisis_global_antes_de_asignar": True,
    "optimizar_asignaciones": True,
    "reservar_cursos_especificos": True,
    "prohibir_reutilizacion": True,
    "segunda_pasada_obligatoria": True,
    "revisar_antes_de_suficiencia": True,
    "permitir_intercambio_asignaciones": True,
    "maximizar_equivalencias_defendibles": True,

    # --------------------------------------------------------
    # Seguridad académica
    # --------------------------------------------------------

    "permitir_inventar_cursos": False,
    "permitir_inventar_notas": False,
    "permitir_inventar_silabos": False,
    "permitir_inventar_contenidos": False,

    "conservar_nombre_original": True,
    "conservar_nota_original": True,

    "validar_falsos_positivos": True,

    # --------------------------------------------------------
    # Suficiencias
    # --------------------------------------------------------

    "suficiencia_como_ultimo_recurso": True,
    "reevaluar_faltantes_antes_suficiencia": True,

    # Semáforo institucional
    "umbral_caso_especial": 5,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # --------------------------------------------------------
    # Flujo de revisión
    # --------------------------------------------------------

    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,

    # No generar caso especial únicamente por cantidad
    "generar_caso_especial": False,
    "reevaluar_caso_especial_con_ia": False,

    # --------------------------------------------------------
    # Lectura de proforma
    # --------------------------------------------------------

    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # --------------------------------------------------------
    # Especialidad
    # --------------------------------------------------------

    "nombre_especialidad": "ADMINISTRACIÓN DE EMPRESAS",
    "programa": "2.5 AÑOS",

    # --------------------------------------------------------
    # Componentes académicos
    # --------------------------------------------------------

    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "reglas_optimizacion": REGLAS_OPTIMIZACION,
    "niveles_afinidad": NIVELES_AFINIDAD,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS,
}


# ============================================================
# 8. FUNCIONES AUXILIARES
# ============================================================

def obtener_nivel_afinidad(curso_destino, curso_origen):
    """
    Busca una equivalencia explícita dentro de la base orientativa.

    Retorna:
        (nivel, puntaje)

    Ejemplo:
        ("ALTA", 85)

    Si no existe coincidencia explícita:
        (None, None)

    IMPORTANTE:
    Que no exista en esta tabla NO significa automáticamente
    que sea incompatible. Puede requerir evaluación académica
    contextual.
    """

    if not curso_destino or not curso_origen:
        return None, None

    destino = str(curso_destino).strip().upper()
    origen = str(curso_origen).strip().upper()

    equivalencias = EQUIVALENCIAS_ORIENTATIVAS.get(destino)

    if not equivalencias:
        return None, None

    for nivel in ("DIRECTA", "ALTA", "MEDIA", "BAJA"):

        cursos = equivalencias.get(nivel, [])

        cursos_normalizados = [
            str(curso).strip().upper()
            for curso in cursos
        ]

        if origen in cursos_normalizados:
            return nivel, NIVELES_AFINIDAD[nivel]

    return None, None


def obtener_equivalencias_curso(curso_destino):
    """
    Devuelve las equivalencias registradas para una asignatura
    UPRIT determinada.
    """

    if not curso_destino:
        return {}

    destino = str(curso_destino).strip().upper()

    return EQUIVALENCIAS_ORIENTATIVAS.get(destino, {})


def obtener_cursos_reservables():
    """
    Cursos altamente específicos que no deberían consumirse
    prematuramente para cubrir asignaturas genéricas.
    """

    return [
        "MATEMATICA FINANCIERA",
        "CONTABILIDAD DE COSTOS",
        "CONTABILIDAD FINANCIERA",
        "INVESTIGACION DE MERCADOS",
        "GESTION DEL TALENTO HUMANO",
        "PLANEAMIENTO ESTRATEGICO",
        "GESTION DE PROYECTOS",
        "GESTION DE LA CALIDAD",
        "ESTADISTICA INFERENCIAL",
        "DERECHO EMPRESARIAL",
        "DERECHO SOCIETARIO",
    ]


def obtener_instrucciones_especialista():

    bloqueos = "\n".join(
        f"- {item}"
        for item in FALSOS_POSITIVOS
    )

    return f"""
{PERFIL_ESPECIALISTA}

{REGLAS_ACADEMICAS}

{REGLAS_OPTIMIZACION}


============================================================
BLOQUEOS Y FALSOS POSITIVOS
============================================================

{bloqueos}


============================================================
INSTRUCCIÓN ESPECIAL PARA ADMINISTRACIÓN DE EMPRESAS
============================================================

La carrera de destino es:

ADMINISTRACIÓN DE EMPRESAS - 2.5 AÑOS


NO determines suficiencias durante la primera pasada.

Primero analiza globalmente todos los cursos.

Debes intentar encontrar la mejor combinación académicamente
defendible utilizando cada curso del certificado una sola vez.

Cuando existan varias alternativas para una misma asignatura,
selecciona aquella que produzca la mejor distribución GLOBAL.

No selecciones necesariamente la primera coincidencia encontrada.


============================================================
ORDEN DE PRIORIDAD
============================================================

1. Coincidencia exacta.
2. Equivalencia DIRECTA.
3. Afinidad ALTA.
4. Afinidad MEDIA.
5. Afinidad BAJA académicamente defendible.
6. Examen de suficiencia.


============================================================
SEGUNDA PASADA OBLIGATORIA
============================================================

Antes de recomendar un examen de suficiencia:

- revisa todos los cursos de origen no utilizados;
- revisa todas las asignaturas UPRIT sin equivalencia;
- busca nuevas combinaciones;
- analiza intercambios;
- comprueba si algún curso específico fue utilizado
  innecesariamente en una asignatura genérica;
- reorganiza cuando la nueva distribución sea académicamente
  superior.


============================================================
AFINIDAD BAJA
============================================================

Cuando exista una alternativa razonable pero no completamente
segura, NO la presentes como equivalencia automática.

Preséntala como:

REQUIERE VALIDACIÓN ACADÉMICA

e indica brevemente la relación académica encontrada.

Una afinidad baja no puede basarse solamente en una palabra
coincidente.


============================================================
SUFICIENCIA
============================================================

Un curso solamente puede recomendarse para suficiencia después
de haber agotado:

DIRECTA -> ALTA -> MEDIA -> BAJA DEFENDIBLE -> REORGANIZACIÓN

La suficiencia constituye el último recurso.


============================================================
CONTROL FINAL
============================================================

Antes de devolver el resultado verifica obligatoriamente:

1. Ningún curso del certificado está repetido.
2. Ninguna nota fue inventada.
3. Los nombres originales fueron conservados.
4. No existe un falso positivo.
5. No quedó un curso libre que pudiera evitar razonablemente una
   suficiencia.
6. No existe una mejor redistribución de cursos.
7. Las afinidades bajas están claramente identificadas.
8. Las recomendaciones dudosas requieren validación académica.

No inventes cursos.
No inventes notas.
No inventes sílabos.
No inventes contenidos.

La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 9. CONFIGURACIÓN PÚBLICA
# ============================================================

def obtener_configuracion():
    """
    Retorna toda la configuración académica correspondiente a
    Administración de Empresas - 2.5 años.
    """

    return {
        "carrera": NOMBRE_CARRERA,
        "programa": "2.5 AÑOS",

        "reglas": REGLAS,

        "niveles_afinidad": NIVELES_AFINIDAD,

        "perfil_especialista": PERFIL_ESPECIALISTA,

        "reglas_academicas": REGLAS_ACADEMICAS,

        "reglas_optimizacion": REGLAS_OPTIMIZACION,

        "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,

        "falsos_positivos": FALSOS_POSITIVOS,

        "cursos_reservables": obtener_cursos_reservables(),

        "instrucciones_especialista": obtener_instrucciones_especialista(),
    }


# ============================================================
# FIN DEL ARCHIVO
# ============================================================