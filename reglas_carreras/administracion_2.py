# ============================================================
# REGLAS PARTICULARES - ADMINISTRACIÓN DE EMPRESAS (2 AÑOS)
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS

Principios:
- evaluación especializada en Administración;
- convalidación por competencias;
- análisis global antes de asignar;
- no repetir cursos del certificado;
- utilizar exclusivamente notas reales;
- nota convalidante máxima 15;
- equivalencias jerarquizadas por afinidad;
- segunda revisión antes de suficiencia;
- optimización global de asignaciones;
- revisión manual asistida;
- decisión final del coordinador académico.
"""

NOMBRE_CARRERA = "Administración de Empresas - 2 años"


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

La carrera de destino es:

ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS
Universidad Privada de Trujillo - UPRIT.

Evalúa integralmente las asignaturas cursadas por el estudiante
y compáralas con las asignaturas de la proforma UPRIT.

NO te limites a comparar palabras.

Debes considerar:

- denominación de las asignaturas;
- área académica;
- finalidad formativa;
- relación disciplinar;
- competencias generales razonablemente inferibles del nombre;
- nivel académico;
- especialidad de origen;
- complementariedad entre asignaturas;
- disponibilidad de otros cursos del certificado.

Considera especialmente las áreas de:

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
- Microeconomía.
- Macroeconomía.
- Marketing.
- Investigación de Mercados.
- Marketing Digital.
- Gestión Comercial.
- Ventas.
- Logística.
- Cadena de Suministro.
- Gestión de Operaciones.
- Gestión de la Producción.
- Gestión de la Calidad.
- Emprendimiento.
- Innovación.
- Gestión de Proyectos.
- Derecho Empresarial.
- Derecho Societario.
- Estadística.
- Matemática.
- Investigación Científica.
- Responsabilidad Social.
- Ética Profesional.
- Transformación Digital.
- Sistemas de Información Empresarial.

El objetivo NO es simplemente encontrar coincidencias individuales.

El objetivo es obtener la MEJOR DISTRIBUCIÓN GLOBAL posible de
las asignaturas del certificado, utilizando cada curso de origen
una sola vez.

No fuerces equivalencias únicamente para disminuir suficiencias.

Pero tampoco declares una suficiencia prematuramente cuando
exista una alternativa académicamente razonable.
"""


# ============================================================
# 3. REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS ACADÉMICAS OBLIGATORIAS:

1. Usa únicamente cursos REALES del certificado y de la proforma.

2. No inventes cursos.

3. No inventes notas.

4. No inventes sílabos.

5. No inventes contenidos específicos que no estén disponibles.

6. Conserva exactamente el nombre ORIGINAL de cada asignatura
   del certificado en el resultado.

7. Conserva exactamente la nota ORIGINAL correspondiente.

8. Un curso del certificado puede utilizarse como máximo UNA VEZ.

9. Un curso UPRIT puede recibir como máximo UNA equivalencia.

10. Una vez utilizado un curso de origen, queda BLOQUEADO para
    cualquier otra asignatura.

11. Analiza TODOS los cursos disponibles antes de confirmar las
    asignaciones.

12. No realices la convalidación únicamente siguiendo el orden
    de aparición de los cursos.

13. Prioriza la solución global sobre la primera coincidencia
    encontrada.

14. Clasifica las relaciones académicas como:

    DIRECTA
    ALTA
    MEDIA
    BAJA
    INCOMPATIBLE

15. Prioriza siempre:

    DIRECTA > ALTA > MEDIA > BAJA > SUFICIENCIA

16. Una coincidencia textual NO constituye por sí sola una
    equivalencia académica.

17. Una diferencia de denominación tampoco significa
    automáticamente que los cursos sean incompatibles.

18. Evalúa el significado académico y el área profesional.

19. Si la equivalencia requiere revisar sílabos, indica:

    REQUIERE VALIDACIÓN ACADÉMICA

20. Una afinidad BAJA solo puede proponerse cuando exista una
    relación académica identificable y defendible.

21. Está prohibido utilizar afinidad BAJA cuando la relación solo
    pueda justificarse inventando contenidos.

22. No sacrifiques una equivalencia DIRECTA o ALTA para producir
    varias equivalencias artificiales.

23. Reserva las asignaturas de origen altamente específicas para
    las asignaturas UPRIT más específicas.

24. Antes de determinar suficiencias realiza obligatoriamente una
    SEGUNDA PASADA.

25. Durante la segunda pasada revisa:

    - cursos UPRIT todavía sin equivalencia;
    - cursos del certificado todavía libres;
    - afinidades altas omitidas;
    - afinidades medias omitidas;
    - afinidades bajas defendibles;
    - posibles intercambios entre asignaciones.

26. Si un intercambio mejora la solución global sin deteriorar
    injustificadamente la calidad académica, reorganiza.

27. La suficiencia constituye el ÚLTIMO recurso.

28. No determines suficiencia durante la primera búsqueda.

29. No fuerces equivalencias solamente para disminuir el número
    de suficiencias.

30. La nota parcial procede exclusivamente del certificado.

31. La nota convalidante se calcula solamente con notas reales.

32. La nota convalidante máxima es 15.

33. Las recomendaciones constituyen apoyo técnico al coordinador.

34. La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 4. EQUIVALENCIAS ORIENTATIVAS JERARQUIZADAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # ========================================================
    # ADMINISTRACIÓN
    # ========================================================

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
            "GESTION ADMINISTRATIVA",
            "FORMACION DE MONITORES DE EMPRESA",
            "ORGANIZACION Y CONSTITUCION DE EMPRESAS",
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
            "FORMACION DE MONITORES DE EMPRESA",
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
            "GESTION DE PROCESOS",
            "PROCESOS ADMINISTRATIVOS",
            "PROCESOS EMPRESARIALES",
        ],
        "BAJA": [
            "CALIDAD TOTAL",
            "GESTION DE LA CALIDAD",
        ],
    },


    # ========================================================
    # CONTABILIDAD
    # ========================================================

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


    # ========================================================
    # ECONOMÍA Y FINANZAS
    # ========================================================

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


    # ========================================================
    # MARKETING Y VENTAS
    # ========================================================

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
            "INTELIGENCIA DE MERCADOS",
        ],
        "MEDIA": [
            "MARKETING E INVESTIGACION DE MERCADOS",
            "ANALISIS COMERCIAL",
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


    # ========================================================
    # TALENTO HUMANO
    # ========================================================

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


    # ========================================================
    # LOGÍSTICA, OPERACIONES Y CALIDAD
    # ========================================================

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


    # ========================================================
    # PROYECTOS, EMPRENDIMIENTO E INNOVACIÓN
    # ========================================================

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


    # ========================================================
    # DERECHO
    # ========================================================

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


    # ========================================================
    # MATEMÁTICA Y ESTADÍSTICA
    # ========================================================

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


    # ========================================================
    # INVESTIGACIÓN
    # ========================================================

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


    # ========================================================
    # TECNOLOGÍA
    # ========================================================

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


    # ========================================================
    # ÉTICA
    # ========================================================

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


    # ========================================================
    # NEGOCIACIÓN
    # ========================================================

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


    # ========================================================
    # COMUNICACIÓN
    # ========================================================

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


    # ========================================================
    # REALIDAD NACIONAL / RESPONSABILIDAD SOCIAL
    # ========================================================

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
# 5. FALSOS POSITIVOS
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
    "Gestión de Proyectos no equivale automáticamente a Metodología de la Investigación.",

    "Formación Práctica en Empresa no equivale automáticamente a Derecho Empresarial.",
    "Seminario de Complementación Práctica no equivale automáticamente a Metodología de la Investigación.",

    "Big Data no equivale automáticamente a Estadística Inferencial.",
    "Machine Learning no equivale automáticamente a Estadística y Probabilidades.",

    "Seguridad e Higiene Industrial no equivale automáticamente a Ética Profesional.",

    "Desarrollo Humano no equivale automáticamente a Realidad Nacional y Derechos Humanos.",

    "Marketing Digital no equivale automáticamente a Transformación Digital.",

    "Contabilidad de Costos no debe utilizarse para Contabilidad Básica si existe una asignatura específica de Contabilidad Básica o Contabilidad General disponible.",

    "Matemática Financiera no debe utilizarse para Matemática Básica si existe una asignatura de Matemática General o Matemática Básica disponible.",

    "Investigación de Mercados no debe utilizarse para Metodología de la Investigación si existe una asignatura específica de investigación disponible.",
]


# ============================================================
# 6. REGLAS DE OPTIMIZACIÓN GLOBAL
# ============================================================

REGLAS_OPTIMIZACION = """
PROCEDIMIENTO OBLIGATORIO DE OPTIMIZACIÓN GLOBAL


FASE 1 - LECTURA COMPLETA

Antes de realizar cualquier equivalencia:

1. Lee todos los cursos UPRIT.
2. Lee todos los cursos del certificado.
3. Identifica todas las notas reales.
4. Identifica cursos de origen altamente específicos.

No confirmes todavía ninguna asignación.


FASE 2 - GENERACIÓN DE CANDIDATOS

Para cada curso UPRIT genera todas las alternativas razonables.

Clasifica cada alternativa:

DIRECTA = 100
ALTA = 85
MEDIA = 65
BAJA = 40
INCOMPATIBLE = 0


FASE 3 - RESERVA DE CURSOS ESPECÍFICOS

Reserva prioritariamente:

- Matemática Financiera para Matemática Financiera.
- Contabilidad de Costos para Contabilidad de Costos.
- Contabilidad Financiera para Contabilidad Financiera.
- Investigación de Mercados para Investigación de Mercados.
- Gestión del Talento Humano para Gestión del Talento Humano.
- Planeamiento Estratégico para Planeamiento Estratégico.
- Gestión de Proyectos para Gestión de Proyectos.
- Estadística Inferencial para Estadística Inferencial.
- Derecho Empresarial para Derecho Empresarial.
- Gestión de la Calidad para Gestión de la Calidad.

No utilices innecesariamente un curso específico para cubrir un
curso genérico.


FASE 4 - ASIGNACIONES FUERTES

Resuelve primero:

1. DIRECTAS.
2. ALTAS.
3. MEDIAS.

No declares todavía suficiencias.


FASE 5 - CONTROL DE DUPLICIDAD

Comprueba que:

- ningún curso de origen esté repetido;
- ningún curso UPRIT tenga dos equivalencias;
- la nota corresponda exactamente al curso seleccionado.


FASE 6 - SEGUNDA PASADA

Obtén:

A. cursos UPRIT sin equivalencia;
B. cursos de origen todavía libres.

Vuelve a comparar únicamente esos cursos.

Busca:

- equivalencias directas omitidas;
- afinidades altas;
- afinidades medias;
- afinidades bajas defendibles;
- posibilidades de intercambio.


FASE 7 - INTERCAMBIOS

Ejemplo:

UPRIT A -> CURSO X = MEDIA
UPRIT B -> VACÍO

pero:

UPRIT A -> CURSO Y = MEDIA
UPRIT B -> CURSO X = ALTA

y CURSO Y está disponible.

Entonces reorganiza:

UPRIT A -> CURSO Y
UPRIT B -> CURSO X

porque mejora la solución global.


FASE 8 - AFINIDAD BAJA

Solo puede proponerse una afinidad BAJA cuando:

- exista relación disciplinar;
- exista relación profesional;
- sea académicamente defendible;
- el curso de origen esté libre;
- no exista una alternativa mejor;
- no dependa únicamente de palabras similares.

Toda afinidad BAJA debe marcarse:

REQUIERE VALIDACIÓN ACADÉMICA


FASE 9 - SUFICIENCIA

Únicamente después de agotar:

DIRECTA
ALTA
MEDIA
BAJA DEFENDIBLE
INTERCAMBIOS
SEGUNDA PASADA

puede declararse:

CANDIDATO A EXAMEN DE SUFICIENCIA


FASE 10 - AUDITORÍA FINAL

Antes de devolver resultados revisa:

- duplicados;
- nombres modificados;
- notas incorrectas;
- falsos positivos;
- cursos específicos mal utilizados;
- cursos de origen libres;
- suficiencias evitables;
- intercambios todavía posibles.

Solo después presenta el resultado.
"""


# ============================================================
# 7. REGLAS DEL SISTEMA
# ============================================================

REGLAS = {

    # Reglas existentes
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Afinidades
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

    # Optimización
    "analisis_global_antes_de_asignar": True,
    "optimizar_asignaciones": True,
    "reservar_cursos_especificos": True,
    "prohibir_reutilizacion": True,
    "segunda_pasada_obligatoria": True,
    "revisar_antes_de_suficiencia": True,
    "permitir_intercambio_asignaciones": True,
    "maximizar_equivalencias_defendibles": True,

    # Seguridad
    "permitir_inventar_cursos": False,
    "permitir_inventar_notas": False,
    "permitir_inventar_silabos": False,
    "permitir_inventar_contenidos": False,

    "conservar_nombre_original": True,
    "conservar_nota_original": True,

    "validar_falsos_positivos": True,

    # Suficiencias
    "suficiencia_como_ultimo_recurso": True,
    "reevaluar_faltantes_antes_suficiencia": True,

    # Semáforo institucional
    "umbral_caso_especial": 5,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # Revisión manual asistida
    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,

    # Caso especial
    "generar_caso_especial": False,
    "reevaluar_caso_especial_con_ia": False,

    # Lectura de proforma
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # Carrera
    "nombre_especialidad": "ADMINISTRACIÓN DE EMPRESAS",
    "programa": "2 AÑOS",

    # Componentes
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

def normalizar_nombre_curso(nombre):
    """
    Normalización básica para búsquedas internas.

    IMPORTANTE:
    Esta función no modifica el nombre que debe aparecer en el
    resultado final.
    """

    if nombre is None:
        return ""

    return str(nombre).strip().upper()


def obtener_nivel_afinidad(curso_destino, curso_origen):
    """
    Busca una equivalencia explícita registrada.

    Retorna:
        ("DIRECTA", 100)
        ("ALTA", 85)
        ("MEDIA", 65)
        ("BAJA", 40)

    Si no está registrada:
        (None, None)

    La ausencia en la tabla NO significa automáticamente que
    exista incompatibilidad.
    """

    destino = normalizar_nombre_curso(curso_destino)
    origen = normalizar_nombre_curso(curso_origen)

    if not destino or not origen:
        return None, None

    equivalencias = EQUIVALENCIAS_ORIENTATIVAS.get(destino)

    if not equivalencias:
        return None, None

    for nivel in ("DIRECTA", "ALTA", "MEDIA", "BAJA"):

        candidatos = equivalencias.get(nivel, [])

        candidatos_normalizados = [
            normalizar_nombre_curso(curso)
            for curso in candidatos
        ]

        if origen in candidatos_normalizados:
            return nivel, NIVELES_AFINIDAD[nivel]

    return None, None


def obtener_equivalencias_curso(curso_destino):
    """
    Devuelve todas las equivalencias orientativas registradas
    para un curso UPRIT.
    """

    destino = normalizar_nombre_curso(curso_destino)

    if not destino:
        return {}

    return EQUIVALENCIAS_ORIENTATIVAS.get(destino, {})


def obtener_cursos_reservables():
    """
    Devuelve cursos altamente específicos que deberían
    reservarse para destinos igualmente específicos.
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


# ============================================================
# 9. INSTRUCCIONES DEL ESPECIALISTA
# ============================================================

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
CARRERA DE DESTINO
============================================================

ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS


============================================================
OBJETIVO PRINCIPAL
============================================================

Obtén la mejor distribución GLOBAL académicamente defendible de
las asignaturas disponibles.

NO evalúes cada curso UPRIT de forma completamente independiente.

NO determines suficiencias durante la primera pasada.


============================================================
ORDEN OBLIGATORIO
============================================================

1. Coincidencia exacta.
2. Equivalencia DIRECTA.
3. Afinidad ALTA.
4. Afinidad MEDIA.
5. Afinidad BAJA académicamente defendible.
6. Reorganización.
7. Segunda pasada.
8. Examen de suficiencia.


============================================================
REGLA DE NO REPETICIÓN
============================================================

Cada asignatura del certificado puede utilizarse UNA SOLA VEZ.

Una asignatura utilizada queda inmediatamente bloqueada.

Antes de entregar el resultado realiza una auditoría específica
para comprobar que ninguna asignatura de origen aparece en dos
equivalencias.


============================================================
REGLA DE RESERVA
============================================================

No consumas innecesariamente una asignatura altamente específica
para cubrir una asignatura genérica.

Ejemplo:

Si existen:

MATEMÁTICA
MATEMÁTICA FINANCIERA

debes preferir:

MATEMÁTICA -> MATEMÁTICA BÁSICA
MATEMÁTICA FINANCIERA -> MATEMÁTICA FINANCIERA

y no:

MATEMÁTICA FINANCIERA -> MATEMÁTICA BÁSICA

dejando Matemática Financiera sin una alternativa apropiada.


============================================================
SEGUNDA PASADA OBLIGATORIA
============================================================

Antes de recomendar suficiencia:

1. Lista internamente las asignaturas UPRIT todavía vacías.
2. Lista internamente los cursos de origen todavía disponibles.
3. Compáralos nuevamente.
4. Busca afinidades altas omitidas.
5. Busca afinidades medias omitidas.
6. Evalúa afinidades bajas defendibles.
7. Revisa asignaciones anteriores.
8. Realiza intercambios cuando mejoren la solución global.


============================================================
AFINIDAD BAJA
============================================================

Una afinidad BAJA no significa automáticamente que el curso sea
convalidable.

Debe existir una relación académica real y defendible.

Cuando sea utilizada debe identificarse como:

REQUIERE VALIDACIÓN ACADÉMICA

No inventes contenidos para justificarla.


============================================================
SUFICIENCIA
============================================================

La suficiencia es el ÚLTIMO recurso.

Solo procede después de agotar:

DIRECTA
-> ALTA
-> MEDIA
-> BAJA DEFENDIBLE
-> INTERCAMBIO
-> SEGUNDA PASADA


============================================================
CONTROL FINAL
============================================================

Antes de devolver el resultado verifica:

1. Ningún curso de origen está repetido.
2. Ninguna nota fue inventada.
3. Cada nota corresponde al curso correcto.
4. Los nombres originales fueron conservados.
5. No existen falsos positivos.
6. No existe un curso libre que razonablemente pueda evitar una
   suficiencia.
7. No existe una redistribución global mejor.
8. Los cursos específicos fueron reservados correctamente.
9. Las afinidades bajas están identificadas.
10. Las equivalencias dudosas indican validación académica.

No inventes cursos.
No inventes notas.
No inventes sílabos.
No inventes contenidos.

La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 10. CONFIGURACIÓN PÚBLICA
# ============================================================

def obtener_configuracion():
    """
    Retorna la configuración académica completa para:

    ADMINISTRACIÓN DE EMPRESAS - 2 AÑOS
    """

    return {
        "carrera": NOMBRE_CARRERA,
        "programa": "2 AÑOS",

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