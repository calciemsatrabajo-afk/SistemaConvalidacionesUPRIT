# ============================================================
# REGLAS PARTICULARES
# EDUCACIÓN SECUNDARIA CON MENCIÓN EN MATEMÁTICA E INFORMÁTICA
# PROGRAMA 1 AÑO
# Universidad Privada de Trujillo - UPRIT
# ============================================================

"""
Este archivo SOLO afecta a:

EDUCACIÓN SECUNDARIA CON MENCIÓN EN MATEMÁTICA E INFORMÁTICA - 1 AÑO

Formato especial de Educación:
1. Convalidación por competencias.
2. Asignaturas no convalidadas.
3. Resumen final de modalidad.

Modalidades:
- POR COMPETENCIA
- EXAMEN DE SUFICIENCIA
"""

NOMBRE_CARRERA = (
    "Educación Secundaria con mención en Matemática e Informática - 1 año"
)

PROGRAMA = "1 AÑO"


# ============================================================
# PERFIL DEL ESPECIALISTA
# ============================================================

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en
EDUCACIÓN SECUNDARIA CON MENCIÓN EN MATEMÁTICA E INFORMÁTICA,
formación docente, matemática, informática educativa y
convalidación académica por competencias.

Debes evaluar las equivalencias desde una perspectiva
pedagógica, matemática, computacional y curricular.

Considera especialmente:

- Matemática Básica.
- Álgebra.
- Geometría.
- Trigonometría.
- Cálculo.
- Análisis Matemático.
- Matemática Discreta.
- Lógica.
- Estadística y Probabilidades.
- Didáctica de la Matemática.
- Resolución de Problemas.
- Pensamiento Lógico Matemático.
- Programación.
- Algoritmos.
- Fundamentos de Computación.
- Informática Educativa.
- TIC aplicadas a la Educación.
- Ofimática Educativa.
- Sistemas de Información.
- Base de Datos.
- Programación aplicada a Educación.
- Recursos Digitales Educativos.
- E-learning.
- Inteligencia Artificial en Educación.
- Pedagogía General.
- Didáctica General.
- Psicología General.
- Psicología Educativa.
- Currículo.
- Programación Curricular.
- Evaluación Educativa.
- Práctica Preprofesional Pedagógica.
- Metodología de la Investigación.
- Investigación Educativa.
- Ética y Responsabilidad Profesional.

No debes limitarte a comparar palabras.

Debes analizar:
1. finalidad pedagógica;
2. área matemática o informática;
3. competencias desarrolladas;
4. nivel académico;
5. relación con el ejercicio docente;
6. pertinencia con Matemática e Informática;
7. correspondencia real con la asignatura UPRIT.

No fuerces equivalencias solo para reducir suficiencias.
"""


# ============================================================
# REGLAS ACADÉMICAS
# ============================================================

REGLAS_ACADEMICAS = """
REGLAS OBLIGATORIAS:

1. Usa únicamente cursos REALES del certificado y de la proforma.
2. No inventes cursos.
3. No inventes notas.
4. No inventes sílabos.
5. Un curso del certificado puede utilizarse máximo una vez.
6. Un curso UPRIT puede recibir máximo una equivalencia.
7. Prioriza coincidencias exactas.
8. Luego evalúa equivalencias por finalidad, área y competencia.
9. Una palabra coincidente no demuestra equivalencia.
10. Si requiere revisar sílabos, marcar REQUIERE VALIDACIÓN ACADÉMICA.
11. Las recomendaciones son apoyo al coordinador.
12. Toda nota parcial procede exclusivamente del certificado.
13. La nota convalidante se calcula solo con notas reales.
14. La nota convalidante máxima es 15.
15. Matemática General no equivale automáticamente a Didáctica de la Matemática.
16. Informática general no equivale automáticamente a Informática Educativa.
17. Programación informática no equivale automáticamente a Programación Curricular.
18. Inteligencia Artificial general no equivale automáticamente a IA en Educación.
19. Prácticas profesionales no docentes no equivalen automáticamente a Prácticas Pedagógicas.
20. La decisión definitiva corresponde al coordinador académico.
"""


# ============================================================
# EQUIVALENCIAS ORIENTATIVAS
# ============================================================

EQUIVALENCIAS_ORIENTATIVAS = {

    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICA BASICA",
        "FUNDAMENTOS DE MATEMATICA"
    ],

    "ALGEBRA": [
        "ALGEBRA",
        "ALGEBRA ELEMENTAL",
        "ALGEBRA LINEAL"
    ],

    "GEOMETRIA": [
        "GEOMETRIA",
        "GEOMETRIA PLANA",
        "GEOMETRIA ANALITICA"
    ],

    "TRIGONOMETRIA": [
        "TRIGONOMETRIA",
        "MATEMATICA TRIGONOMETRICA"
    ],

    "ANALISIS MATEMATICO I": [
        "CALCULO I",
        "ANALISIS MATEMATICO I",
        "CALCULO DIFERENCIAL"
    ],

    "ANALISIS MATEMATICO II": [
        "CALCULO II",
        "ANALISIS MATEMATICO II",
        "CALCULO INTEGRAL"
    ],

    "MATEMATICA DISCRETA": [
        "MATEMATICAS DISCRETAS",
        "ESTRUCTURAS DISCRETAS",
        "LOGICA Y MATEMATICA DISCRETA"
    ],

    "LOGICA GENERAL": [
        "LOGICA",
        "LOGICA GENERAL",
        "LOGICA MATEMATICA",
        "LOGICA FORMAL"
    ],

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "PROBABILIDAD Y ESTADISTICA",
        "ESTADISTICA APLICADA"
    ],

    "DIDACTICA DE LA MATEMATICA": [
        "DIDACTICA DE MATEMATICA",
        "ENSENANZA DE LA MATEMATICA",
        "METODOLOGIA DE LA ENSENANZA DE MATEMATICA"
    ],

    "RESOLUCION DE PROBLEMAS MATEMATICOS": [
        "RESOLUCION DE PROBLEMAS",
        "ESTRATEGIAS DE RESOLUCION DE PROBLEMAS",
        "PROBLEMAS MATEMATICOS"
    ],

    "PENSAMIENTO LOGICO MATEMATICO": [
        "PENSAMIENTO MATEMATICO",
        "LOGICA MATEMATICA",
        "RAZONAMIENTO MATEMATICO"
    ],

    "FUNDAMENTOS DE PROGRAMACION": [
        "PROGRAMACION",
        "PROGRAMACION I",
        "INTRODUCCION A LA PROGRAMACION",
        "ALGORITMOS Y PROGRAMACION",
        "PROGRAMACION ESTRUCTURADA"
    ],

    "ALGORITMOS": [
        "ALGORITMOS",
        "DISENO DE ALGORITMOS",
        "ANALISIS DE ALGORITMOS"
    ],

    "FUNDAMENTOS DE COMPUTACION": [
        "INTRODUCCION A LA COMPUTACION",
        "FUNDAMENTOS DE INFORMATICA",
        "COMPUTACION BASICA"
    ],

    "INFORMATICA EDUCATIVA": [
        "INFORMATICA EDUCATIVA",
        "COMPUTACION APLICADA A LA EDUCACION",
        "TECNOLOGIA EDUCATIVA"
    ],

    "TIC APLICADAS A LA EDUCACION": [
        "TIC EN EDUCACION",
        "TECNOLOGIAS EDUCATIVAS",
        "TECNOLOGIAS DE INFORMACION APLICADAS A LA EDUCACION",
        "INFORMATICA EDUCATIVA"
    ],

    "BASE DE DATOS": [
        "BASE DE DATOS",
        "BASES DE DATOS",
        "FUNDAMENTOS DE BASE DE DATOS"
    ],

    "E-LEARNING EN ENSENANZA Y APRENDIZAJE VIRTUAL": [
        "E-LEARNING",
        "EDUCACION VIRTUAL",
        "APRENDIZAJE VIRTUAL",
        "ENTORNOS VIRTUALES DE APRENDIZAJE"
    ],

    "INTELIGENCIA ARTIFICIAL EN EDUCACION": [
        "INTELIGENCIA ARTIFICIAL APLICADA A LA EDUCACION",
        "IA EN EDUCACION",
        "TECNOLOGIAS INTELIGENTES PARA LA EDUCACION"
    ],

    "PEDAGOGIA GENERAL": [
        "PEDAGOGIA",
        "PEDAGOGIA GENERAL",
        "FUNDAMENTOS DE PEDAGOGIA"
    ],

    "DIDACTICA GENERAL": [
        "DIDACTICA",
        "DIDACTICA GENERAL",
        "TEORIA DE LA ENSENANZA"
    ],

    "PSICOLOGIA GENERAL": [
        "PSICOLOGIA",
        "PSICOLOGIA GENERAL",
        "INTRODUCCION A LA PSICOLOGIA"
    ],

    "PSICOLOGIA EDUCATIVA": [
        "PSICOLOGIA DE LA EDUCACION",
        "PSICOLOGIA DEL APRENDIZAJE",
        "PSICOLOGIA ESCOLAR"
    ],

    "CURRICULO GENERAL": [
        "CURRICULO",
        "CURRICULO GENERAL",
        "TEORIA CURRICULAR",
        "DISENO CURRICULAR"
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

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA Y DEONTOLOGIA"
    ]
}


# ============================================================
# FALSOS POSITIVOS
# ============================================================

FALSOS_POSITIVOS = [
    "Matemática General no equivale automáticamente a Didáctica de la Matemática.",
    "Programación informática no equivale automáticamente a Programación Curricular.",
    "Informática general no equivale automáticamente a Informática Educativa.",
    "Ofimática no equivale automáticamente a Programación.",
    "Base de Datos no equivale automáticamente a Informática Educativa.",
    "Inteligencia Artificial general no equivale automáticamente a Inteligencia Artificial en Educación.",
    "Estadística no equivale automáticamente a Didáctica de la Matemática.",
    "Lógica computacional no equivale automáticamente a Lógica General si el contenido es exclusivamente técnico.",
    "Práctica profesional no docente no equivale automáticamente a Práctica Preprofesional Pedagógica.",
    "Sistemas Operativos no equivale automáticamente a TIC aplicadas a la Educación."
]


# ============================================================
# REGLAS DEL MOTOR
# ============================================================

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

    "programa": PROGRAMA,

    "formato_educacion_tres_bloques": True,
    "usar_bloque_competencias": True,
    "actualizar_asignaturas_no_convalidadas": True,
    "usar_resumen_modalidad": True,

    "modalidad_competencia": "POR COMPETENCIA",
    "modalidad_suficiencia": "EXAMEN DE SUFICIENCIA",

    "respetar_marca_asterisco_suficiencia": True,
    "detectar_competencia_a_la_izquierda_de_asignatura": True,

    "nombre_especialidad":
        "EDUCACIÓN SECUNDARIA CON MENCIÓN EN MATEMÁTICA E INFORMÁTICA",

    "perfil_especialista":
        PERFIL_ESPECIALISTA,

    "reglas_academicas_especialista":
        REGLAS_ACADEMICAS,

    "equivalencias_orientativas":
        EQUIVALENCIAS_ORIENTATIVAS,

    "falsos_positivos_especialidad":
        FALSOS_POSITIVOS
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

La carrera de destino es:

EDUCACIÓN SECUNDARIA CON MENCIÓN EN MATEMÁTICA E INFORMÁTICA - 1 AÑO.

El formato institucional utiliza:
1. CONVALIDACIÓN POR COMPETENCIAS.
2. ASIGNATURAS NO CONVALIDADAS.
3. RESUMEN FINAL DE MODALIDAD.

Si existe equivalencia:
MODALIDAD = POR COMPETENCIA.

Si el curso queda para examen:
MODALIDAD = EXAMEN DE SUFICIENCIA.

No inventes cursos.
No inventes notas.
No reutilices cursos del certificado.
No fuerces equivalencias.
La decisión final corresponde al coordinador académico.
"""


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
