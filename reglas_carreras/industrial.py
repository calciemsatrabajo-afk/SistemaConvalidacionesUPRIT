# ============================================================
# REGLAS PARTICULARES - INGENIERÍA INDUSTRIAL
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a Ingeniería Industrial.

OBJETIVO:
- mantener la lógica general de convalidación por competencias;
- realizar la evaluación semántica como especialista en
  Ingeniería Industrial;
- activar una segunda revisión cuando se supera el umbral
  ordinario de suficiencias;
- recomendar cursos reales del certificado sin repetirlos;
- nunca inventar cursos ni notas.
"""

NOMBRE_CARRERA = "Ingeniería Industrial"


# ============================================================
# PERFIL ACADÉMICO DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
INGENIERÍA INDUSTRIAL y en procesos de convalidación académica
por competencias.

Debes analizar las equivalencias desde la perspectiva curricular
de Ingeniería Industrial.

Considera especialmente estas áreas:

- Matemática, análisis matemático y cálculo.
- Física y química.
- Estadística y probabilidades.
- Investigación de Operaciones.
- Optimización y programación lineal.
- Ingeniería de Métodos.
- Estudio del Trabajo.
- Medición del trabajo.
- Productividad.
- Ergonomía.
- Procesos industriales.
- Procesos de manufactura.
- Ingeniería de procesos.
- Gestión de operaciones.
- Sistemas de producción.
- Planeamiento y control de la producción.
- Logística.
- Gestión de almacenes.
- Inventarios.
- Cadena de suministro.
- Gestión de la calidad.
- Control de calidad.
- Control estadístico de procesos.
- Seguridad y Salud en el Trabajo.
- Seguridad industrial.
- Higiene industrial.
- Gestión del mantenimiento.
- Mantenimiento industrial.
- Diseño y distribución de planta.
- Ingeniería de planta.
- Automatización industrial.
- Simulación.
- Gestión de proyectos.
- Administración.
- Contabilidad.
- Costos industriales.
- Economía.
- Finanzas.
- Talento humano.
- Sistemas de información.
- Gestión ambiental y sostenibilidad.

No te limites a comparar palabras del nombre de los cursos.
Evalúa también el significado académico, finalidad, área,
competencias habituales y relación profesional con Ingeniería
Industrial.

No fuerces equivalencias para reducir el número de suficiencias.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA INGENIERÍA INDUSTRIAL:

1. Usa únicamente cursos REALES presentes en las listas recibidas.
2. No inventes cursos.
3. No inventes notas.
4. No inventes sílabos ni contenidos no proporcionados.
5. Un curso del certificado puede utilizarse como máximo una vez.
6. Un curso UPRIT puede recibir como máximo una equivalencia.
7. Prioriza coincidencias exactas y equivalencias académicamente
   defendibles.
8. Una semejanza de palabras no implica equivalencia.
9. Los créditos distintos pueden generar revisión, pero no son por
   sí solos razón para rechazar una equivalencia.
10. Si la relación académica es razonable pero requiere comprobar
    contenidos, marcar como REQUIERE VALIDACIÓN ACADÉMICA.
11. Las recomendaciones para el coordinador NO son aprobaciones
    automáticas.
12. Toda nota parcial debe proceder exclusivamente del certificado.
13. La nota convalidante se calcula solo con notas parciales reales.
14. La nota convalidante máxima es 15.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {
    "INGENIERIA DE METODOS": [
        "ESTUDIO DEL TRABAJO",
        "ESTUDIO DE METODOS",
        "METODOS Y TIEMPOS",
        "TIEMPOS Y MOVIMIENTOS",
        "ORGANIZACION Y METODOS",
        "INGENIERIA DEL TRABAJO"
    ],

    "INVESTIGACION DE OPERACIONES I": [
        "INVESTIGACION DE OPERACIONES",
        "INVESTIGACION OPERATIVA",
        "PROGRAMACION LINEAL",
        "OPTIMIZACION",
        "METODOS CUANTITATIVOS"
    ],

    "INVESTIGACION DE OPERACIONES II": [
        "INVESTIGACION DE OPERACIONES II",
        "OPTIMIZACION AVANZADA",
        "MODELOS DE REDES",
        "SIMULACION DE SISTEMAS",
        "TEORIA DE COLAS"
    ],

    "GESTION DE OPERACIONES": [
        "ADMINISTRACION DE OPERACIONES",
        "DIRECCION DE OPERACIONES",
        "GESTION DE PRODUCCION",
        "ADMINISTRACION DE LA PRODUCCION",
        "SISTEMAS DE PRODUCCION"
    ],

    "PLANEAMIENTO Y CONTROL DE LA PRODUCCION": [
        "PLANIFICACION Y CONTROL DE LA PRODUCCION",
        "PLANEAMIENTO DE LA PRODUCCION",
        "CONTROL DE PRODUCCION",
        "ADMINISTRACION DE LA PRODUCCION",
        "GESTION DE LA PRODUCCION"
    ],

    "LOGISTICA": [
        "GESTION LOGISTICA",
        "LOGISTICA INTEGRAL",
        "ADMINISTRACION LOGISTICA",
        "CADENA DE SUMINISTRO",
        "SUPPLY CHAIN",
        "ABASTECIMIENTO Y DISTRIBUCION"
    ],

    "GESTION DE LA CALIDAD": [
        "CONTROL DE CALIDAD",
        "CALIDAD TOTAL",
        "ASEGURAMIENTO DE LA CALIDAD",
        "SISTEMAS DE GESTION DE LA CALIDAD",
        "GESTION DE CALIDAD"
    ],

    "SEGURIDAD Y SALUD EN EL TRABAJO": [
        "SEGURIDAD INDUSTRIAL",
        "HIGIENE Y SEGURIDAD INDUSTRIAL",
        "SALUD OCUPACIONAL",
        "PREVENCION DE RIESGOS",
        "GESTION DE RIESGOS LABORALES"
    ],

    "ERGONOMIA": [
        "ERGONOMIA INDUSTRIAL",
        "FACTORES HUMANOS",
        "INGENIERIA HUMANA",
        "ERGONOMIA Y FACTORES HUMANOS"
    ],

    "GESTION DEL MANTENIMIENTO": [
        "MANTENIMIENTO INDUSTRIAL",
        "INGENIERIA DE MANTENIMIENTO",
        "GESTION DE MANTENIMIENTO",
        "MANTENIMIENTO DE PLANTA"
    ],

    "COSTOS INDUSTRIALES": [
        "CONTABILIDAD DE COSTOS",
        "COSTOS",
        "COSTOS DE PRODUCCION",
        "CONTABILIDAD INDUSTRIAL"
    ],

    "DISENO DE PLANTA": [
        "DISTRIBUCION DE PLANTA",
        "INGENIERIA DE PLANTA",
        "LOCALIZACION Y DISTRIBUCION DE PLANTA",
        "DISENO DE INSTALACIONES"
    ],

    "PROCESOS DE MANUFACTURA": [
        "PROCESOS INDUSTRIALES",
        "PROCESOS DE FABRICACION",
        "MANUFACTURA",
        "TECNOLOGIA DE MANUFACTURA"
    ],

    "SIMULACION": [
        "SIMULACION DE SISTEMAS",
        "MODELAMIENTO Y SIMULACION",
        "SIMULACION DE PROCESOS"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [
    "Educación Física, Actividad Física o Deportes no equivalen a Física.",
    "Programación Neurolingüística no equivale a Programación informática.",
    "Redes Sociales no equivale a Redes informáticas.",
    "Cálculo de Costos no equivale a Cálculo matemático ni a Análisis Matemático.",
    "Telecomunicaciones no equivale a Comunicación.",
    "Administración no equivale automáticamente a Ingeniería de Métodos.",
    "Contabilidad no equivale automáticamente a Costos Industriales.",
    "Logística no equivale automáticamente a Investigación de Operaciones.",
    "Seguridad Industrial no equivale automáticamente a Gestión Ambiental.",
    "Dibujo Técnico no equivale automáticamente a Diseño de Planta.",
    "Mantenimiento no equivale automáticamente a Producción.",
]


# ============================================================
# REGLAS QUE LEE CONVALIDACIONES.PY
# ============================================================

REGLAS = {
    # Competencias
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Caso especial
    # En Ingeniería Industrial no se genera un documento de CASO ESPECIAL.
    # Si quedan muchos cursos pendientes, se abre una revisión manual asistida.
    "umbral_caso_especial": 7,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,
    "reevaluar_caso_especial_con_ia": False,

    # Flujo específico de revisión por el coordinador.
    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,
    "generar_caso_especial": False,

    # La detección solo se usará como respaldo si la proforma
    # no trae CICLO/CÓDIGO suficientes para detectar competencia.
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # Datos que utilizará el motor para orientar la evaluación.
    "nombre_especialidad": "INGENIERÍA INDUSTRIAL",
    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS,
}


def obtener_instrucciones_especialista():
    """
    Devuelve el bloque completo que el motor general agrega
    al prompt semántico cuando la carrera seleccionada es
    Ingeniería Industrial.
    """

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
La carrera de destino es INGENIERÍA INDUSTRIAL.
Evalúa cada equivalencia desde la perspectiva profesional y
curricular de Ingeniería Industrial.
"""


def obtener_configuracion():
    """
    Configuración completa disponible para futuras ampliaciones.
    """

    return {
        "carrera": NOMBRE_CARRERA,
        "reglas": REGLAS,
        "perfil_especialista": PERFIL_ESPECIALISTA,
        "reglas_academicas": REGLAS_ACADEMICAS,
        "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
        "falsos_positivos": FALSOS_POSITIVOS,
        "instrucciones_especialista": obtener_instrucciones_especialista(),
    }
