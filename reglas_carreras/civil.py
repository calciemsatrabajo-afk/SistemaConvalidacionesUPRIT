# ============================================================
# REGLAS PARTICULARES - INGENIERÍA CIVIL
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Configuración académica especializada para INGENIERÍA CIVIL.

OBJETIVOS:
- evaluar equivalencias por competencias;
- analizar globalmente el certificado;
- evitar duplicación de cursos;
- priorizar equivalencias directas y de alta afinidad;
- reconocer diferentes denominaciones académicas;
- reservar cursos específicos para destinos específicos;
- reducir suficiencias evitables;
- no forzar equivalencias académicamente incorrectas;
- realizar segunda revisión antes de declarar suficiencia;
- conservar notas y nombres reales;
- mantener nota convalidante máxima de 15.
"""

NOMBRE_CARRERA = "Ingeniería Civil"


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
INGENIERÍA CIVIL y en procesos de convalidación académica por
competencias.

La carrera de destino es INGENIERÍA CIVIL de la Universidad
Privada de Trujillo - UPRIT.

Analiza integralmente TODOS los cursos del certificado antes de
realizar asignaciones definitivas.

NO te limites a comparar palabras.

Evalúa:

- denominación de la asignatura;
- área disciplinar;
- finalidad formativa;
- competencias generales razonablemente identificables;
- nivel matemático o técnico;
- relación con Ingeniería Civil;
- especialidad de origen;
- existencia de otros cursos más apropiados;
- distribución global de las asignaturas.

Considera especialmente:

CIENCIAS BÁSICAS:
- Matemática.
- Álgebra.
- Geometría.
- Trigonometría.
- Cálculo.
- Análisis Matemático.
- Ecuaciones Diferenciales.
- Estadística.
- Probabilidades.
- Física.
- Química.

CIENCIAS DE INGENIERÍA:
- Estática.
- Dinámica.
- Mecánica.
- Mecánica de Fluidos.
- Resistencia de Materiales.
- Mecánica de Materiales.
- Topografía.
- Geología.
- Mecánica de Suelos.
- Geotecnia.
- Hidráulica.
- Hidrología.
- Materiales de Construcción.
- Tecnología del Concreto.

ESTRUCTURAS:
- Análisis Estructural.
- Concreto Armado.
- Estructuras Metálicas.
- Diseño Estructural.

CONSTRUCCIÓN:
- Procesos Constructivos.
- Tecnología de la Construcción.
- Planeamiento de Obras.
- Programación de Obras.
- Costos y Presupuestos.
- Metrados.
- Supervisión de Obras.
- Seguridad en Construcción.

INFRAESTRUCTURA:
- Caminos.
- Carreteras.
- Pavimentos.
- Transportes.
- Abastecimiento de Agua.
- Saneamiento.
- Ingeniería Sanitaria.

GESTIÓN E INVESTIGACIÓN:
- Gestión de Proyectos.
- Administración de Obras.
- Metodología de la Investigación.
- Investigación Científica.
- Ética Profesional.
- Responsabilidad Social.

El objetivo es obtener la MEJOR DISTRIBUCIÓN GLOBAL posible.

No declares suficiencias prematuramente.

No fuerces equivalencias únicamente para disminuir suficiencias.
"""


# ============================================================
# 3. REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS ACADÉMICAS OBLIGATORIAS:

1. Utiliza únicamente cursos REALES del certificado.

2. Utiliza únicamente cursos REALES de la proforma UPRIT.

3. No inventes cursos.

4. No inventes notas.

5. No inventes sílabos.

6. No inventes contenidos específicos no disponibles.

7. Conserva exactamente el nombre original del curso del
   certificado.

8. Conserva exactamente su nota original.

9. Un curso del certificado puede utilizarse máximo UNA VEZ.

10. Un curso UPRIT puede recibir máximo UNA equivalencia.

11. Una asignatura de origen ya utilizada queda BLOQUEADA.

12. Analiza todos los cursos antes de realizar asignaciones
    definitivas.

13. No evalúes las asignaturas únicamente de manera secuencial.

14. Prioriza la solución global.

15. Clasifica las equivalencias:

    DIRECTA
    ALTA
    MEDIA
    BAJA
    INCOMPATIBLE

16. Prioriza:

    DIRECTA > ALTA > MEDIA > BAJA > SUFICIENCIA

17. Una palabra coincidente no demuestra equivalencia.

18. Una denominación diferente tampoco demuestra incompatibilidad.

19. Considera las denominaciones históricas y alternativas
    utilizadas en carreras de Ingeniería Civil.

20. Reserva cursos específicos para destinos específicos.

21. No utilices Cálculo II para Matemática Básica si existe
    Matemática General disponible.

22. No utilices Mecánica de Suelos para Geología si existe
    Geología disponible.

23. No utilices Concreto Armado para Materiales de Construcción
    si existe un curso específico de Materiales.

24. No utilices Hidráulica para Física si existen cursos de
    Física disponibles.

25. No utilices Análisis Estructural para Estática cuando exista
    un curso específico de Estática.

26. Una afinidad BAJA requiere:

    REQUIERE VALIDACIÓN ACADÉMICA

27. Una afinidad baja solo procede cuando exista relación
    disciplinar real.

28. No inventes contenidos para justificar afinidades bajas.

29. Antes de declarar suficiencia realiza una SEGUNDA PASADA.

30. Durante la segunda pasada revisa:

    - cursos UPRIT todavía vacíos;
    - cursos de origen todavía libres;
    - equivalencias omitidas;
    - afinidades altas;
    - afinidades medias;
    - afinidades bajas defendibles;
    - posibles intercambios.

31. Reorganiza las asignaciones cuando ello mejore la solución
    global sin perjudicar equivalencias fuertes.

32. La suficiencia es el ÚLTIMO recurso.

33. La nota parcial procede exclusivamente del certificado.

34. La nota convalidante se calcula con notas parciales reales.

35. La nota convalidante máxima es 15.

36. La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 4. EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # ========================================================
    # MATEMÁTICA
    # ========================================================

    "MATEMATICA BASICA": {
        "DIRECTA": [
            "MATEMATICA BASICA",
            "MATEMATICA",
            "MATEMATICA GENERAL",
            "MATEMATICAS BASICAS",
        ],
        "ALTA": [
            "MATEMATICA I",
            "MATEMATICA APLICADA",
            "FUNDAMENTOS DE MATEMATICA",
        ],
        "MEDIA": [
            "ALGEBRA",
            "ALGEBRA Y GEOMETRIA",
            "LOGICA Y FUNCIONES",
        ],
        "BAJA": [
            "CALCULO I",
            "ANALISIS MATEMATICO I",
        ],
    },

    "ANALISIS MATEMATICO I": {
        "DIRECTA": [
            "ANALISIS MATEMATICO I",
            "CALCULO I",
            "CALCULO DIFERENCIAL",
        ],
        "ALTA": [
            "CALCULO DIFERENCIAL E INTEGRAL",
            "MATEMATICA SUPERIOR I",
        ],
        "MEDIA": [
            "MATEMATICA II",
            "CALCULO",
        ],
        "BAJA": [
            "MATEMATICA APLICADA",
        ],
    },

    "ANALISIS MATEMATICO II": {
        "DIRECTA": [
            "ANALISIS MATEMATICO II",
            "CALCULO II",
            "CALCULO INTEGRAL",
        ],
        "ALTA": [
            "CALCULO MULTIVARIABLE",
            "CALCULO VECTORIAL",
            "MATEMATICA SUPERIOR II",
        ],
        "MEDIA": [
            "MATEMATICA III",
            "CALCULO AVANZADO",
        ],
        "BAJA": [
            "ECUACIONES DIFERENCIALES",
        ],
    },

    "ANALISIS MATEMATICO III": {
        "DIRECTA": [
            "ANALISIS MATEMATICO III",
            "CALCULO III",
        ],
        "ALTA": [
            "ECUACIONES DIFERENCIALES",
            "CALCULO AVANZADO",
            "MATEMATICA SUPERIOR III",
        ],
        "MEDIA": [
            "CALCULO VECTORIAL",
            "METODOS NUMERICOS",
        ],
        "BAJA": [
            "MATEMATICA III",
        ],
    },

    "ECUACIONES DIFERENCIALES": {
        "DIRECTA": [
            "ECUACIONES DIFERENCIALES",
            "ECUACIONES DIFERENCIALES ORDINARIAS",
        ],
        "ALTA": [
            "MATEMATICA SUPERIOR",
            "ANALISIS MATEMATICO III",
        ],
        "MEDIA": [
            "CALCULO III",
            "METODOS MATEMATICOS",
        ],
        "BAJA": [
            "METODOS NUMERICOS",
        ],
    },


    # ========================================================
    # ESTADÍSTICA
    # ========================================================

    "ESTADISTICA Y PROBABILIDADES": {
        "DIRECTA": [
            "ESTADISTICA Y PROBABILIDADES",
            "PROBABILIDAD Y ESTADISTICA",
            "ESTADISTICA GENERAL",
            "ESTADISTICA",
        ],
        "ALTA": [
            "ESTADISTICA APLICADA",
            "PROBABILIDADES",
            "ESTADISTICA DESCRIPTIVA",
        ],
        "MEDIA": [
            "METODOS ESTADISTICOS",
            "ANALISIS ESTADISTICO",
        ],
        "BAJA": [
            "METODOS CUANTITATIVOS",
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
        ],
        "MEDIA": [
            "METODOS ESTADISTICOS",
            "ANALISIS ESTADISTICO",
        ],
        "BAJA": [
            "METODOS CUANTITATIVOS",
        ],
    },


    # ========================================================
    # FÍSICA Y QUÍMICA
    # ========================================================

    "FISICA I": {
        "DIRECTA": [
            "FISICA I",
            "FISICA GENERAL",
            "FISICA",
        ],
        "ALTA": [
            "FISICA MECANICA",
            "MECANICA",
            "FISICA Y QUIMICA",
        ],
        "MEDIA": [
            "MECANICA CLASICA",
            "FUNDAMENTOS DE FISICA",
        ],
        "BAJA": [
            "FISICA APLICADA",
        ],
    },

    "FISICA II": {
        "DIRECTA": [
            "FISICA II",
        ],
        "ALTA": [
            "ELECTRICIDAD Y MAGNETISMO",
            "FISICA ELECTRICA",
            "ELECTROMAGNETISMO",
        ],
        "MEDIA": [
            "FISICA APLICADA",
            "FISICA ELECTRONICA",
        ],
        "BAJA": [
            "CIRCUITOS ELECTRICOS",
        ],
    },

    "QUIMICA": {
        "DIRECTA": [
            "QUIMICA",
            "QUIMICA GENERAL",
        ],
        "ALTA": [
            "QUIMICA APLICADA",
            "QUIMICA PARA INGENIERIA",
        ],
        "MEDIA": [
            "FISICA Y QUIMICA",
            "QUIMICA INDUSTRIAL",
        ],
        "BAJA": [
            "CIENCIA DE LOS MATERIALES",
        ],
    },


    # ========================================================
    # MECÁNICA
    # ========================================================

    "ESTATICA": {
        "DIRECTA": [
            "ESTATICA",
            "MECANICA ESTATICA",
        ],
        "ALTA": [
            "MECANICA PARA INGENIEROS - ESTATICA",
            "MECANICA DE CUERPOS RIGIDOS",
        ],
        "MEDIA": [
            "MECANICA",
            "FISICA MECANICA",
        ],
        "BAJA": [
            "ANALISIS ESTRUCTURAL I",
        ],
    },

    "DINAMICA": {
        "DIRECTA": [
            "DINAMICA",
            "MECANICA DINAMICA",
        ],
        "ALTA": [
            "MECANICA PARA INGENIEROS - DINAMICA",
            "DINAMICA DE CUERPOS RIGIDOS",
        ],
        "MEDIA": [
            "MECANICA",
            "FISICA MECANICA",
        ],
        "BAJA": [
            "MECANICA APLICADA",
        ],
    },

    "RESISTENCIA DE MATERIALES": {
        "DIRECTA": [
            "RESISTENCIA DE MATERIALES",
            "RESISTENCIA DE MATERIALES I",
        ],
        "ALTA": [
            "MECANICA DE MATERIALES",
            "MECANICA DE SOLIDOS",
        ],
        "MEDIA": [
            "RESISTENCIA Y ENSAYO DE MATERIALES",
            "MECANICA APLICADA",
        ],
        "BAJA": [
            "ANALISIS ESTRUCTURAL",
        ],
    },


    # ========================================================
    # TOPOGRAFÍA
    # ========================================================

    "TOPOGRAFIA": {
        "DIRECTA": [
            "TOPOGRAFIA",
            "TOPOGRAFIA I",
        ],
        "ALTA": [
            "TOPOGRAFIA GENERAL",
            "LEVANTAMIENTOS TOPOGRAFICOS",
        ],
        "MEDIA": [
            "GEOMATICA",
            "TOPOGRAFIA APLICADA",
        ],
        "BAJA": [
            "SISTEMAS DE INFORMACION GEOGRAFICA",
        ],
    },

    "TOPOGRAFIA II": {
        "DIRECTA": [
            "TOPOGRAFIA II",
        ],
        "ALTA": [
            "TOPOGRAFIA APLICADA",
            "TOPOGRAFIA AVANZADA",
        ],
        "MEDIA": [
            "GEODESIA",
            "GEOMATICA",
        ],
        "BAJA": [
            "SISTEMAS DE INFORMACION GEOGRAFICA",
        ],
    },


    # ========================================================
    # GEOLOGÍA Y SUELOS
    # ========================================================

    "GEOLOGIA": {
        "DIRECTA": [
            "GEOLOGIA",
            "GEOLOGIA GENERAL",
        ],
        "ALTA": [
            "GEOLOGIA APLICADA",
            "GEOLOGIA PARA INGENIEROS",
            "GEOLOGIA DE INGENIERIA",
        ],
        "MEDIA": [
            "GEOTECNIA",
            "GEOMORFOLOGIA",
        ],
        "BAJA": [
            "MECANICA DE SUELOS",
        ],
    },

    "MECANICA DE SUELOS": {
        "DIRECTA": [
            "MECANICA DE SUELOS",
            "MECANICA DE SUELOS I",
        ],
        "ALTA": [
            "GEOTECNIA",
            "INGENIERIA GEOTECNICA",
        ],
        "MEDIA": [
            "GEOTECNIA I",
            "SUELOS Y CIMENTACIONES",
        ],
        "BAJA": [
            "GEOLOGIA APLICADA",
        ],
    },

    "MECANICA DE SUELOS II": {
        "DIRECTA": [
            "MECANICA DE SUELOS II",
        ],
        "ALTA": [
            "GEOTECNIA II",
            "INGENIERIA DE CIMENTACIONES",
        ],
        "MEDIA": [
            "CIMENTACIONES",
            "DISEÑO DE CIMENTACIONES",
        ],
        "BAJA": [
            "GEOTECNIA",
        ],
    },


    # ========================================================
    # FLUIDOS, HIDRÁULICA E HIDROLOGÍA
    # ========================================================

    "MECANICA DE FLUIDOS": {
        "DIRECTA": [
            "MECANICA DE FLUIDOS",
        ],
        "ALTA": [
            "MECANICA DE LOS FLUIDOS",
            "FLUIDOMECANICA",
        ],
        "MEDIA": [
            "HIDROMECANICA",
            "FUNDAMENTOS DE HIDRAULICA",
        ],
        "BAJA": [
            "HIDRAULICA",
        ],
    },

    "HIDRAULICA": {
        "DIRECTA": [
            "HIDRAULICA",
            "HIDRAULICA I",
        ],
        "ALTA": [
            "HIDRAULICA GENERAL",
            "HIDRAULICA APLICADA",
        ],
        "MEDIA": [
            "MECANICA DE FLUIDOS",
            "HIDROMECANICA",
        ],
        "BAJA": [
            "RECURSOS HIDRICOS",
        ],
    },

    "HIDROLOGIA": {
        "DIRECTA": [
            "HIDROLOGIA",
            "HIDROLOGIA GENERAL",
        ],
        "ALTA": [
            "HIDROLOGIA APLICADA",
            "INGENIERIA HIDROLOGICA",
        ],
        "MEDIA": [
            "RECURSOS HIDRICOS",
            "HIDROLOGIA Y DRENAJE",
        ],
        "BAJA": [
            "HIDRAULICA",
        ],
    },


    # ========================================================
    # MATERIALES Y CONCRETO
    # ========================================================

    "MATERIALES DE CONSTRUCCION": {
        "DIRECTA": [
            "MATERIALES DE CONSTRUCCION",
        ],
        "ALTA": [
            "TECNOLOGIA DE MATERIALES",
            "MATERIALES PARA LA CONSTRUCCION",
            "MATERIALES DE INGENIERIA",
        ],
        "MEDIA": [
            "CIENCIA DE LOS MATERIALES",
            "ENSAYO DE MATERIALES",
        ],
        "BAJA": [
            "TECNOLOGIA DEL CONCRETO",
        ],
    },

    "TECNOLOGIA DEL CONCRETO": {
        "DIRECTA": [
            "TECNOLOGIA DEL CONCRETO",
        ],
        "ALTA": [
            "CONCRETO",
            "CONCRETO Y MATERIALES",
        ],
        "MEDIA": [
            "MATERIALES DE CONSTRUCCION",
            "ENSAYO DE MATERIALES",
        ],
        "BAJA": [
            "CONCRETO ARMADO",
        ],
    },


    # ========================================================
    # ESTRUCTURAS
    # ========================================================

    "ANALISIS ESTRUCTURAL I": {
        "DIRECTA": [
            "ANALISIS ESTRUCTURAL I",
            "ANALISIS ESTRUCTURAL",
        ],
        "ALTA": [
            "TEORIA DE ESTRUCTURAS I",
            "ESTRUCTURAS I",
        ],
        "MEDIA": [
            "ANALISIS DE ESTRUCTURAS",
            "MECANICA ESTRUCTURAL",
        ],
        "BAJA": [
            "RESISTENCIA DE MATERIALES II",
        ],
    },

    "ANALISIS ESTRUCTURAL II": {
        "DIRECTA": [
            "ANALISIS ESTRUCTURAL II",
        ],
        "ALTA": [
            "TEORIA DE ESTRUCTURAS II",
            "ESTRUCTURAS II",
        ],
        "MEDIA": [
            "ANALISIS MATRICIAL DE ESTRUCTURAS",
            "ANALISIS ESTRUCTURAL AVANZADO",
        ],
        "BAJA": [
            "DISEÑO ESTRUCTURAL",
        ],
    },

    "CONCRETO ARMADO": {
        "DIRECTA": [
            "CONCRETO ARMADO",
            "CONCRETO ARMADO I",
        ],
        "ALTA": [
            "DISEÑO EN CONCRETO ARMADO",
            "ESTRUCTURAS DE CONCRETO",
        ],
        "MEDIA": [
            "DISEÑO DE ESTRUCTURAS DE CONCRETO",
            "CONCRETO ESTRUCTURAL",
        ],
        "BAJA": [
            "DISEÑO ESTRUCTURAL",
        ],
    },

    "ESTRUCTURAS METALICAS": {
        "DIRECTA": [
            "ESTRUCTURAS METALICAS",
        ],
        "ALTA": [
            "DISEÑO DE ESTRUCTURAS METALICAS",
            "ESTRUCTURAS DE ACERO",
        ],
        "MEDIA": [
            "DISEÑO EN ACERO",
            "CONSTRUCCIONES METALICAS",
        ],
        "BAJA": [
            "DISEÑO ESTRUCTURAL",
        ],
    },


    # ========================================================
    # CONSTRUCCIÓN
    # ========================================================

    "PROCESOS CONSTRUCTIVOS": {
        "DIRECTA": [
            "PROCESOS CONSTRUCTIVOS",
            "PROCEDIMIENTOS CONSTRUCTIVOS",
        ],
        "ALTA": [
            "TECNOLOGIA DE LA CONSTRUCCION",
            "CONSTRUCCION I",
            "PROCESOS DE CONSTRUCCION",
        ],
        "MEDIA": [
            "OBRAS CIVILES",
            "TECNICAS DE CONSTRUCCION",
        ],
        "BAJA": [
            "FORMACION PRACTICA EN OBRA",
        ],
    },

    "COSTOS Y PRESUPUESTOS": {
        "DIRECTA": [
            "COSTOS Y PRESUPUESTOS",
            "COSTOS Y PRESUPUESTOS DE OBRA",
        ],
        "ALTA": [
            "COSTOS DE CONSTRUCCION",
            "PRESUPUESTOS DE OBRA",
            "COSTOS Y METRADOS",
        ],
        "MEDIA": [
            "METRADOS Y PRESUPUESTOS",
            "GESTION DE COSTOS",
        ],
        "BAJA": [
            "CONTABILIDAD DE COSTOS",
        ],
    },

    "METRADOS": {
        "DIRECTA": [
            "METRADOS",
            "METRADOS EN EDIFICACIONES",
        ],
        "ALTA": [
            "METRADOS Y PRESUPUESTOS",
            "COSTOS Y METRADOS",
        ],
        "MEDIA": [
            "PRESUPUESTOS DE OBRA",
            "COSTOS Y PRESUPUESTOS",
        ],
        "BAJA": [
            "PROCESOS CONSTRUCTIVOS",
        ],
    },

    "PLANEAMIENTO Y PROGRAMACION DE OBRAS": {
        "DIRECTA": [
            "PLANEAMIENTO Y PROGRAMACION DE OBRAS",
            "PLANIFICACION Y PROGRAMACION DE OBRAS",
        ],
        "ALTA": [
            "PROGRAMACION DE OBRAS",
            "PLANEAMIENTO DE OBRAS",
            "GESTION DE OBRAS",
        ],
        "MEDIA": [
            "ADMINISTRACION DE OBRAS",
            "GESTION DE PROYECTOS DE CONSTRUCCION",
        ],
        "BAJA": [
            "GESTION DE PROYECTOS",
        ],
    },


    # ========================================================
    # TRANSPORTES
    # ========================================================

    "CAMINOS": {
        "DIRECTA": [
            "CAMINOS",
            "CAMINOS I",
        ],
        "ALTA": [
            "CARRETERAS",
            "DISEÑO GEOMETRICO DE CARRETERAS",
        ],
        "MEDIA": [
            "INGENIERIA DE CARRETERAS",
            "VIAS DE TRANSPORTE",
        ],
        "BAJA": [
            "INGENIERIA DE TRANSPORTES",
        ],
    },

    "PAVIMENTOS": {
        "DIRECTA": [
            "PAVIMENTOS",
            "PAVIMENTOS I",
        ],
        "ALTA": [
            "DISEÑO DE PAVIMENTOS",
            "INGENIERIA DE PAVIMENTOS",
        ],
        "MEDIA": [
            "CARRETERAS",
            "INFRAESTRUCTURA VIAL",
        ],
        "BAJA": [
            "CAMINOS",
        ],
    },

    "INGENIERIA DE TRANSPORTES": {
        "DIRECTA": [
            "INGENIERIA DE TRANSPORTES",
            "TRANSPORTES",
        ],
        "ALTA": [
            "INGENIERIA DE TRANSITO",
            "TRANSITO Y TRANSPORTE",
        ],
        "MEDIA": [
            "PLANEAMIENTO DEL TRANSPORTE",
            "SISTEMAS DE TRANSPORTE",
        ],
        "BAJA": [
            "VIAS DE TRANSPORTE",
        ],
    },


    # ========================================================
    # SANEAMIENTO
    # ========================================================

    "ABASTECIMIENTO DE AGUA Y ALCANTARILLADO": {
        "DIRECTA": [
            "ABASTECIMIENTO DE AGUA Y ALCANTARILLADO",
        ],
        "ALTA": [
            "AGUA POTABLE Y ALCANTARILLADO",
            "SISTEMAS DE ABASTECIMIENTO DE AGUA",
            "SANEAMIENTO",
        ],
        "MEDIA": [
            "INGENIERIA SANITARIA",
            "SANEAMIENTO BASICO",
        ],
        "BAJA": [
            "HIDRAULICA APLICADA",
        ],
    },


    # ========================================================
    # SEGURIDAD
    # ========================================================

    "SEGURIDAD Y SALUD EN EL TRABAJO": {
        "DIRECTA": [
            "SEGURIDAD Y SALUD EN EL TRABAJO",
            "SEGURIDAD Y SALUD OCUPACIONAL",
        ],
        "ALTA": [
            "SEGURIDAD INDUSTRIAL",
            "SEGURIDAD E HIGIENE INDUSTRIAL",
            "PREVENCION DE RIESGOS LABORALES",
        ],
        "MEDIA": [
            "SEGURIDAD EN OBRAS",
            "SEGURIDAD EN CONSTRUCCION",
        ],
        "BAJA": [
            "GESTION DE RIESGOS",
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
            "SEMINARIO DE TESIS",
            "PROYECTO DE TESIS",
        ],
    },


    # ========================================================
    # GESTIÓN
    # ========================================================

    "GESTION DE PROYECTOS": {
        "DIRECTA": [
            "GESTION DE PROYECTOS",
            "ADMINISTRACION DE PROYECTOS",
            "DIRECCION DE PROYECTOS",
        ],
        "ALTA": [
            "GESTION DE PROYECTOS DE CONSTRUCCION",
            "GERENCIA DE PROYECTOS",
            "PROJECT MANAGEMENT",
        ],
        "MEDIA": [
            "ADMINISTRACION DE OBRAS",
            "GESTION DE OBRAS",
            "FORMULACION Y EVALUACION DE PROYECTOS",
        ],
        "BAJA": [
            "PLANEAMIENTO Y PROGRAMACION DE OBRAS",
        ],
    },


    # ========================================================
    # ÉTICA
    # ========================================================

    "ETICA Y RESPONSABILIDAD PROFESIONAL": {
        "DIRECTA": [
            "ETICA Y RESPONSABILIDAD PROFESIONAL",
            "ETICA PROFESIONAL",
        ],
        "ALTA": [
            "ETICA",
            "DEONTOLOGIA PROFESIONAL",
            "ETICA Y DEONTOLOGIA",
        ],
        "MEDIA": [
            "RESPONSABILIDAD SOCIAL",
            "RESPONSABILIDAD SOCIAL EMPRESARIAL",
        ],
        "BAJA": [
            "FORMACION Y ORIENTACION LABORAL",
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
            "LENGUAJE",
        ],
        "MEDIA": [
            "REDACCION",
            "EXPRESION ORAL Y ESCRITA",
        ],
        "BAJA": [
            "LENGUAJE I",
            "LENGUAJE II",
        ],
    },


    # ========================================================
    # REALIDAD NACIONAL
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
        ],
        "MEDIA": [
            "SOCIEDAD Y ECONOMIA",
            "CIUDADANIA",
            "DESARROLLO HUMANO",
        ],
        "BAJA": [
            "RESPONSABILIDAD SOCIAL",
        ],
    },
}


# ============================================================
# 5. FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [

    # Física
    "Educación Física no equivale a Física.",
    "Cultura Física no equivale a Física.",
    "Cultura Física y Deporte no equivale a Física.",
    "Actividad Física no equivale a Física.",
    "Deporte no equivale a Física.",

    # Matemática
    "Matemática Financiera no equivale automáticamente a Matemática Básica.",
    "Estadística no equivale automáticamente a Análisis Matemático.",
    "Métodos Numéricos no equivale automáticamente a Análisis Matemático.",

    # Construcción / estructuras
    "Materiales de Construcción no equivale automáticamente a Resistencia de Materiales.",
    "Tecnología del Concreto no equivale automáticamente a Concreto Armado.",
    "Concreto Armado no equivale automáticamente a Tecnología del Concreto.",

    "Estática no equivale automáticamente a Análisis Estructural.",
    "Resistencia de Materiales no equivale automáticamente a Análisis Estructural.",

    # Suelos
    "Geología no equivale automáticamente a Mecánica de Suelos.",
    "Mecánica de Suelos no equivale automáticamente a Geología.",

    # Hidráulica
    "Mecánica de Fluidos no equivale automáticamente a Hidrología.",
    "Hidrología no equivale automáticamente a Hidráulica.",
    "Hidráulica no equivale automáticamente a Mecánica de Fluidos.",

    # Transporte
    "Topografía no equivale automáticamente a Caminos.",
    "Caminos no equivale automáticamente a Pavimentos.",
    "Pavimentos no equivale automáticamente a Ingeniería de Transportes.",

    # Gestión
    "Gestión de Proyectos no equivale automáticamente a Planeamiento y Programación de Obras.",
    "Contabilidad de Costos no equivale automáticamente a Costos y Presupuestos de Obra.",

    # Investigación
    "Proyecto de Investigación no equivale automáticamente a Gestión de Proyectos.",
    "Gestión de Proyectos no equivale automáticamente a Metodología de la Investigación.",

    # Seguridad
    "Seguridad Industrial no equivale automáticamente a Gestión de la Calidad.",

    # Tecnología
    "Ofimática no equivale automáticamente a Dibujo Técnico.",
    "Informática no equivale automáticamente a Diseño Asistido por Computadora.",
]


# ============================================================
# 6. CURSOS ESPECÍFICOS QUE DEBEN RESERVARSE
# ============================================================

CURSOS_RESERVABLES = [
    "FISICA I",
    "FISICA II",
    "CALCULO I",
    "CALCULO II",
    "CALCULO III",
    "ANALISIS MATEMATICO I",
    "ANALISIS MATEMATICO II",
    "ANALISIS MATEMATICO III",
    "ECUACIONES DIFERENCIALES",
    "ESTATICA",
    "DINAMICA",
    "RESISTENCIA DE MATERIALES",
    "MECANICA DE FLUIDOS",
    "HIDRAULICA",
    "HIDROLOGIA",
    "TOPOGRAFIA",
    "MECANICA DE SUELOS",
    "GEOLOGIA",
    "TECNOLOGIA DEL CONCRETO",
    "ANALISIS ESTRUCTURAL",
    "CONCRETO ARMADO",
    "ESTRUCTURAS METALICAS",
    "COSTOS Y PRESUPUESTOS",
    "CAMINOS",
    "PAVIMENTOS",
]


# ============================================================
# 7. REGLAS DE OPTIMIZACIÓN GLOBAL
# ============================================================

REGLAS_OPTIMIZACION = """
PROCEDIMIENTO OBLIGATORIO PARA INGENIERÍA CIVIL


FASE 1 - ANALIZAR TODO

Lee TODOS los cursos del certificado y TODOS los cursos UPRIT.

No confirmes equivalencias todavía.


FASE 2 - GENERAR CANDIDATOS

Para cada curso UPRIT identifica todas las asignaturas de origen
potencialmente compatibles.

Clasifica:

DIRECTA = 100
ALTA = 85
MEDIA = 65
BAJA = 40
INCOMPATIBLE = 0


FASE 3 - RESERVAR CURSOS ESPECÍFICOS

Reserva cursos específicos.

Ejemplo:

Si existen:

MATEMÁTICA GENERAL
CÁLCULO I
CÁLCULO II

la distribución preferida es:

MATEMÁTICA GENERAL -> MATEMÁTICA BÁSICA
CÁLCULO I -> ANÁLISIS MATEMÁTICO I
CÁLCULO II -> ANÁLISIS MATEMÁTICO II

No utilices CÁLCULO I para MATEMÁTICA BÁSICA si MATEMÁTICA
GENERAL está disponible.


FASE 4 - ASIGNAR EQUIVALENCIAS FUERTES

Resuelve:

DIRECTAS
ALTAS
MEDIAS

en ese orden.


FASE 5 - CONTROL DE DUPLICIDAD

Comprueba:

- ningún curso de origen repetido;
- ninguna asignatura UPRIT duplicada;
- nota correcta;
- nombre original correcto.


FASE 6 - SEGUNDA PASADA

Antes de cualquier suficiencia:

1. Identifica cursos UPRIT sin equivalencia.
2. Identifica cursos de origen todavía libres.
3. Compara nuevamente.
4. Busca afinidades altas omitidas.
5. Busca afinidades medias omitidas.
6. Evalúa afinidades bajas defendibles.
7. Busca intercambios.


FASE 7 - REORGANIZACIÓN

Si una asignatura específica fue utilizada en un destino menos
específico y puede reemplazarse por otro curso disponible,
reorganiza la distribución.

La prioridad es mejorar la solución GLOBAL.


FASE 8 - AFINIDAD BAJA

Puede proponerse solamente cuando exista relación disciplinar
real.

Toda afinidad baja debe indicar:

REQUIERE VALIDACIÓN ACADÉMICA


FASE 9 - SUFICIENCIA

La suficiencia se determina únicamente después de agotar:

DIRECTA
-> ALTA
-> MEDIA
-> BAJA DEFENDIBLE
-> REORGANIZACIÓN
-> SEGUNDA PASADA


FASE 10 - AUDITORÍA

Antes de finalizar comprueba:

- duplicaciones;
- notas incorrectas;
- cursos inventados;
- falsos positivos;
- cursos libres útiles;
- suficiencias evitables;
- asignaciones específicas desperdiciadas.

Solo entonces presenta el resultado.
"""


# ============================================================
# 8. REGLAS DEL SISTEMA
# ============================================================

REGLAS = {

    # --------------------------------------------------------
    # Competencias
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

    # Umbral institucional
    "umbral_caso_especial": 5,

    # Máximo final
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # --------------------------------------------------------
    # Caso especial
    # --------------------------------------------------------

    # Se conserva por compatibilidad con el motor existente.
    "reevaluar_caso_especial_con_ia": True,

    # Pero la segunda revisión ya no depende exclusivamente
    # de superar el umbral.
    "segunda_revision_independiente_del_umbral": True,

    # Si después de la revisión quedan más de 7 faltantes,
    # NO se convierten artificialmente en convalidados.
    "excedentes_como_pendientes_revision": True,

    # --------------------------------------------------------
    # Proforma
    # --------------------------------------------------------

    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # --------------------------------------------------------
    # Carrera
    # --------------------------------------------------------

    "nombre_especialidad": "INGENIERÍA CIVIL",
    "programa": "REGULAR",

    # --------------------------------------------------------
    # Componentes
    # --------------------------------------------------------

    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "reglas_optimizacion": REGLAS_OPTIMIZACION,
    "niveles_afinidad": NIVELES_AFINIDAD,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS,
    "cursos_reservables": CURSOS_RESERVABLES,
}


# ============================================================
# 9. FUNCIONES AUXILIARES
# ============================================================

def normalizar_nombre_curso(nombre):
    """
    Normalización básica para búsquedas internas.

    No debe utilizarse para modificar el nombre original que
    aparece en el resultado final.
    """

    if nombre is None:
        return ""

    return str(nombre).strip().upper()


def obtener_nivel_afinidad(curso_destino, curso_origen):
    """
    Busca una equivalencia explícita.

    Retorna:

        ("DIRECTA", 100)
        ("ALTA", 85)
        ("MEDIA", 65)
        ("BAJA", 40)

    Si no existe una equivalencia explícita:

        (None, None)

    La ausencia en esta tabla NO implica automáticamente
    incompatibilidad.
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
    Devuelve las equivalencias registradas para un curso UPRIT.
    """

    destino = normalizar_nombre_curso(curso_destino)

    if not destino:
        return {}

    return EQUIVALENCIAS_ORIENTATIVAS.get(destino, {})


def obtener_cursos_reservables():
    """
    Devuelve los cursos específicos que deberían reservarse
    prioritariamente.
    """

    return CURSOS_RESERVABLES.copy()


# ============================================================
# 10. INSTRUCCIONES PARA EL ESPECIALISTA
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
CARRERA
============================================================

INGENIERÍA CIVIL


============================================================
OBJETIVO
============================================================

Encuentra la mejor distribución GLOBAL de los cursos reales del
certificado.

NO realices una asignación simplemente porque sea la primera
coincidencia encontrada.

NO determines suficiencias durante la primera pasada.


============================================================
PRIORIDAD
============================================================

EXACTA
-> DIRECTA
-> ALTA
-> MEDIA
-> BAJA DEFENDIBLE
-> REORGANIZACIÓN
-> SEGUNDA PASADA
-> SUFICIENCIA


============================================================
REGLA FUNDAMENTAL DE INGENIERÍA CIVIL
============================================================

Las asignaturas técnicas específicas deben reservarse
preferentemente para su área específica.

Ejemplos:

FÍSICA no debe consumir un curso de HIDRÁULICA.

ESTÁTICA no debe consumir ANÁLISIS ESTRUCTURAL si existe una
alternativa específica.

MATERIALES DE CONSTRUCCIÓN no debe consumir CONCRETO ARMADO si
existe un curso de materiales disponible.

MATEMÁTICA BÁSICA no debe consumir CÁLCULO II si existe
MATEMÁTICA GENERAL.

TOPOGRAFÍA no debe consumir CAMINOS si existe TOPOGRAFÍA.

GEOLOGÍA no debe consumir MECÁNICA DE SUELOS si existe GEOLOGÍA.


============================================================
SEGUNDA PASADA OBLIGATORIA
============================================================

La segunda revisión se realiza SIEMPRE antes de declarar
suficiencias.

No depende de que existan 5, 6 o 7 faltantes.

Revisa:

- cursos UPRIT vacíos;
- cursos de origen libres;
- afinidades omitidas;
- posibilidades de intercambio;
- cursos específicos mal utilizados.


============================================================
CASO DE MÁS DE 5 FALTANTES
============================================================

Si después de la revisión ordinaria permanecen más de 5
candidatos:

realiza una revisión reforzada de TODOS los candidatos reales.

NO recortes previamente la lista.


============================================================
CASO DE MÁS DE 7 FALTANTES REALES
============================================================

Si después de todas las revisiones permanecen más de 7 cursos
realmente no equivalentes:

NO inventes convalidaciones.

NO conviertas automáticamente los excedentes en convalidados.

Los excedentes deben quedar como:

PENDIENTE DE REVISIÓN ACADÉMICA


============================================================
CONTROL FINAL
============================================================

Verifica obligatoriamente:

1. Ningún curso del certificado está repetido.
2. Ninguna nota fue inventada.
3. Los nombres originales se conservaron.
4. Cada nota pertenece al curso correcto.
5. No existen falsos positivos.
6. No quedó un curso libre útil para evitar razonablemente una
   suficiencia.
7. No existe una redistribución global mejor.
8. Los cursos técnicos específicos fueron reservados.
9. Las afinidades bajas indican validación académica.
10. Los excedentes reales no fueron convalidados artificialmente.

La decisión final corresponde al coordinador académico.
"""


# ============================================================
# 11. CONFIGURACIÓN PÚBLICA
# ============================================================

def obtener_configuracion():
    """
    Retorna la configuración completa de Ingeniería Civil.
    """

    return {
        "carrera": NOMBRE_CARRERA,

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