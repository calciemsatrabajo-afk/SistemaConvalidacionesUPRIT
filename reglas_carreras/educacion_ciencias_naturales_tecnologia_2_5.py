# ============================================================
# REGLAS PARTICULARES
# EDUCACIÓN SECUNDARIA CON MENCIÓN EN CIENCIAS NATURALES Y TECNOLOGÍA - 2.5 AÑOS
# ============================================================

NOMBRE_CARRERA = "Educación Secundaria con mención en Ciencias Naturales y Tecnología - 2.5 años"
PROGRAMA = "2.5 AÑOS"

PERFIL_ESPECIALISTA = """
Actúa como especialista académico universitario senior en Educación Secundaria
con mención en Ciencias Naturales y Tecnología, formación docente y
convalidación académica por competencias.

Evalúa desde una perspectiva pedagógica, científica, experimental,
tecnológica y curricular. Considera Biología, Botánica, Zoología,
Anatomía y Fisiología, Química, Física, Ciencias Naturales, Ciencia y
Tecnología, Ecología, Medio Ambiente, Educación Ambiental, Laboratorio,
metodología experimental, didáctica de las ciencias, Pedagogía, Psicología,
Currículo, Evaluación, TIC, IA aplicada a Educación, prácticas pedagógicas
e investigación educativa.

No compares únicamente nombres. Analiza finalidad, contenidos disciplinares,
competencias científicas, componente experimental, aplicación pedagógica y
pertinencia con la enseñanza secundaria. No fuerces equivalencias para
reducir suficiencias.
"""

REGLAS_ACADEMICAS = """
1. Usa únicamente cursos reales del certificado y la proforma.
2. No inventes cursos, notas, sílabos ni contenidos.
3. Un curso del certificado puede utilizarse máximo una vez.
4. Un curso UPRIT puede recibir máximo una equivalencia.
5. Prioriza coincidencias exactas y luego equivalencias por competencia.
6. Si requiere revisar sílabos, marcar REQUIERE VALIDACIÓN ACADÉMICA.
7. Toda nota parcial procede exclusivamente del certificado.
8. La nota convalidante máxima es 15.
9. Educación Física NO equivale a Física.
10. Química Industrial no equivale automáticamente a Didáctica de la Química.
11. Biología General no equivale automáticamente a Didáctica de la Biología.
12. Física General no equivale automáticamente a Didáctica de la Física.
13. Tecnología industrial no equivale automáticamente a Tecnología Educativa.
14. Informática general no equivale automáticamente a TIC aplicadas a Educación.
15. Prácticas profesionales no docentes no equivalen a prácticas pedagógicas.
16. La decisión definitiva corresponde al coordinador académico.
"""

EQUIVALENCIAS_ORIENTATIVAS = {
    "BIOLOGIA GENERAL": ["BIOLOGIA", "BIOLOGIA GENERAL", "FUNDAMENTOS DE BIOLOGIA", "CIENCIAS BIOLOGICAS"],
    "BOTANICA": ["BOTANICA", "BIOLOGIA VEGETAL", "BOTANICA GENERAL"],
    "ZOOLOGIA": ["ZOOLOGIA", "BIOLOGIA ANIMAL", "ZOOLOGIA GENERAL"],
    "ANATOMIA Y FISIOLOGIA": ["ANATOMIA", "FISIOLOGIA", "ANATOMIA Y FISIOLOGIA", "ANATOMIA HUMANA"],
    "QUIMICA GENERAL": ["QUIMICA", "QUIMICA GENERAL", "FUNDAMENTOS DE QUIMICA"],
    "QUIMICA ORGANICA": ["QUIMICA ORGANICA", "QUIMICA DEL CARBONO"],
    "QUIMICA INORGANICA": ["QUIMICA INORGANICA", "QUIMICA MINERAL"],
    "FISICA GENERAL": ["FISICA", "FISICA GENERAL", "FUNDAMENTOS DE FISICA"],
    "CIENCIAS NATURALES": ["CIENCIAS NATURALES", "CIENCIA Y AMBIENTE", "CIENCIA TECNOLOGIA Y AMBIENTE"],
    "CIENCIA Y TECNOLOGIA": ["CIENCIA Y TECNOLOGIA", "CIENCIA TECNOLOGIA Y AMBIENTE", "CIENCIAS NATURALES Y TECNOLOGIA"],
    "ECOLOGIA E IMPACTO AMBIENTAL": ["ECOLOGIA", "ECOLOGIA Y MEDIO AMBIENTE", "MEDIO AMBIENTE", "GESTION AMBIENTAL"],
    "EDUCACION AMBIENTAL": ["EDUCACION AMBIENTAL", "CULTURA AMBIENTAL", "EDUCACION PARA EL DESARROLLO SOSTENIBLE"],
    "LABORATORIO DE CIENCIAS": ["LABORATORIO DE CIENCIAS", "LABORATORIO DE BIOLOGIA", "LABORATORIO DE QUIMICA", "LABORATORIO DE FISICA"],
    "METODOLOGIA EXPERIMENTAL": ["METODO EXPERIMENTAL", "METODOLOGIA EXPERIMENTAL", "TECNICAS EXPERIMENTALES"],
    "DIDACTICA DE LAS CIENCIAS NATURALES": ["DIDACTICA DE LAS CIENCIAS", "DIDACTICA DE CIENCIAS NATURALES", "ENSENANZA DE LAS CIENCIAS"],
    "DIDACTICA DE LA BIOLOGIA": ["DIDACTICA DE BIOLOGIA", "ENSENANZA DE LA BIOLOGIA"],
    "DIDACTICA DE LA QUIMICA": ["DIDACTICA DE QUIMICA", "ENSENANZA DE LA QUIMICA"],
    "DIDACTICA DE LA FISICA": ["DIDACTICA DE FISICA", "ENSENANZA DE LA FISICA"],
    "PEDAGOGIA GENERAL": ["PEDAGOGIA", "PEDAGOGIA GENERAL", "FUNDAMENTOS DE PEDAGOGIA"],
    "DIDACTICA GENERAL": ["DIDACTICA", "DIDACTICA GENERAL", "TEORIA DE LA ENSENANZA"],
    "PSICOLOGIA GENERAL": ["PSICOLOGIA", "PSICOLOGIA GENERAL", "INTRODUCCION A LA PSICOLOGIA"],
    "PSICOLOGIA EDUCATIVA": ["PSICOLOGIA DE LA EDUCACION", "PSICOLOGIA DEL APRENDIZAJE", "PSICOLOGIA ESCOLAR"],
    "CURRICULO GENERAL": ["CURRICULO", "CURRICULO GENERAL", "TEORIA CURRICULAR", "DISENO CURRICULAR"],
    "PROGRAMACION CURRICULAR": ["PLANIFICACION CURRICULAR", "PROGRAMACION CURRICULAR", "DIVERSIFICACION CURRICULAR"],
    "EVALUACION EDUCATIVA": ["EVALUACION DEL APRENDIZAJE", "EVALUACION EDUCACIONAL", "EVALUACION PEDAGOGICA"],
    "TIC APLICADAS A LA EDUCACION": ["TIC EN EDUCACION", "TECNOLOGIAS EDUCATIVAS", "INFORMATICA EDUCATIVA"],
    "INTELIGENCIA ARTIFICIAL EN EDUCACION": ["INTELIGENCIA ARTIFICIAL APLICADA A LA EDUCACION", "IA EN EDUCACION"],
    "PRACTICA PREPROFESIONAL PEDAGOGICA I": ["PRACTICA PREPROFESIONAL I", "PRACTICA PEDAGOGICA I", "PRACTICA DOCENTE I"],
    "PRACTICA PREPROFESIONAL PEDAGOGICA II": ["PRACTICA PREPROFESIONAL II", "PRACTICA PEDAGOGICA II", "PRACTICA DOCENTE II"],
    "PRACTICA PREPROFESIONAL PEDAGOGICA III": ["PRACTICA PREPROFESIONAL III", "PRACTICA PEDAGOGICA III", "PRACTICA DOCENTE III"],
    "PRACTICA PREPROFESIONAL PEDAGOGICA IV": ["PRACTICA PREPROFESIONAL IV", "PRACTICA PEDAGOGICA IV", "PRACTICA DOCENTE IV"],
    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": ["METODOLOGIA DE LA INVESTIGACION", "INVESTIGACION CIENTIFICA"],
    "INVESTIGACION EDUCATIVA": ["INVESTIGACION PEDAGOGICA", "INVESTIGACION EN EDUCACION"],
    "ETICA Y RESPONSABILIDAD PROFESIONAL": ["ETICA", "ETICA PROFESIONAL", "ETICA Y DEONTOLOGIA"]
}

FALSOS_POSITIVOS = [
    "Educación Física no equivale a Física.",
    "Química Industrial no equivale automáticamente a Didáctica de la Química.",
    "Biología General no equivale automáticamente a Didáctica de la Biología.",
    "Física General no equivale automáticamente a Didáctica de la Física.",
    "Tecnología industrial no equivale automáticamente a Tecnología Educativa.",
    "Informática general no equivale automáticamente a TIC aplicadas a Educación.",
    "Mecánica automotriz no equivale automáticamente a Física.",
    "Práctica profesional no docente no equivale a Práctica Preprofesional Pedagógica."
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
    "programa": PROGRAMA,
    "formato_educacion_tres_bloques": True,
    "usar_bloque_competencias": True,
    "actualizar_asignaturas_no_convalidadas": True,
    "usar_resumen_modalidad": True,
    "modalidad_competencia": "POR COMPETENCIA",
    "modalidad_suficiencia": "EXAMEN DE SUFICIENCIA",
    "respetar_marca_asterisco_suficiencia": True,
    "detectar_competencia_a_la_izquierda_de_asignatura": True,
    "nombre_especialidad": "EDUCACIÓN SECUNDARIA CON MENCIÓN EN CIENCIAS NATURALES Y TECNOLOGÍA",
    "perfil_especialista": PERFIL_ESPECIALISTA,
    "reglas_academicas_especialista": REGLAS_ACADEMICAS,
    "equivalencias_orientativas": EQUIVALENCIAS_ORIENTATIVAS,
    "falsos_positivos_especialidad": FALSOS_POSITIVOS
}

def obtener_instrucciones_especialista():
    bloqueos = "\n".join(f"- {x}" for x in FALSOS_POSITIVOS)
    return f"""
{PERFIL_ESPECIALISTA}

{REGLAS_ACADEMICAS}

BLOQUEOS Y FALSOS POSITIVOS:
{bloqueos}

Carrera de destino:
EDUCACIÓN SECUNDARIA CON MENCIÓN EN CIENCIAS NATURALES Y TECNOLOGÍA - 2.5 AÑOS.

Si existe equivalencia: MODALIDAD = POR COMPETENCIA.
Si el curso queda para examen: MODALIDAD = EXAMEN DE SUFICIENCIA.

No inventes cursos ni notas. No reutilices cursos del certificado.
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
