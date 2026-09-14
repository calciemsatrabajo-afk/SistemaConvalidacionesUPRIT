# ============================================================
# REGLAS PARTICULARES
# EDUCACIÓN INICIAL - 1 AÑO
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

EDUCACIÓN INICIAL - 1 AÑO

El formato institucional de Educación trabaja con tres bloques:
1. Convalidación por competencias.
2. Asignaturas no convalidadas.
3. Resumen final con modalidad de convalidación.

Modalidades:
- POR COMPETENCIA
- EXAMEN DE SUFICIENCIA

La revisión final corresponde al coordinador académico.
"""

NOMBRE_CARRERA = "Educación Inicial - 1 año"
PROGRAMA = "1 AÑO"


# ============================================================
# PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
EDUCACIÓN INICIAL, primera infancia, desarrollo infantil,
didáctica y procesos de convalidación académica por competencias.

La carrera de destino es:

EDUCACIÓN INICIAL - 1 AÑO.

Debes evaluar las equivalencias desde una perspectiva
pedagógica, curricular, psicológica y profesional propia de la
formación docente para la primera infancia.

Considera especialmente las siguientes áreas:

- Pedagogía General.
- Didáctica General.
- Didáctica de Educación Inicial.
- Psicología General.
- Psicología del Desarrollo.
- Desarrollo Infantil.
- Desarrollo Humano.
- Desarrollo Cognitivo.
- Desarrollo Socioemocional.
- Psicomotricidad.
- Desarrollo Psicomotor.
- Estimulación Temprana.
- Atención Temprana.
- Juego y Aprendizaje.
- Juego Infantil.
- Literatura Infantil.
- Expresión Oral.
- Comunicación Infantil.
- Lenguaje Infantil.
- Expresión Artística.
- Arte Infantil.
- Expresión Corporal.
- Música y Movimiento.
- Ciencia y Ambiente.
- Descubrimiento del Entorno.
- Matemática para Educación Inicial.
- Pensamiento Lógico Matemático.
- Currículo de Educación Inicial.
- Programación Curricular.
- Evaluación del Desarrollo Infantil.
- Evaluación Educativa.
- Inclusión Educativa.
- Atención a la Diversidad.
- Necesidades Educativas Especiales.
- Familia, Escuela y Comunidad.
- Tutoría y Orientación.
- TIC aplicadas a Educación Inicial.
- Inteligencia Artificial aplicada a la Educación.
- Práctica Preprofesional Pedagógica.
- Investigación Educativa.
- Metodología de la Investigación.
- Ética y Responsabilidad Profesional.

No debes limitarte a comparar palabras.

Debes analizar:

1. finalidad pedagógica;
2. población objetivo;
3. etapa del desarrollo infantil;
4. área curricular;
5. competencias desarrolladas;
6. nivel académico;
7. aplicación profesional;
8. pertinencia con Educación Inicial.

No fuerces equivalencias únicamente para reducir suficiencias.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS PARA EDUCACIÓN INICIAL - 1 AÑO:

1. Utiliza únicamente cursos REALES presentes en el certificado
   y en la proforma.

2. No inventes nombres de asignaturas.

3. No inventes notas.

4. No inventes contenidos de sílabos.

5. Un curso del certificado puede utilizarse como máximo una vez.

6. Un curso UPRIT puede recibir como máximo una equivalencia.

7. Prioriza coincidencias exactas.

8. Luego analiza equivalencias académicamente defendibles por
   finalidad, área, población objetivo y competencia.

9. La semejanza de palabras no demuestra equivalencia.

10. Si una relación requiere comprobar contenidos, marcar:
    REQUIERE VALIDACIÓN ACADÉMICA.

11. Las recomendaciones automáticas son únicamente apoyo al
    coordinador.

12. Una recomendación NO constituye aprobación automática.

13. Toda nota parcial debe proceder exclusivamente del certificado.

14. Si una nota no está disponible, no la inventes.

15. La nota convalidante se calcula únicamente con notas reales.

16. La nota convalidante máxima es 15.

17. No conviertas automáticamente cursos generales en cursos
    específicos de primera infancia.

18. No conviertas automáticamente Educación Física en Psicomotricidad.

19. No conviertas automáticamente Pediatría o Enfermería Pediátrica
    en Desarrollo Infantil o Estimulación Temprana.

20. No conviertas automáticamente Psicología General en Psicología
    del Desarrollo.

21. No conviertas automáticamente Literatura General en Literatura Infantil.

22. No conviertas automáticamente Informática en TIC aplicadas a
    Educación Inicial.

23. No conviertas automáticamente prácticas profesionales no docentes
    en Práctica Preprofesional Pedagógica.

24. La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    # --------------------------------------------------------
    # PEDAGOGÍA / DIDÁCTICA
    # --------------------------------------------------------

    "PEDAGOGIA GENERAL": [
        "PEDAGOGIA",
        "PEDAGOGIA GENERAL",
        "FUNDAMENTOS DE PEDAGOGIA",
        "INTRODUCCION A LA PEDAGOGIA"
    ],

    "DIDACTICA GENERAL": [
        "DIDACTICA",
        "DIDACTICA GENERAL",
        "TEORIA DE LA ENSENANZA",
        "PROCESOS DIDACTICOS"
    ],

    "DIDACTICA DE EDUCACION INICIAL": [
        "DIDACTICA DE EDUCACION INICIAL",
        "DIDACTICA EN EDUCACION INICIAL",
        "METODOLOGIA DE LA EDUCACION INICIAL",
        "DIDACTICA PARA LA PRIMERA INFANCIA"
    ],


    # --------------------------------------------------------
    # PSICOLOGÍA / DESARROLLO
    # --------------------------------------------------------

    "PSICOLOGIA GENERAL": [
        "PSICOLOGIA",
        "PSICOLOGIA GENERAL",
        "INTRODUCCION A LA PSICOLOGIA",
        "FUNDAMENTOS DE PSICOLOGIA"
    ],

    "PSICOLOGIA DEL DESARROLLO": [
        "PSICOLOGIA EVOLUTIVA",
        "DESARROLLO HUMANO",
        "DESARROLLO PSICOLOGICO",
        "PSICOLOGIA DEL NINO",
        "PSICOLOGIA INFANTIL"
    ],

    "DESARROLLO INFANTIL": [
        "DESARROLLO DEL NINO",
        "DESARROLLO INFANTIL",
        "DESARROLLO EN LA PRIMERA INFANCIA",
        "CRECIMIENTO Y DESARROLLO INFANTIL"
    ],

    "DESARROLLO COGNITIVO": [
        "DESARROLLO COGNOSCITIVO",
        "PROCESOS COGNITIVOS EN LA INFANCIA",
        "COGNICION INFANTIL"
    ],

    "DESARROLLO SOCIOEMOCIONAL": [
        "DESARROLLO SOCIOAFECTIVO",
        "DESARROLLO EMOCIONAL",
        "DESARROLLO SOCIAL Y EMOCIONAL",
        "DESARROLLO SOCIOEMOCIONAL INFANTIL"
    ],


    # --------------------------------------------------------
    # PSICOMOTRICIDAD / ESTIMULACIÓN
    # --------------------------------------------------------

    "PSICOMOTRICIDAD": [
        "DESARROLLO PSICOMOTOR",
        "EDUCACION PSICOMOTRIZ",
        "PSICOMOTRICIDAD INFANTIL",
        "PSICOMOTRICIDAD EN LA PRIMERA INFANCIA"
    ],

    "ESTIMULACION TEMPRANA": [
        "ESTIMULACION INFANTIL",
        "ESTIMULACION OPORTUNA",
        "ATENCION TEMPRANA",
        "INTERVENCION TEMPRANA",
        "DESARROLLO Y ESTIMULACION TEMPRANA"
    ],


    # --------------------------------------------------------
    # JUEGO
    # --------------------------------------------------------

    "JUEGO Y APRENDIZAJE": [
        "JUEGO INFANTIL",
        "EL JUEGO EN EDUCACION INICIAL",
        "JUEGO Y DESARROLLO",
        "METODOLOGIA DEL JUEGO",
        "APRENDIZAJE A TRAVES DEL JUEGO"
    ],


    # --------------------------------------------------------
    # COMUNICACIÓN / LENGUAJE
    # --------------------------------------------------------

    "COMUNICACION": [
        "COMUNICACION",
        "LENGUAJE",
        "COMUNICACION ORAL Y ESCRITA",
        "EXPRESION ORAL Y ESCRITA"
    ],

    "LENGUAJE INFANTIL": [
        "DESARROLLO DEL LENGUAJE",
        "LENGUAJE Y COMUNICACION INFANTIL",
        "ADQUISICION DEL LENGUAJE",
        "COMUNICACION EN LA PRIMERA INFANCIA"
    ],

    "LITERATURA INFANTIL": [
        "LITERATURA PARA NINOS",
        "LITERATURA INFANTIL",
        "NARRATIVA INFANTIL",
        "CUENTOS Y LITERATURA INFANTIL"
    ],

    "EXPRESION ORAL": [
        "COMUNICACION ORAL",
        "EXPRESION ORAL",
        "ORALIDAD",
        "LENGUAJE ORAL"
    ],


    # --------------------------------------------------------
    # ARTE / EXPRESIÓN
    # --------------------------------------------------------

    "EXPRESION ARTISTICA": [
        "ARTE INFANTIL",
        "EDUCACION ARTISTICA",
        "EXPRESION CREATIVA",
        "ARTES EN EDUCACION INICIAL"
    ],

    "EXPRESION CORPORAL": [
        "EXPRESION CORPORAL",
        "MOVIMIENTO Y EXPRESION",
        "EXPRESION CORPORAL INFANTIL"
    ],

    "MUSICA Y MOVIMIENTO": [
        "EDUCACION MUSICAL",
        "MUSICA INFANTIL",
        "MUSICA Y EXPRESION CORPORAL",
        "MUSICA Y MOVIMIENTO"
    ],


    # --------------------------------------------------------
    # MATEMÁTICA
    # --------------------------------------------------------

    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICA BASICA"
    ],

    "PENSAMIENTO LOGICO MATEMATICO": [
        "LOGICA MATEMATICA INFANTIL",
        "DESARROLLO DEL PENSAMIENTO MATEMATICO",
        "MATEMATICA EN EDUCACION INICIAL",
        "PENSAMIENTO LOGICO MATEMATICO"
    ],

    "DIDACTICA DE LA MATEMATICA": [
        "DIDACTICA DE MATEMATICA",
        "ENSENANZA DE LA MATEMATICA",
        "METODOLOGIA DE LA ENSENANZA DE MATEMATICA"
    ],


    # --------------------------------------------------------
    # CIENCIA / ENTORNO
    # --------------------------------------------------------

    "CIENCIA Y AMBIENTE": [
        "CIENCIA Y TECNOLOGIA",
        "CIENCIAS NATURALES",
        "CIENCIA, TECNOLOGIA Y AMBIENTE",
        "DESCUBRIMIENTO DEL ENTORNO"
    ],

    "CONOCIMIENTO DEL ENTORNO": [
        "DESCUBRIMIENTO DEL ENTORNO",
        "MEDIO NATURAL Y SOCIAL",
        "ENTORNO NATURAL Y SOCIAL"
    ],


    # --------------------------------------------------------
    # CURRÍCULO / EVALUACIÓN
    # --------------------------------------------------------

    "CURRICULO GENERAL": [
        "CURRICULO",
        "CURRICULO GENERAL",
        "TEORIA CURRICULAR",
        "DISENO CURRICULAR"
    ],

    "CURRICULO DE EDUCACION INICIAL": [
        "CURRICULO DE EDUCACION INICIAL",
        "DISENO CURRICULAR DE EDUCACION INICIAL",
        "PROGRAMACION CURRICULAR EN EDUCACION INICIAL"
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

    "EVALUACION DEL DESARROLLO INFANTIL": [
        "EVALUACION DEL NINO",
        "EVALUACION DEL DESARROLLO",
        "EVALUACION INFANTIL",
        "VALORACION DEL DESARROLLO INFANTIL"
    ],


    # --------------------------------------------------------
    # FAMILIA / COMUNIDAD / INCLUSIÓN
    # --------------------------------------------------------

    "FAMILIA Y COMUNIDAD": [
        "ESCUELA FAMILIA Y COMUNIDAD",
        "FAMILIA ESCUELA Y COMUNIDAD",
        "TRABAJO CON FAMILIAS",
        "PARTICIPACION FAMILIAR Y COMUNITARIA"
    ],

    "EDUCACION INCLUSIVA": [
        "INCLUSION EDUCATIVA",
        "EDUCACION ESPECIAL",
        "ATENCION A LA DIVERSIDAD",
        "NECESIDADES EDUCATIVAS ESPECIALES"
    ],

    "TUTORIA Y ORIENTACION EDUCATIVA": [
        "TUTORIA",
        "ORIENTACION EDUCATIVA",
        "ORIENTACION Y TUTORIA"
    ],


    # --------------------------------------------------------
    # TECNOLOGÍA
    # --------------------------------------------------------

    "TIC APLICADAS A LA EDUCACION": [
        "TIC EN EDUCACION",
        "TECNOLOGIAS EDUCATIVAS",
        "INFORMATICA EDUCATIVA",
        "TECNOLOGIAS DE INFORMACION APLICADAS A LA EDUCACION"
    ],

    "INTELIGENCIA ARTIFICIAL EN EDUCACION": [
        "INTELIGENCIA ARTIFICIAL APLICADA A LA EDUCACION",
        "IA EN EDUCACION",
        "TECNOLOGIAS INTELIGENTES PARA LA EDUCACION"
    ],


    # --------------------------------------------------------
    # PRÁCTICAS
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # INVESTIGACIÓN / ÉTICA
    # --------------------------------------------------------

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

    "SEMINARIO DE TESIS": [
        "SEMINARIO DE INVESTIGACION",
        "SEMINARIO DE TESIS",
        "TESIS I"
    ],

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA Y DEONTOLOGIA"
    ],


    # --------------------------------------------------------
    # ESTADÍSTICA / LÓGICA
    # --------------------------------------------------------

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "PROBABILIDAD Y ESTADISTICA",
        "ESTADISTICA APLICADA"
    ],

    "LOGICA GENERAL": [
        "LOGICA",
        "LOGICA GENERAL",
        "LOGICA FORMAL"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [
    "Educación Física no equivale automáticamente a Psicomotricidad.",
    "Psicología General no equivale automáticamente a Psicología del Desarrollo.",
    "Pediatría no equivale automáticamente a Desarrollo Infantil.",
    "Enfermería Pediátrica no equivale automáticamente a Estimulación Temprana.",
    "Literatura General no equivale automáticamente a Literatura Infantil.",
    "Arte General no equivale automáticamente a Expresión Artística Infantil.",
    "Informática general no equivale automáticamente a TIC aplicadas a Educación Inicial.",
    "Inteligencia Artificial general no equivale automáticamente a Inteligencia Artificial en Educación.",
    "Matemática General no equivale automáticamente a Pensamiento Lógico Matemático.",
    "Comunicación General no equivale automáticamente a Lenguaje Infantil.",
    "Práctica profesional no docente no equivale automáticamente a Práctica Preprofesional Pedagógica.",
    "Programación informática no equivale a Programación Curricular.",
    "Evaluación médica no equivale a Evaluación del Desarrollo Infantil.",
    "Nutrición infantil no equivale automáticamente a Desarrollo Infantil."
]


# ============================================================
# REGLAS DEL MOTOR
# ============================================================

REGLAS = {

    # Competencias
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Semáforo
    "umbral_caso_especial": 5,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # Revisión manual
    "revision_manual_asistida": True,
    "autoseleccionar_recomendaciones": True,
    "generar_caso_especial": False,
    "reevaluar_caso_especial_con_ia": False,

    # Programa
    "programa": PROGRAMA,

    # Formato especial de Educación
    "formato_educacion_tres_bloques": True,
    "usar_bloque_competencias": True,
    "actualizar_asignaturas_no_convalidadas": True,
    "usar_resumen_modalidad": True,

    # Modalidades
    "modalidad_competencia": "POR COMPETENCIA",
    "modalidad_suficiencia": "EXAMEN DE SUFICIENCIA",

    "respetar_marca_asterisco_suficiencia": True,

    # Estructura
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    # Perfil
    "nombre_especialidad": "EDUCACIÓN INICIAL",

    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS
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

BLOQUEOS Y FALSOS POSITIVOS:
{bloqueos}

La carrera de destino es EDUCACIÓN INICIAL - 1 AÑO.

El formato institucional utiliza:

1. CONVALIDACIÓN POR COMPETENCIAS.
2. ASIGNATURAS NO CONVALIDADAS.
3. RESUMEN FINAL DE MODALIDAD.

Si existe equivalencia académica:
MODALIDAD = POR COMPETENCIA.

Si el curso permanece para examen:
MODALIDAD = EXAMEN DE SUFICIENCIA.

No inventes cursos.
No inventes notas.
No reutilices cursos del certificado.
No fuerces equivalencias.

La decisión final corresponde al coordinador académico.
"""


# ============================================================
# CONFIGURACIÓN COMPLETA
# ============================================================

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
