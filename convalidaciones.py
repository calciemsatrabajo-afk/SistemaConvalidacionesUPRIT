import importlib
import json
import re
import unicodedata
from collections import defaultdict

import streamlit as st
from docx import Document
from openai import OpenAI
from rapidfuzz import fuzz


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

NOTA_MAXIMA_CONVALIDANTE = 15
MAXIMO_EXAMENES_SUFICIENCIA = 7

client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)


# ============================================================
# REGLAS POR CARRERA
# ============================================================

REGLAS_GENERALES = {
    # Conserva el comportamiento general que ya tenía el sistema.
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,
    "umbral_caso_especial": 7,
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,
    "reevaluar_caso_especial_con_ia": False,

    # Por defecto NO se asume que la columna inmediatamente a la
    # izquierda de ASIGNATURA sea la competencia. Esto evita afectar
    # plantillas de otras carreras.
    "detectar_competencia_a_la_izquierda_de_asignatura": False,
}


MAPA_MODULOS_REGLAS = {
    "INGENIERIA CIVIL": "civil",
    "INGENIERIA INDUSTRIAL": "industrial",
    "INGENIERIA DE SISTEMAS E IA": "sistemas_ia",
    "INGENIERIA DE SISTEMAS Y IA": "sistemas_ia",
    "PSICOLOGIA": "psicologia",
    "EDUCACION": "educacion",

    # Administración de Empresas - 2 años
    "ADMINISTRACION DE EMPRESAS - 2 ANOS": "administracion_2",
    "ADMINISTRACION DE EMPRESAS 2 ANOS": "administracion_2",
    "ADMINISTRACION - 2 ANOS": "administracion_2",
    "ADMINISTRACION 2 ANOS": "administracion_2",

    # Administración de Empresas - 2.5 años
    "ADMINISTRACION DE EMPRESAS - 2.5 ANOS": "administracion_2_5",
    "ADMINISTRACION DE EMPRESAS 2.5 ANOS": "administracion_2_5",
    "ADMINISTRACION - 2.5 ANOS": "administracion_2_5",
    "ADMINISTRACION 2.5 ANOS": "administracion_2_5",

    # Contabilidad - 2 años
    "CONTABILIDAD - 2 ANOS": "contabilidad_2",
    "CONTABILIDAD 2 ANOS": "contabilidad_2",
    "CONTABILIDAD DE EMPRESAS - 2 ANOS": "contabilidad_2",
    "CONTABILIDAD DE EMPRESAS 2 ANOS": "contabilidad_2",

    # Contabilidad - 2.5 años
    "CONTABILIDAD - 2.5 ANOS": "contabilidad_2_5",
    "CONTABILIDAD 2.5 ANOS": "contabilidad_2_5",
    "CONTABILIDAD DE EMPRESAS - 2.5 ANOS": "contabilidad_2_5",
    "CONTABILIDAD DE EMPRESAS 2.5 ANOS": "contabilidad_2_5",

    # Educación Secundaria con mención en Ciencias Sociales - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS SOCIALES - 1 ANO":
        "educacion_ciencias_sociales_1",

    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS SOCIALES 1 ANO":
        "educacion_ciencias_sociales_1",

    "EDUCACION SECUNDARIA - CIENCIAS SOCIALES - 1 ANO":
        "educacion_ciencias_sociales_1",

    "EDUCACION CIENCIAS SOCIALES - 1 ANO":
        "educacion_ciencias_sociales_1",

    "EDUCACION CIENCIAS SOCIALES 1 ANO":
        "educacion_ciencias_sociales_1",

    # Educación Secundaria con mención en Ciencias Sociales - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS SOCIALES - 2.5 ANOS":
        "educacion_ciencias_sociales_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS SOCIALES 2.5 ANOS":
        "educacion_ciencias_sociales_2_5",

    "EDUCACION SECUNDARIA - CIENCIAS SOCIALES - 2.5 ANOS":
        "educacion_ciencias_sociales_2_5",

    "EDUCACION CIENCIAS SOCIALES - 2.5 ANOS":
        "educacion_ciencias_sociales_2_5",

    "EDUCACION CIENCIAS SOCIALES 2.5 ANOS":
        "educacion_ciencias_sociales_2_5",

    # Educación Primaria - 1 año
    "EDUCACION PRIMARIA - 1 ANO":
        "educacion_primaria_1",

    "EDUCACION PRIMARIA 1 ANO":
        "educacion_primaria_1",

    "CARRERA PROFESIONAL DE EDUCACION PRIMARIA - 1 ANO":
        "educacion_primaria_1",

    "CARRERA PROFESIONAL DE EDUCACION PRIMARIA 1 ANO":
        "educacion_primaria_1",

    # Educación Primaria - 2.5 años
    "EDUCACION PRIMARIA - 2.5 ANOS":
        "educacion_primaria_2_5",

    "EDUCACION PRIMARIA 2.5 ANOS":
        "educacion_primaria_2_5",

    "CARRERA PROFESIONAL DE EDUCACION PRIMARIA - 2.5 ANOS":
        "educacion_primaria_2_5",

    "CARRERA PROFESIONAL DE EDUCACION PRIMARIA 2.5 ANOS":
        "educacion_primaria_2_5",

    # Educación Inicial - 1 año
    "EDUCACION INICIAL - 1 ANO":
        "educacion_inicial_1",

    "EDUCACION INICIAL 1 ANO":
        "educacion_inicial_1",

    "CARRERA PROFESIONAL DE EDUCACION INICIAL - 1 ANO":
        "educacion_inicial_1",

    "CARRERA PROFESIONAL DE EDUCACION INICIAL 1 ANO":
        "educacion_inicial_1",

    # Educación Inicial - 2.5 años
    "EDUCACION INICIAL - 2.5 ANOS":
        "educacion_inicial_2_5",

    "EDUCACION INICIAL 2.5 ANOS":
        "educacion_inicial_2_5",

    "CARRERA PROFESIONAL DE EDUCACION INICIAL - 2.5 ANOS":
        "educacion_inicial_2_5",

    "CARRERA PROFESIONAL DE EDUCACION INICIAL 2.5 ANOS":
        "educacion_inicial_2_5",

    # Educación Secundaria con mención en Matemática e Informática - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN MATEMATICA E INFORMATICA - 1 ANO":
        "educacion_matematica_informatica_1",

    "EDUCACION SECUNDARIA CON MENCION EN MATEMATICA E INFORMATICA 1 ANO":
        "educacion_matematica_informatica_1",

    "EDUCACION MATEMATICA E INFORMATICA - 1 ANO":
        "educacion_matematica_informatica_1",

    "EDUCACION MATEMATICA E INFORMATICA 1 ANO":
        "educacion_matematica_informatica_1",

    # Educación Secundaria con mención en Matemática e Informática - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN MATEMATICA E INFORMATICA - 2.5 ANOS":
        "educacion_matematica_informatica_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN MATEMATICA E INFORMATICA 2.5 ANOS":
        "educacion_matematica_informatica_2_5",

    "EDUCACION MATEMATICA E INFORMATICA - 2.5 ANOS":
        "educacion_matematica_informatica_2_5",

    "EDUCACION MATEMATICA E INFORMATICA 2.5 ANOS":
        "educacion_matematica_informatica_2_5",

    # Educación Secundaria con mención en Comunicación, Literatura y Lingüística - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN COMUNICACION, LITERATURA Y LINGUISTICA - 1 ANO":
        "educacion_comunicacion_literatura_linguistica_1",

    "EDUCACION SECUNDARIA CON MENCION EN COMUNICACION, LITERATURA Y LINGUISTICA 1 ANO":
        "educacion_comunicacion_literatura_linguistica_1",

    "EDUCACION COMUNICACION LITERATURA LINGUISTICA - 1 ANO":
        "educacion_comunicacion_literatura_linguistica_1",

    "EDUCACION COMUNICACION LITERATURA LINGUISTICA 1 ANO":
        "educacion_comunicacion_literatura_linguistica_1",

    # Educación Secundaria con mención en Comunicación, Literatura y Lingüística - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN COMUNICACION, LITERATURA Y LINGUISTICA - 2.5 ANOS":
        "educacion_comunicacion_literatura_linguistica_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN COMUNICACION, LITERATURA Y LINGUISTICA 2.5 ANOS":
        "educacion_comunicacion_literatura_linguistica_2_5",

    "EDUCACION COMUNICACION LITERATURA LINGUISTICA - 2.5 ANOS":
        "educacion_comunicacion_literatura_linguistica_2_5",

    "EDUCACION COMUNICACION LITERATURA LINGUISTICA 2.5 ANOS":
        "educacion_comunicacion_literatura_linguistica_2_5",

    # Educación Secundaria con mención en Ciencias Naturales y Tecnología - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS NATURALES Y TECNOLOGIA - 1 ANO":
        "educacion_ciencias_naturales_tecnologia_1",
    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS NATURALES Y TECNOLOGIA 1 ANO":
        "educacion_ciencias_naturales_tecnologia_1",
    "EDUCACION CIENCIAS NATURALES Y TECNOLOGIA - 1 ANO":
        "educacion_ciencias_naturales_tecnologia_1",
    "EDUCACION CIENCIAS NATURALES Y TECNOLOGIA 1 ANO":
        "educacion_ciencias_naturales_tecnologia_1",

    # Educación Secundaria con mención en Ciencias Naturales y Tecnología - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS NATURALES Y TECNOLOGIA - 2.5 ANOS":
        "educacion_ciencias_naturales_tecnologia_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN CIENCIAS NATURALES Y TECNOLOGIA 2.5 ANOS":
        "educacion_ciencias_naturales_tecnologia_2_5",

    "EDUCACION CIENCIAS NATURALES Y TECNOLOGIA - 2.5 ANOS":
        "educacion_ciencias_naturales_tecnologia_2_5",

    "EDUCACION CIENCIAS NATURALES Y TECNOLOGIA 2.5 ANOS":
        "educacion_ciencias_naturales_tecnologia_2_5",

    # Educación Secundaria con mención en Educación Física y Ciencias del Deporte - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN EDUCACION FISICA Y CIENCIAS DEL DEPORTE - 1 ANO":
        "educacion_fisica_deporte_1",

    "EDUCACION SECUNDARIA CON MENCION EN EDUCACION FISICA Y CIENCIAS DEL DEPORTE 1 ANO":
        "educacion_fisica_deporte_1",

    "EDUCACION FISICA Y CIENCIAS DEL DEPORTE - 1 ANO":
        "educacion_fisica_deporte_1",

    "EDUCACION FISICA Y CIENCIAS DEL DEPORTE 1 ANO":
        "educacion_fisica_deporte_1",

    # Educación Secundaria con mención en Educación Física y Ciencias del Deporte - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN EDUCACION FISICA Y CIENCIAS DEL DEPORTE - 2.5 ANOS":
        "educacion_fisica_deporte_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN EDUCACION FISICA Y CIENCIAS DEL DEPORTE 2.5 ANOS":
        "educacion_fisica_deporte_2_5",

    "EDUCACION FISICA Y CIENCIAS DEL DEPORTE - 2.5 ANOS":
        "educacion_fisica_deporte_2_5",

    "EDUCACION FISICA Y CIENCIAS DEL DEPORTE 2.5 ANOS":
        "educacion_fisica_deporte_2_5",

    # Educación Secundaria con mención en Idiomas Extranjeros - 1 año
    "EDUCACION SECUNDARIA CON MENCION EN IDIOMAS EXTRANJEROS - 1 ANO":
        "educacion_idiomas_extranjeros_1",

    "EDUCACION SECUNDARIA CON MENCION EN IDIOMAS EXTRANJEROS 1 ANO":
        "educacion_idiomas_extranjeros_1",

    "EDUCACION IDIOMAS EXTRANJEROS - 1 ANO":
        "educacion_idiomas_extranjeros_1",

    "EDUCACION IDIOMAS EXTRANJEROS 1 ANO":
        "educacion_idiomas_extranjeros_1",

    # Educación Secundaria con mención en Idiomas Extranjeros - 2.5 años
    "EDUCACION SECUNDARIA CON MENCION EN IDIOMAS EXTRANJEROS - 2.5 ANOS":
        "educacion_idiomas_extranjeros_2_5",

    "EDUCACION SECUNDARIA CON MENCION EN IDIOMAS EXTRANJEROS 2.5 ANOS":
        "educacion_idiomas_extranjeros_2_5",

    "EDUCACION IDIOMAS EXTRANJEROS - 2.5 ANOS":
        "educacion_idiomas_extranjeros_2_5",

    "EDUCACION IDIOMAS EXTRANJEROS 2.5 ANOS":
        "educacion_idiomas_extranjeros_2_5",
}


def cargar_reglas_carrera(
    carrera_destino=""
):
    """
    Devuelve una copia de las reglas generales y, cuando exista,
    aplica encima las reglas particulares de la carrera.

    Si el archivo de reglas de una carrera todavía no existe,
    el sistema continúa usando las reglas generales.
    """

    reglas = dict(
        REGLAS_GENERALES
    )

    carrera_normal = normalizar(
        carrera_destino
    )

    modulo = MAPA_MODULOS_REGLAS.get(
        carrera_normal
    )

    if not modulo:
        return reglas

    try:
        modulo_reglas = importlib.import_module(
            f"reglas_carreras.{modulo}"
        )
    except ModuleNotFoundError:
        # La carrera todavía no tiene reglas particulares.
        return reglas
    except Exception:
        # Una regla particular nunca debe tumbar el motor general.
        return reglas

    reglas_especificas = getattr(
        modulo_reglas,
        "REGLAS",
        None
    )

    if reglas_especificas is None:
        # Compatibilidad con el nombre REGLAS_CIVIL.
        reglas_especificas = getattr(
            modulo_reglas,
            f"REGLAS_{modulo.upper()}",
            {}
        )

    if isinstance(
        reglas_especificas,
        dict
    ):
        reglas.update(
            reglas_especificas
        )

    # Cargar instrucciones especializadas de la carrera, si existen.
    obtener_instrucciones = getattr(
        modulo_reglas,
        "obtener_instrucciones_especialista",
        None
    )

    if callable(
        obtener_instrucciones
    ):
        try:
            reglas[
                "instrucciones_especialista"
            ] = obtener_instrucciones()
        except Exception:
            pass

    return reglas


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def analizar_convalidaciones(
    cursos_alumno,
    ruta_formato="formato.docx",
    carrera_destino=""
):
    """
    Motor general de convalidaciones para TODAS las carreras.

    Orden de decisión:
    1. coincidencia exacta;
    2. coincidencia por nombre muy similar;
    3. equivalencias determinísticas seguras;
    4. equivalencia semántica con DeepSeek;
    5. evaluación por competencias;
    6. cálculo de nota convalidante;
    7. suficiencias y caso especial.

    Reglas:
    - un curso de procedencia solo puede utilizarse una vez;
    - un curso UPRIT solo puede recibir una equivalencia;
    - la nota parcial SIEMPRE sale del certificado;
    - DeepSeek nunca inventa notas;
    - la nota convalidante se calcula con las notas parciales reales;
    - tope de nota convalidante: 15;
    - 1 faltante en competencia: se mantiene fila vacía solo en ese curso;
    - 2 o más faltantes: candidatos a suficiencia;
    - más de 7 suficiencias: caso especial.
    """

    if not cursos_alumno:
        raise ValueError(
            "No existen cursos del certificado para analizar."
        )

    # Cargar reglas específicas únicamente para la carrera
    # seleccionada. Las demás carreras conservan sus reglas generales.
    reglas = cargar_reglas_carrera(
        carrera_destino
    )

    estructura_proforma = leer_estructura_proforma(
        ruta_formato=ruta_formato,
        reglas=reglas
    )

    estructura_proforma = filtrar_estructura_proforma(
        estructura_proforma
    )

    if not estructura_proforma:
        raise ValueError(
            f"No se pudieron leer las asignaturas de la proforma: "
            f"{ruta_formato}"
        )

    cursos_proforma = [
        item["curso"]
        for item in estructura_proforma
    ]

    # --------------------------------------------------------
    # 1) COINCIDENCIAS EXACTAS
    # --------------------------------------------------------

    directas = buscar_coincidencias_exactas(
        cursos_alumno,
        estructura_proforma
    )

    usados_origen = {
        normalizar(
            x.get(
                "curso_origen",
                ""
            )
        )
        for x in directas
        if x.get(
            "curso_origen"
        )
    }

    usados_destino = {
        normalizar(
            x.get(
                "curso_destino",
                ""
            )
        )
        for x in directas
        if x.get(
            "curso_destino"
        )
    }

    # --------------------------------------------------------
    # 2) COINCIDENCIAS POR NOMBRE MUY SIMILAR
    # --------------------------------------------------------

    cercanas = buscar_coincidencias_cercanas(
        cursos_alumno=cursos_alumno,
        estructura_proforma=estructura_proforma,
        usados_origen=usados_origen,
        usados_destino=usados_destino
    )

    usados_origen.update(
        normalizar(
            x.get(
                "curso_origen",
                ""
            )
        )
        for x in cercanas
        if x.get(
            "curso_origen"
        )
    )

    usados_destino.update(
        normalizar(
            x.get(
                "curso_destino",
                ""
            )
        )
        for x in cercanas
        if x.get(
            "curso_destino"
        )
    )

    # --------------------------------------------------------
    # 3) RESPALDO DETERMINÍSTICO SEGURO
    # --------------------------------------------------------

    respaldo = buscar_equivalencias_respaldo(
        cursos_alumno=cursos_alumno,
        estructura_proforma=estructura_proforma,
        usados_origen=usados_origen,
        usados_destino=usados_destino,
        reglas=reglas
    )

    usados_origen.update(
        normalizar(
            x.get(
                "curso_origen",
                ""
            )
        )
        for x in respaldo
        if x.get(
            "curso_origen"
        )
    )

    usados_destino.update(
        normalizar(
            x.get(
                "curso_destino",
                ""
            )
        )
        for x in respaldo
        if x.get(
            "curso_destino"
        )
    )

    # --------------------------------------------------------
    # 4) DEEPSEEK SOLO CON LOS CURSOS RESTANTES
    # --------------------------------------------------------

    alumnos_restantes = [
        item
        for item in cursos_alumno
        if normalizar(
            item.get(
                "curso",
                ""
            )
        ) not in usados_origen
    ]

    proforma_restante = [
        item
        for item in estructura_proforma
        if normalizar(
            item.get(
                "curso",
                ""
            )
        ) not in usados_destino
    ]

    propuesta_ia = []

    if (
        alumnos_restantes
        and proforma_restante
    ):
        propuesta_ia = consultar_deepseek(
            cursos_alumno=alumnos_restantes,
            estructura_proforma=proforma_restante,
            carrera_destino=carrera_destino,
            reglas=reglas
        )

    equivalencias_ia = validar_equivalencias(
        propuesta=propuesta_ia,
        cursos_alumno=alumnos_restantes,
        estructura_proforma=proforma_restante
    )

    # --------------------------------------------------------
    # 5) UNIR EQUIVALENCIAS BASE
    # --------------------------------------------------------

    convalidaciones_base = (
        directas
        + cercanas
        + respaldo
        + equivalencias_ia
    )

    convalidaciones_base = eliminar_duplicados_equivalencias(
        convalidaciones_base
    )

    # --------------------------------------------------------
    # 5.1) RECUPERAR NOTAS FALTANTES DESDE EL CERTIFICADO
    #
    # Si una equivalencia ya tiene curso_origen pero perdió la nota
    # durante una etapa intermedia, buscamos exclusivamente la nota
    # de ese mismo curso en cursos_alumno.
    # --------------------------------------------------------

    convalidaciones_base = rehidratar_notas_equivalencias(
        equivalencias=convalidaciones_base,
        cursos_alumno=cursos_alumno
    )

    # --------------------------------------------------------
    # 6) EVALUAR POR COMPETENCIAS
    # --------------------------------------------------------

    evaluacion = evaluar_por_competencias(
        estructura_proforma=estructura_proforma,
        convalidaciones_base=convalidaciones_base,
        cursos_alumno=cursos_alumno,
        reglas=reglas
    )

    convalidaciones = evaluacion[
        "convalidaciones"
    ]

    pendientes = evaluacion[
        "pendientes"
    ]

    suficiencias = evaluacion[
        "suficiencias"
    ]

    competencias = evaluacion[
        "competencias"
    ]

    # --------------------------------------------------------
    # 6.1) SEGUNDA REVISIÓN PARA CASO ESPECIAL - CIVIL / INDUSTRIAL
    # --------------------------------------------------------

    suficiencias_iniciales = list(
        suficiencias
    )

    umbral_caso_especial = int(
        reglas.get(
            "umbral_caso_especial",
            reglas.get(
                "maximo_suficiencias",
                MAXIMO_EXAMENES_SUFICIENCIA
            )
        )
    )

    maximo_suficiencias_final = int(
        reglas.get(
            "maximo_suficiencias_final",
            reglas.get(
                "maximo_suficiencias",
                MAXIMO_EXAMENES_SUFICIENCIA
            )
        )
    )

    revision_especial_realizada = False
    equivalencias_nuevas_revision = []
    suficiencias_excedentes_revision = []

    carrera_normal = normalizar(
        carrera_destino
    )

    es_ingenieria_civil = (
        carrera_normal
        == "INGENIERIA CIVIL"
    )

    es_ingenieria_industrial = (
        carrera_normal
        == "INGENIERIA INDUSTRIAL"
    )

    es_carrera_con_revision_especial = (
        es_ingenieria_civil
        or es_ingenieria_industrial
    )

    if (
        es_carrera_con_revision_especial
        and reglas.get(
            "reevaluar_caso_especial_con_ia",
            False
        )
        and len(
            suficiencias
        ) > umbral_caso_especial
    ):
        revision_especial_realizada = True

        if es_ingenieria_civil:

            equivalencias_nuevas_revision = (
                reevaluar_caso_especial_ingenieria_civil(
                    cursos_alumno=cursos_alumno,
                    estructura_proforma=estructura_proforma,
                    convalidaciones_actuales=convalidaciones_base,
                    competencias_actuales=competencias,
                    suficiencias_actuales=suficiencias
                )
            )

        else:

            equivalencias_nuevas_revision = (
                reevaluar_caso_especial_ingenieria_industrial(
                    cursos_alumno=cursos_alumno,
                    estructura_proforma=estructura_proforma,
                    convalidaciones_actuales=convalidaciones_base,
                    competencias_actuales=competencias,
                    suficiencias_actuales=suficiencias,
                    reglas=reglas
                )
            )

        if equivalencias_nuevas_revision:

            convalidaciones_base = (
                convalidaciones_base
                + equivalencias_nuevas_revision
            )

            convalidaciones_base = (
                eliminar_duplicados_equivalencias(
                    convalidaciones_base
                )
            )

            convalidaciones_base = (
                rehidratar_notas_equivalencias(
                    equivalencias=convalidaciones_base,
                    cursos_alumno=cursos_alumno
                )
            )

            evaluacion = evaluar_por_competencias(
                estructura_proforma=estructura_proforma,
                convalidaciones_base=convalidaciones_base,
                cursos_alumno=cursos_alumno,
                reglas=reglas
            )

            convalidaciones = evaluacion[
                "convalidaciones"
            ]

            pendientes = evaluacion[
                "pendientes"
            ]

            suficiencias = filtrar_lista_suficiencias(
                evaluacion[
                    "suficiencias"
                ]
            )

            competencias = evaluacion[
                "competencias"
            ]

    # --------------------------------------------------------
    # LISTA COMPLETA DESPUÉS DE LA SEGUNDA REVISIÓN
    #
    # IMPORTANTE:
    # aquí todavía NO se recorta nada. Esta lista puede contener
    # 8, 10, 12... cursos. Se conserva completa para auditoría
    # y para el Word de CASO ESPECIAL.
    # --------------------------------------------------------

    suficiencias_post_revision_completas = list(
        suficiencias
    )

    # Máximo absoluto de suficiencias en carreras con revisión especial.
    # SOLO AHORA, después de la segunda revisión, se limita a 7.
    # Los excedentes NO se convalidan automáticamente.
    if (
        es_ingenieria_civil
        and len(
            suficiencias_post_revision_completas
        ) > maximo_suficiencias_final
    ):
        suficiencias_excedentes_revision = (
            suficiencias_post_revision_completas[
                maximo_suficiencias_final:
            ]
        )

        suficiencias = (
            suficiencias_post_revision_completas[
                :maximo_suficiencias_final
            ]
        )

        for curso_excedente in suficiencias_excedentes_revision:
            if curso_excedente not in pendientes:
                pendientes.append(
                    curso_excedente
                )

    else:
        suficiencias = list(
            suficiencias_post_revision_completas
        )

    # --------------------------------------------------------
    # 7) CURSOS NO UTILIZADOS
    # --------------------------------------------------------

    origenes_finales_usados = {
        normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )
        for item in convalidaciones
        if item.get(
            "curso_origen"
        )
    }

    cursos_no_utilizados = [
        item
        for item in cursos_alumno
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in origenes_finales_usados
        )
    ]

    # --------------------------------------------------------
    # 8) FILTRO FINAL DE SUFICIENCIAS / PENDIENTES
    # --------------------------------------------------------

    suficiencias = filtrar_lista_suficiencias(
        suficiencias
    )

    pendientes = filtrar_lista_suficiencias(
        pendientes
    )

    # --------------------------------------------------------
    # 9) CASO ESPECIAL
    # --------------------------------------------------------

    maximo_suficiencias_carrera = int(
        reglas.get(
            "maximo_suficiencias",
            MAXIMO_EXAMENES_SUFICIENCIA
        )
    )

    # El caso especial se activa cuando el resultado inicial
    # supera el umbral ordinario de 5 o cuando existen excedentes
    # pendientes de revisión.
    generar_caso_especial = bool(
        reglas.get(
            "generar_caso_especial",
            True
        )
    )

    caso_especial = (
        generar_caso_especial
        and len(
            suficiencias_iniciales
        ) > umbral_caso_especial
    )

    observacion_caso_especial = ""

    if caso_especial:

        nombre_carrera_observacion = (
            "INGENIERÍA CIVIL"
            if es_ingenieria_civil
            else (
                "INGENIERÍA INDUSTRIAL"
                if es_ingenieria_industrial
                else str(
                    carrera_destino
                    or "CARRERA"
                ).upper()
            )
        )

        observacion_caso_especial = (
            f"CASO ESPECIAL - {nombre_carrera_observacion}: "
            f"el umbral ordinario es de "
            f"{umbral_caso_especial} asignaturas de suficiencia. "
            f"Antes de la segunda revisión se identificaron "
            f"{len(suficiencias_iniciales)} candidatos reales a suficiencia. "
        )

        if revision_especial_realizada:
            observacion_caso_especial += (
                "El expediente fue sometido a una segunda revisión "
                "integral de todos los cursos del certificado y de la "
                "proforma mediante un análisis académico especializado "
                f"en {nombre_carrera_observacion.title()}. "
            )

        observacion_caso_especial += (
            f"Después de la segunda revisión quedaron "
            f"{len(suficiencias_post_revision_completas)} cursos "
            f"todavía faltantes. De ellos, se seleccionaron "
            f"{len(suficiencias)} asignaturas para examen de suficiencia, "
            f"respetando un máximo absoluto de "
            f"{maximo_suficiencias_final}. "
        )

        if suficiencias_excedentes_revision:
            observacion_caso_especial += (
                f"Adicionalmente, {len(suficiencias_excedentes_revision)} "
                f"asignatura(s) quedaron como PENDIENTES DE REVISIÓN "
                f"ACADÉMICA y NO se consideran convalidadas ni se agregan "
                f"como exámenes de suficiencia. Cursos pendientes: "
                + ", ".join(
                    suficiencias_excedentes_revision
                )
                + "."
            )

    # --------------------------------------------------------
    # 10) RECOMENDACIONES PARA CURSOS NO CONVALIDADOS
    # --------------------------------------------------------

    recomendaciones_caso_especial = []

    if (
        es_ingenieria_civil
        or es_ingenieria_industrial
    ):

        destinos_con_equivalencia_real = {
            normalizar(
                item.get(
                    "curso_destino",
                    ""
                )
            )
            for item in convalidaciones
            if (
                isinstance(
                    item,
                    dict
                )
                and item.get(
                    "curso_destino"
                )
                and item.get(
                    "curso_origen"
                )
            )
        }

        cursos_sin_equivalencia_real = [
            item.get(
                "curso",
                ""
            )
            for item in estructura_proforma
            if (
                isinstance(
                    item,
                    dict
                )
                and item.get(
                    "curso"
                )
                and normalizar(
                    item.get(
                        "curso",
                        ""
                    )
                ) not in destinos_con_equivalencia_real
            )
        ]

        cursos_sin_equivalencia_real = lista_unica(
            cursos_sin_equivalencia_real
        )

        if es_ingenieria_civil:

            recomendaciones_caso_especial = (
                recomendar_cursos_no_convalidables_civil(
                    cursos_alumno=cursos_alumno,
                    cursos_pendientes=(
                        cursos_sin_equivalencia_real
                    ),
                    convalidaciones_actuales=convalidaciones
                )
            )

        else:

            recomendaciones_caso_especial = (
                recomendar_cursos_no_convalidables_industrial(
                    cursos_alumno=cursos_alumno,
                    cursos_pendientes=(
                        cursos_sin_equivalencia_real
                    ),
                    convalidaciones_actuales=convalidaciones,
                    reglas=reglas
                )
            )

    return {
        "convalidaciones":
            convalidaciones,
        "pendientes":
            pendientes,
        "suficiencias":
            suficiencias,
        "competencias":
            competencias,
        "cursos_no_utilizados":
            cursos_no_utilizados,
        "cursos_proforma":
            cursos_proforma,
        "estructura_proforma":
            estructura_proforma,
        "caso_especial":
            caso_especial,
        "cantidad_suficiencias":
            len(
                suficiencias
            ),
        "maximo_suficiencias":
            maximo_suficiencias_carrera,
        "umbral_caso_especial":
            umbral_caso_especial,
        "maximo_suficiencias_final":
            maximo_suficiencias_final,
        "revision_especial_civil_realizada":
            (
                revision_especial_realizada
                and es_ingenieria_civil
            ),
        "revision_especial_industrial_realizada":
            (
                revision_especial_realizada
                and es_ingenieria_industrial
            ),
        "revision_especial_realizada":
            revision_especial_realizada,
        "cantidad_suficiencias_iniciales":
            len(suficiencias_iniciales),
        "suficiencias_iniciales":
            suficiencias_iniciales,
        "equivalencias_nuevas_revision_especial":
            equivalencias_nuevas_revision,
        "suficiencias_post_revision_completas":
            suficiencias_post_revision_completas,
        "cantidad_suficiencias_post_revision":
            len(suficiencias_post_revision_completas),
        "suficiencias_excedentes_revision":
            suficiencias_excedentes_revision,
        "recomendaciones_caso_especial":
            recomendaciones_caso_especial,
        "reglas_carrera":
            reglas,
        "revision_manual_asistida":
            bool(
                reglas.get(
                    "revision_manual_asistida",
                    False
                )
            ),
        "autoseleccionar_recomendaciones":
            bool(
                reglas.get(
                    "autoseleccionar_recomendaciones",
                    False
                )
            ),
        "observacion_caso_especial":
            observacion_caso_especial,
        "ruta_formato":
            ruta_formato,
        "cantidad_directas":
            len(
                directas
            ),
        "cantidad_cercanas":
            len(
                cercanas
            ),
        "cantidad_respaldo":
            len(
                respaldo
            ),
        "cantidad_ia":
            len(
                equivalencias_ia
            ),
        "cantidad_convalidaciones_base":
            len(
                convalidaciones_base
            ),
        "convalidaciones_base_con_notas":
            [
                {
                    "curso_destino":
                        item.get(
                            "curso_destino",
                            ""
                        ),
                    "curso_origen":
                        item.get(
                            "curso_origen",
                            ""
                        ),
                    "nota":
                        item.get(
                            "nota",
                            ""
                        )
                }
                for item in convalidaciones_base
            ],
        "equivalencias_sin_nota_real":
            [
                {
                    "curso_destino":
                        item.get(
                            "curso_destino",
                            ""
                        ),
                    "curso_origen":
                        item.get(
                            "curso_origen",
                            ""
                        )
                }
                for item in convalidaciones_base
                if obtener_nota_real(
                    item
                ) == ""
            ],
        "cursos_certificado_recibidos":
            [
                {
                    "curso":
                        item.get(
                            "curso",
                            ""
                        ),
                    "nota":
                        item.get(
                            "nota",
                            None
                        ),
                    "creditos":
                        item.get(
                            "creditos",
                            ""
                        )
                }
                for item in cursos_alumno
            ]
    }



# ============================================================
# VALIDAR NOMBRE REAL DE ASIGNATURA
# ============================================================

def es_nombre_curso_valido(texto):
    """
    Un curso debe ser un nombre textual académico.
    Nunca puede ser una nota, crédito, código, ciclo, año,
    número aislado, encabezado o total.
    """
    if texto is None:
        return False

    original = str(texto).strip()
    if not original:
        return False

    normal = normalizar(original)
    if not normal:
        return False

    # Números aislados / notas / créditos / promedios
    if re.fullmatch(r"\s*\d+(?:[.,]\d+)?\s*", original):
        return False

    # Años, ciclos o periodos tipo 1994B, 2016-1, etc.
    if re.fullmatch(r"(19|20)\d{2}\s*[A-Z0-9\-]*", normal):
        return False

    # Números romanos solos
    if normal in {"I","II","III","IV","V","VI","VII","VIII","IX","X"}:
        return False

    invalidos_exactos = {
        "ASIGNATURA", "ASIGNATURAS", "CURSO", "CURSOS",
        "MATERIA", "MATERIAS", "CODIGO", "COD",
        "CREDITO", "CREDITOS", "NOTA", "NOTA PARCIAL",
        "NOTA CONVALIDANTE", "V B", "VB", "CICLO",
        "SEMESTRE", "COMPETENCIA", "COMPETENCIAS",
        "N", "NRO", "NUMERO", "TOTAL", "TOTAL CREDITOS",
        "TOTAL DE CREDITOS", "PROMEDIO", "PROMEDIO PONDERADO",
        "APROBADO", "DESAPROBADO"
    }
    if normal in invalidos_exactos:
        return False

    invalidos_contenidos = [
        "TOTAL DE CREDITOS",
        "TOTAL CREDITOS",
        "PROMEDIO PONDERADO",
        "ASIGNATURA CONVALIDANTE",
        "ASIGANTURA CONVALIDANTE",
        "NOTA PARCIAL",
        "NOTA CONVALIDANTE"
    ]
    if any(frase in normal for frase in invalidos_contenidos):
        return False

    # Códigos académicos aislados como PS101, MAT203, G01
    if (
        len(normal) <= 12
        and re.fullmatch(r"[A-Z]{0,5}\d+[A-Z0-9\-]*", normal)
    ):
        return False

    # Debe contener letras reales
    cantidad_letras = sum(c.isalpha() for c in original)
    if cantidad_letras < 2:
        return False

    palabras = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", original)
    if not palabras:
        return False

    if len(palabras) == 1 and len(palabras[0]) < 2:
        return False

    return True


def filtrar_estructura_proforma(estructura):
    """
    Segunda barrera de seguridad:
    solo conserva filas cuyo campo 'curso' sea realmente
    un nombre de asignatura.
    """
    resultado = []
    vistos = set()

    for item in estructura or []:
        if not isinstance(item, dict):
            continue

        curso = str(item.get("curso", "") or "").strip()
        if not es_nombre_curso_valido(curso):
            continue

        clave = (
            normalizar(item.get("competencia", "")),
            normalizar(item.get("codigo", "")),
            normalizar(curso),
        )

        if clave in vistos:
            continue

        vistos.add(clave)
        resultado.append(item)

    return resultado


def filtrar_lista_suficiencias(cursos):
    """
    Última barrera antes de mostrar/generar suficiencias.
    Nunca deja pasar notas, créditos, códigos ni números aislados.
    """
    resultado = []
    vistos = set()

    for curso in cursos or []:
        curso = str(curso or "").strip()

        if not es_nombre_curso_valido(curso):
            continue

        clave = normalizar(curso)
        if clave in vistos:
            continue

        vistos.add(clave)
        resultado.append(curso)

    return resultado


# ============================================================
# LEER PROFORMA - DETECCIÓN ROBUSTA
# ============================================================

def detectar_columnas_proforma(
    tabla,
    reglas=None
):
    """
    Detecta columnas incluso si los encabezados están partidos
    entre varias filas o existen celdas combinadas.
    """

    reglas = reglas or REGLAS_GENERALES

    if not tabla.rows:
        return None

    filas_revision = min(
        6,
        len(
            tabla.rows
        )
    )

    max_columnas = max(
        len(
            tabla.rows[i].cells
        )
        for i in range(
            filas_revision
        )
    )

    textos_columnas = []

    for col in range(
        max_columnas
    ):

        partes = []

        for fila_idx in range(
            filas_revision
        ):

            fila = tabla.rows[
                fila_idx
            ]

            if col < len(
                fila.cells
            ):

                texto = normalizar(
                    fila.cells[
                        col
                    ].text
                )

                if texto:
                    partes.append(
                        texto
                    )

        textos_columnas.append(
            " ".join(
                partes
            )
        )

    columnas = {
        "fila_encabezado":
            0,
        "competencia":
            None,
        "ciclo":
            None,
        "codigo":
            None,
        "asignatura":
            None,
        "creditos":
            None,
        "convalidante":
            None,
        "nota_parcial":
            None,
        "nota_convalidante":
            None
    }

    for i, texto in enumerate(
        textos_columnas
    ):

        if (
            "ASIGNATURA CONVALIDANTE" in texto
            or "ASIGANTURA CONVALIDANTE" in texto
            or (
                "CONVALIDANTE" in texto
                and "NOTA" not in texto
            )
        ):
            columnas[
                "convalidante"
            ] = i
            continue

        if (
            "NOTA PARCIAL" in texto
            or (
                "NOTA" in texto
                and "PARCIAL" in texto
            )
        ):
            columnas[
                "nota_parcial"
            ] = i
            continue

        if (
            "NOTA CONVALIDANTE" in texto
            or (
                "NOTA" in texto
                and "CONVALIDANTE" in texto
            )
        ):
            columnas[
                "nota_convalidante"
            ] = i
            continue

        if (
            "CONVALIDANTE" not in texto
            and (
                texto == "ASIGNATURA"
                or texto == "ASIGNATURAS"
                or "ASIGNATURA UPRIT" in texto
                or "ASIGNATURA A CONVALIDAR" in texto
            )
        ):
            columnas[
                "asignatura"
            ] = i
            continue

        if (
            texto == "CODIGO"
            or texto == "COD"
            or "CODIGO DE ASIGNATURA" in texto
        ):
            columnas[
                "codigo"
            ] = i
            continue

        if (
            texto == "CREDITO"
            or texto == "CREDITOS"
            or "CREDITO ACADEMICO" in texto
            or "CREDITOS ACADEMICOS" in texto
        ):
            columnas[
                "creditos"
            ] = i
            continue

        if (
            texto == "CICLO"
            or texto == "SEMESTRE"
        ):
            columnas[
                "ciclo"
            ] = i

    # --------------------------------------------------------
    # SEGUNDO INTENTO POR CELDA
    # --------------------------------------------------------

    for fila_idx in range(
        filas_revision
    ):

        fila = tabla.rows[
            fila_idx
        ]

        for i, celda in enumerate(
            fila.cells
        ):

            texto = normalizar(
                celda.text
            )

            if not texto:
                continue

            if (
                columnas[
                    "convalidante"
                ] is None
                and (
                    "ASIGNATURA CONVALIDANTE" in texto
                    or "ASIGANTURA CONVALIDANTE" in texto
                )
            ):
                columnas[
                    "convalidante"
                ] = i

            elif (
                columnas[
                    "nota_parcial"
                ] is None
                and "NOTA PARCIAL" in texto
            ):
                columnas[
                    "nota_parcial"
                ] = i

            elif (
                columnas[
                    "nota_convalidante"
                ] is None
                and "NOTA CONVALIDANTE" in texto
            ):
                columnas[
                    "nota_convalidante"
                ] = i

            elif (
                columnas[
                    "asignatura"
                ] is None
                and "CONVALIDANTE" not in texto
                and texto in (
                    "ASIGNATURA",
                    "ASIGNATURAS"
                )
            ):
                columnas[
                    "asignatura"
                ] = i

                columnas[
                    "fila_encabezado"
                ] = fila_idx

            elif (
                columnas[
                    "codigo"
                ] is None
                and texto in (
                    "CODIGO",
                    "COD"
                )
            ):
                columnas[
                    "codigo"
                ] = i

            elif (
                columnas[
                    "creditos"
                ] is None
                and texto in (
                    "CREDITO",
                    "CREDITOS"
                )
            ):
                columnas[
                    "creditos"
                ] = i

            elif (
                columnas[
                    "ciclo"
                ] is None
                and texto in (
                    "CICLO",
                    "SEMESTRE"
                )
            ):
                columnas[
                    "ciclo"
                ] = i

    if columnas[
        "asignatura"
    ] is None:
        return None

    # --------------------------------------------------------
    # COMPETENCIA
    # --------------------------------------------------------

    if (
        columnas[
            "ciclo"
        ] is not None
        and columnas[
            "ciclo"
        ] > 0
    ):
        columnas[
            "competencia"
        ] = (
            columnas[
                "ciclo"
            ] - 1
        )

    elif (
        columnas[
            "codigo"
        ] is not None
        and columnas[
            "codigo"
        ] > 0
    ):
        columnas[
            "competencia"
        ] = (
            columnas[
                "codigo"
            ] - 1
        )

    # Solo para carreras cuya configuración lo autorice.
    # Ingeniería Civil utiliza una proforma donde la competencia
    # específica está inmediatamente a la izquierda de ASIGNATURA.
    elif (
        reglas.get(
            "detectar_competencia_a_la_izquierda_de_asignatura",
            False
        )
        and columnas[
            "asignatura"
        ] is not None
        and columnas[
            "asignatura"
        ] > 0
    ):
        columnas[
            "competencia"
        ] = (
            columnas[
                "asignatura"
            ] - 1
        )

    return columnas


def leer_estructura_proforma(
    ruta_formato="formato.docx",
    reglas=None
):
    """
    Extrae cursos, competencia, código, ciclo y créditos.
    """

    documento = Document(
        ruta_formato
    )

    estructura = []

    for tabla in documento.tables:

        if not tabla.rows:
            continue

        columnas = detectar_columnas_proforma(
            tabla=tabla,
            reglas=reglas
        )

        if not columnas:
            continue

        inicio_datos = (
            columnas[
                "fila_encabezado"
            ]
            + 1
        )

        ultima_competencia = ""
        vistos = set()

        for fila in tabla.rows[
            inicio_datos:
        ]:

            cells = fila.cells

            idx_asignatura = columnas[
                "asignatura"
            ]

            if len(
                cells
            ) <= idx_asignatura:
                continue

            curso = cells[
                idx_asignatura
            ].text.strip()

            curso_normal = normalizar(
                curso
            )

            if not curso_normal:
                continue

            if not es_nombre_curso_valido(
                curso
            ):
                continue

            if (
                "TOTAL DE CREDITOS" in curso_normal
                or "TOTAL CREDITOS" in curso_normal
                or curso_normal in (
                    "ASIGNATURA",
                    "ASIGNATURAS"
                )
            ):
                continue

            competencia = ""

            idx_competencia = columnas.get(
                "competencia"
            )

            if (
                idx_competencia is not None
                and idx_competencia < len(
                    cells
                )
            ):
                competencia = cells[
                    idx_competencia
                ].text.strip()

            if competencia:
                ultima_competencia = competencia
            else:
                competencia = ultima_competencia

            ciclo = obtener_texto_columna(
                cells,
                columnas.get(
                    "ciclo"
                )
            )

            codigo = obtener_texto_columna(
                cells,
                columnas.get(
                    "codigo"
                )
            )

            creditos = obtener_texto_columna(
                cells,
                columnas.get(
                    "creditos"
                )
            )

            clave = (
                normalizar(
                    competencia
                ),
                normalizar(
                    codigo
                ),
                curso_normal
            )

            if clave in vistos:
                continue

            vistos.add(
                clave
            )

            estructura.append({
                "competencia":
                    competencia,
                "ciclo":
                    ciclo,
                "codigo":
                    codigo,
                "curso":
                    curso,
                "creditos":
                    creditos
            })

        if estructura:
            break

    if not estructura:

        diagnostico = []

        for numero, tabla in enumerate(
            documento.tables
        ):

            encabezado = normalizar(
                " ".join(
                    celda.text
                    for fila in tabla.rows[:5]
                    for celda in fila.cells
                )
            )

            diagnostico.append(
                f"Tabla {numero}: "
                f"{encabezado[:160]}"
            )

        raise ValueError(
            "No se pudieron leer las asignaturas de la proforma. "
            + " | ".join(
                diagnostico
            )
        )

    return estructura


def obtener_texto_columna(
    cells,
    indice
):
    if indice is None:
        return ""

    if indice >= len(
        cells
    ):
        return ""

    return cells[
        indice
    ].text.strip()


# ============================================================
# COINCIDENCIAS EXACTAS
# ============================================================

def buscar_coincidencias_exactas(
    cursos_alumno,
    estructura_proforma
):

    resultado = []
    usados_origen = set()
    usados_destino = set()

    mapa_origen = defaultdict(
        list
    )

    for item in cursos_alumno:

        nombre = item.get(
            "curso",
            ""
        )

        if nombre:
            mapa_origen[
                normalizar(
                    nombre
                )
            ].append(
                item
            )

    for destino in estructura_proforma:

        curso_destino = destino[
            "curso"
        ]

        destino_normal = normalizar(
            curso_destino
        )

        for candidato in mapa_origen.get(
            destino_normal,
            []
        ):

            origen_real = candidato.get(
                "curso",
                ""
            )

            origen_normal = normalizar(
                origen_real
            )

            if origen_normal in usados_origen:
                continue

            if destino_normal in usados_destino:
                continue

            if son_areas_incompatibles(
                origen_real,
                curso_destino
            ):
                continue

            resultado.append(
                crear_equivalencia(
                    destino_info=destino,
                    origen_info=candidato,
                    afinidad="MUY ALTA",
                    tipo="COINCIDENCIA EXACTA",
                    requiere_validacion=False,
                    justificacion=(
                        "Coincidencia directa por nombre de asignatura."
                    )
                )
            )

            usados_origen.add(
                origen_normal
            )

            usados_destino.add(
                destino_normal
            )

            break

    return resultado


# ============================================================
# COINCIDENCIAS CERCANAS
# ============================================================

def buscar_coincidencias_cercanas(
    cursos_alumno,
    estructura_proforma,
    usados_origen=None,
    usados_destino=None
):

    usados_origen = set(
        usados_origen
        or []
    )

    usados_destino = set(
        usados_destino
        or []
    )

    resultado = []

    for destino in estructura_proforma:

        destino_real = destino.get(
            "curso",
            ""
        )

        destino_normal = normalizar(
            destino_real
        )

        if destino_normal in usados_destino:
            continue

        candidatos = []

        for origen_info in cursos_alumno:

            origen_real = origen_info.get(
                "curso",
                ""
            )

            origen_normal = normalizar(
                origen_real
            )

            if origen_normal in usados_origen:
                continue

            if son_areas_incompatibles(
                origen_real,
                destino_real
            ):
                continue

            puntaje = max(
                fuzz.ratio(
                    origen_normal,
                    destino_normal
                ),
                fuzz.token_sort_ratio(
                    origen_normal,
                    destino_normal
                )
            )

            if puntaje >= 90:

                candidatos.append(
                    (
                        puntaje,
                        origen_info
                    )
                )

        if not candidatos:
            continue

        candidatos.sort(
            key=lambda x: x[0],
            reverse=True
        )

        puntaje, origen_info = candidatos[
            0
        ]

        resultado.append(
            crear_equivalencia(
                destino_info=destino,
                origen_info=origen_info,
                afinidad="ALTA",
                tipo="COINCIDENCIA POR NOMBRE",
                requiere_validacion=False,
                justificacion=(
                    f"Los nombres de las asignaturas presentan "
                    f"una similitud académica alta ({round(puntaje, 1)}%)."
                )
            )
        )

        usados_origen.add(
            normalizar(
                origen_info.get(
                    "curso",
                    ""
                )
            )
        )

        usados_destino.add(
            destino_normal
        )

    return resultado


# ============================================================
# RESPALDO DETERMINÍSTICO
# ============================================================

EQUIVALENCIAS_RESPALDO = {

    "COMUNICACION": [
        "LENGUAJE",
        "LENGUAJE Y COMUNICACION",
        "COMUNICACION ORAL Y ESCRITA",
        "EXPRESION ORAL Y ESCRITA",
        "REDACCION",
        "REDACCION UNIVERSITARIA",
        "COMPRENSION Y PRODUCCION DE TEXTOS",
        "COMPETENCIAS COMUNICATIVAS"
    ],

    "TALLER DE EXPRESION ESCRITA": [
        "REDACCION",
        "REDACCION UNIVERSITARIA",
        "REDACCION ACADEMICA",
        "REDACCION Y TECNICAS DE LECTURA",
        "EXPRESION ESCRITA",
        "TECNICAS DE LECTURA Y REDACCION"
    ],

    "REALIDAD NACIONAL Y DERECHOS HUMANOS": [
        "REALIDAD NACIONAL",
        "REALIDAD PERUANA",
        "DERECHOS HUMANOS",
        "CONSTITUCION Y DERECHOS HUMANOS",
        "CONSTITUCION POLITICA Y DERECHOS HUMANOS",
        "EDUCACION CIVICA",
        "FORMACION CIUDADANA"
    ],

    "ESTADISTICA Y PROBABILIDADES": [
        "ESTADISTICA",
        "ESTADISTICA GENERAL",
        "ESTADISTICA APLICADA",
        "ESTADISTICA DESCRIPTIVA",
        "PROBABILIDAD Y ESTADISTICA",
        "METODOS ESTADISTICOS"
    ],

    "FUNDAMENTOS DE LA ADMINISTRACION": [
        "ADMINISTRACION",
        "ADMINISTRACION GENERAL",
        "FUNDAMENTOS DE ADMINISTRACION",
        "PRINCIPIOS DE ADMINISTRACION",
        "TEORIA GENERAL DE LA ADMINISTRACION"
    ],

    "ETICA Y RESPONSABILIDAD PROFESIONAL": [
        "ETICA",
        "ETICA PROFESIONAL",
        "ETICA Y DEONTOLOGIA",
        "DEONTOLOGIA",
        "DEONTOLOGIA PROFESIONAL",
        "ETICA Y RESPONSABILIDAD SOCIAL"
    ],

    "MATEMATICA BASICA": [
        "MATEMATICA",
        "MATEMATICA GENERAL",
        "MATEMATICA I",
        "MATEMATICAS BASICAS"
    ],

    "MATEMATICA FINANCIERA": [
        "MATEMATICA FINANCIERA",
        "MATEMATICAS FINANCIERAS"
    ],

    "LOGICA GENERAL": [
        "LOGICA",
        "LOGICA MATEMATICA",
        "LOGICA Y PENSAMIENTO CRITICO"
    ],

    "METODOLOGIA DE LA INVESTIGACION CIENTIFICA": [
        "METODOLOGIA DE LA INVESTIGACION",
        "METODOLOGIA DE INVESTIGACION",
        "INVESTIGACION CIENTIFICA",
        "METODOS DE INVESTIGACION",
        "SEMINARIO DE INVESTIGACION"
    ],

    "PSICOLOGIA GENERAL": [
        "INTRODUCCION A LA PSICOLOGIA",
        "FUNDAMENTOS DE PSICOLOGIA",
        "BASES DE LA PSICOLOGIA"
    ],

    "PSICOLOGIA DEL DESARROLLO": [
        "PSICOLOGIA EVOLUTIVA",
        "DESARROLLO HUMANO",
        "DESARROLLO PSICOLOGICO",
        "CICLO VITAL"
    ],

    "PSICOLOGIA DEL DESARROLLO I": [
        "PSICOLOGIA EVOLUTIVA I",
        "DESARROLLO HUMANO I",
        "DESARROLLO PSICOLOGICO I"
    ],

    "PSICOLOGIA DEL DESARROLLO II": [
        "PSICOLOGIA EVOLUTIVA II",
        "DESARROLLO HUMANO II",
        "DESARROLLO PSICOLOGICO II"
    ],

    "PSICOMETRIA": [
        "MEDICION PSICOLOGICA",
        "TEORIA DE LOS TESTS",
        "CONSTRUCCION DE PRUEBAS",
        "EVALUACION PSICOMETRICA"
    ],

    "PSICOPATOLOGIA": [
        "PSICOLOGIA ANORMAL",
        "TRASTORNOS PSICOLOGICOS",
        "PSICOPATOLOGIA GENERAL"
    ],

    "PSICOLOGIA SOCIAL": [
        "COMPORTAMIENTO SOCIAL",
        "PROCESOS PSICOSOCIALES",
        "PSICOLOGIA DE GRUPOS"
    ],

    "PSICOLOGIA Y SOCIEDAD": [
        "PSICOLOGIA SOCIAL",
        "PROCESOS PSICOSOCIALES",
        "COMPORTAMIENTO SOCIAL"
    ],

    "PSICOLOGIA ORGANIZACIONAL": [
        "PSICOLOGIA DEL TRABAJO",
        "PSICOLOGIA LABORAL",
        "COMPORTAMIENTO ORGANIZACIONAL"
    ],

    "PSICOLOGIA DE LAS ORGANIZACIONES": [
        "PSICOLOGIA DEL TRABAJO",
        "PSICOLOGIA LABORAL",
        "PSICOLOGIA ORGANIZACIONAL",
        "COMPORTAMIENTO ORGANIZACIONAL"
    ],

    "PSICOLOGIA EDUCATIVA": [
        "PSICOLOGIA DEL APRENDIZAJE",
        "PSICOLOGIA ESCOLAR",
        "ORIENTACION EDUCATIVA"
    ],

    "PROCESOS DE APRENDIZAJE": [
        "PSICOLOGIA DEL APRENDIZAJE",
        "TEORIAS DEL APRENDIZAJE",
        "APRENDIZAJE"
    ],

    "ANALISIS DE DATOS": [
        "ANALISIS ESTADISTICO",
        "PROCESAMIENTO DE DATOS",
        "ESTADISTICA APLICADA"
    ],

    "LIDERAZGO TRANSFORMACIONAL": [
        "LIDERAZGO",
        "LIDERAZGO Y GESTION",
        "HABILIDADES DIRECTIVAS"
    ],

    "FISICA I": [
        "FISICA",
        "FISICA GENERAL",
        "FISICA GENERAL I",
        "FISICA BASICA"
    ],

    "FISICA II": [
        "FISICA II",
        "FISICA GENERAL II"
    ],

    "CONTABILIDAD BASICA": [
        "CONTABILIDAD",
        "CONTABILIDAD GENERAL",
        "FUNDAMENTOS DE CONTABILIDAD"
    ],

    "DIBUJO EN INGENIERIA": [
        "DIBUJO TECNICO",
        "DIBUJO TECNICO INDUSTRIAL",
        "DIBUJO DE INGENIERIA"
    ],

    "ECOLOGIA E IMPACTO AMBIENTAL": [
        "ECOLOGIA",
        "MEDIO AMBIENTE",
        "GESTION AMBIENTAL",
        "IMPACTO AMBIENTAL"
    ],

    "QUIMICA GENERAL": [
        "QUIMICA",
        "QUIMICA I",
        "QUIMICA BASICA"
    ],

    "FUNDAMENTOS DE PROGRAMACION": [
        "PROGRAMACION",
        "PROGRAMACION I",
        "INTRODUCCION A LA PROGRAMACION",
        "ALGORITMOS Y PROGRAMACION"
    ],

    "REDES Y SISTEMAS OPERATIVOS": [
        "REDES DE COMPUTADORAS",
        "REDES INFORMATICAS",
        "SISTEMAS OPERATIVOS",
        "REDES Y COMUNICACIONES"
    ]
}


def buscar_equivalencias_respaldo(
    cursos_alumno,
    estructura_proforma,
    usados_origen=None,
    usados_destino=None,
    reglas=None
):

    usados_origen = set(
        usados_origen
        or []
    )

    usados_destino = set(
        usados_destino
        or []
    )

    resultado = []

    mapa_alias = {}

    # Equivalencias generales del motor.
    equivalencias_combinadas = dict(
        EQUIVALENCIAS_RESPALDO
    )

    # Equivalencias específicas de la carrera.
    reglas = reglas or {}

    equivalencias_carrera = reglas.get(
        "equivalencias_orientativas",
        {}
    )

    if isinstance(
        equivalencias_carrera,
        dict
    ):
        for destino, alias in equivalencias_carrera.items():
            equivalencias_combinadas[
                destino
            ] = list(
                alias
                if isinstance(
                    alias,
                    (list, tuple, set)
                )
                else [alias]
            )

    for destino, alias in equivalencias_combinadas.items():

        destino_n = normalizar(
            destino
        )

        mapa_alias[
            destino_n
        ] = {
            normalizar(
                item
            )
            for item in alias
        }

        mapa_alias[
            destino_n
        ].add(
            destino_n
        )

    for destino in estructura_proforma:

        destino_real = destino.get(
            "curso",
            ""
        )

        destino_n = normalizar(
            destino_real
        )

        if destino_n in usados_destino:
            continue

        alias_destino = mapa_alias.get(
            destino_n
        )

        if not alias_destino:
            continue

        candidatos = []

        for origen_info in cursos_alumno:

            origen_real = origen_info.get(
                "curso",
                ""
            )

            origen_n = normalizar(
                origen_real
            )

            if origen_n in usados_origen:
                continue

            if son_areas_incompatibles(
                origen_real,
                destino_real
            ):
                continue

            if origen_n in alias_destino:

                candidatos.append(
                    origen_info
                )

        if not candidatos:
            continue

        origen_info = candidatos[
            0
        ]

        resultado.append(
            crear_equivalencia(
                destino_info=destino,
                origen_info=origen_info,
                afinidad="ALTA",
                tipo="EQUIVALENCIA DE RESPALDO",
                requiere_validacion=True,
                justificacion=(
                    "La asignatura de procedencia pertenece a una "
                    "denominación académicamente compatible con la "
                    "asignatura UPRIT. Se recomienda validación "
                    "académica de contenidos y/o sílabo."
                )
            )
        )

        usados_origen.add(
            normalizar(
                origen_info.get(
                    "curso",
                    ""
                )
            )
        )

        usados_destino.add(
            destino_n
        )

    return resultado


# ============================================================
# REVISIÓN ESPECIALISTA - INGENIERÍA CIVIL
# ============================================================

def reevaluar_caso_especial_ingenieria_civil(
    cursos_alumno,
    estructura_proforma,
    convalidaciones_actuales,
    competencias_actuales,
    suficiencias_actuales
):
    """
    Segunda revisión académica exclusiva para casos especiales
    de Ingeniería Civil.

    Busca equivalencias adicionales reales entre cursos todavía
    disponibles. No inventa notas ni cursos y no reemplaza
    equivalencias ya aceptadas.
    """

    usados_origen = {
        normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_origen"
        )
    }

    usados_destino = {
        normalizar(
            item.get(
                "curso_destino",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_destino"
        )
    }

    cursos_disponibles = [
        item
        for item in cursos_alumno or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in usados_origen
        )
    ]

    destinos_disponibles = [
        item
        for item in estructura_proforma or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in usados_destino
        )
    ]

    if (
        not cursos_disponibles
        or not destinos_disponibles
    ):
        return []

    prompt_sistema = """
Eres un especialista universitario senior en INGENIERÍA CIVIL y en
convalidaciones académicas por COMPETENCIAS.

Realizas una SEGUNDA REVISIÓN de un expediente que superó el umbral
ordinario de exámenes de suficiencia.

Revisa con mayor profundidad las posibles equivalencias entre los cursos
REALES del certificado todavía disponibles y los cursos REALES de la
proforma todavía pendientes.

ÁREAS DE INGENIERÍA CIVIL A CONSIDERAR:
- matemática básica, cálculo, análisis matemático, álgebra, geometría;
- física, química, estadística;
- dibujo técnico, dibujo de ingeniería, CAD, geometría descriptiva;
- materiales, construcción, tecnología del concreto;
- estática, dinámica, resistencia de materiales, estructuras;
- geología, mecánica de suelos, geotecnia;
- fluidos, hidráulica, hidrología;
- topografía, caminos y transportes;
- gestión y formación general cuando exista correspondencia clara.

REGLA DE COMPETENCIAS:
- si una competencia tiene varios cursos y falta SOLO 1, ese único
  faltante no debe generar por sí solo una suficiencia;
- si faltan 2 o más, sí pueden quedar como suficiencia.

REGLAS OBLIGATORIAS:
1. Usa únicamente cursos presentes en las listas entregadas.
2. No inventes cursos.
3. No devuelvas notas.
4. No inventes sílabos ni contenidos no disponibles.
5. Un curso del certificado puede utilizarse máximo una vez.
6. Un curso UPRIT puede recibir máximo una equivalencia.
7. No propongas equivalencias falsas para reducir suficiencias.
8. Educación Física no equivale a Física.
9. Cálculo de Costos no equivale a Cálculo matemático.
10. Programación Neurolingüística no equivale a Programación informática.
11. Redes Sociales no equivale a Redes informáticas.
12. Si la relación académica no es defendible, no la propongas.

Devuelve exclusivamente JSON válido.
"""

    prompt_usuario = f"""
CARRERA DESTINO:
INGENIERÍA CIVIL

TODOS LOS CURSOS REALES DEL CERTIFICADO:
{json.dumps(cursos_alumno, ensure_ascii=False, indent=2)}

CURSOS DEL CERTIFICADO TODAVÍA DISPONIBLES:
{json.dumps(cursos_disponibles, ensure_ascii=False, indent=2)}

TODOS LOS CURSOS DE LA PROFORMA:
{json.dumps(estructura_proforma, ensure_ascii=False, indent=2)}

CURSOS UPRIT TODAVÍA DISPONIBLES:
{json.dumps(destinos_disponibles, ensure_ascii=False, indent=2)}

COMPETENCIAS ACTUALES:
{json.dumps(competencias_actuales, ensure_ascii=False, indent=2)}

SUFICIENCIAS ANTES DE LA SEGUNDA REVISIÓN:
{json.dumps(suficiencias_actuales, ensure_ascii=False, indent=2)}

Devuelve exactamente:

{{
  "equivalencias": [
    {{
      "curso_origen": "",
      "curso_destino": "",
      "nivel_afinidad": "ALTA",
      "requiere_validacion": false,
      "justificacion": ""
    }}
  ]
}}
"""

    try:

        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": prompt_usuario
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=0
        )

        contenido = (
            respuesta
            .choices[0]
            .message
            .content
        )

        if not contenido:
            return []

        datos = json.loads(
            contenido
        )

        propuesta = datos.get(
            "equivalencias",
            []
        )

        if not isinstance(
            propuesta,
            list
        ):
            return []

        return validar_equivalencias(
            propuesta=propuesta,
            cursos_alumno=cursos_disponibles,
            estructura_proforma=destinos_disponibles
        )

    except Exception:
        return []


# ============================================================
# SEGUNDA REVISIÓN ESPECIALISTA - INGENIERÍA INDUSTRIAL
# ============================================================

def reevaluar_caso_especial_ingenieria_industrial(
    cursos_alumno,
    estructura_proforma,
    convalidaciones_actuales,
    competencias_actuales,
    suficiencias_actuales,
    reglas=None
):
    """
    Segunda revisión académica exclusiva para casos especiales
    de Ingeniería Industrial.

    Revisa únicamente cursos todavía disponibles y nunca
    reemplaza equivalencias ya aceptadas.
    """

    reglas = reglas or {}

    usados_origen = {
        normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_origen"
        )
    }

    usados_destino = {
        normalizar(
            item.get(
                "curso_destino",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_destino"
        )
    }

    cursos_disponibles = [
        item
        for item in cursos_alumno or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in usados_origen
        )
    ]

    destinos_disponibles = [
        item
        for item in estructura_proforma or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in usados_destino
        )
    ]

    if (
        not cursos_disponibles
        or not destinos_disponibles
    ):
        return []

    instrucciones = str(
        reglas.get(
            "instrucciones_especialista",
            ""
        )
        or ""
    ).strip()

    prompt_sistema = f"""
Eres un especialista universitario senior en INGENIERÍA INDUSTRIAL
y en convalidaciones académicas por COMPETENCIAS.

Realizas una SEGUNDA REVISIÓN de un expediente que superó el
umbral ordinario de suficiencias.

Debes revisar con mayor profundidad las posibles equivalencias
entre los cursos REALES del certificado todavía disponibles y
los cursos REALES de la proforma todavía pendientes.

ÁREAS PRIORITARIAS:
- ingeniería de métodos, estudio del trabajo y productividad;
- investigación de operaciones, optimización y simulación;
- producción, planeamiento y control de la producción;
- gestión de operaciones;
- logística, inventarios, almacenes y cadena de suministro;
- calidad y control estadístico de procesos;
- seguridad y salud en el trabajo;
- ergonomía;
- mantenimiento;
- procesos industriales y manufactura;
- diseño y distribución de planta;
- costos industriales, contabilidad, economía y finanzas;
- administración y gestión de proyectos;
- matemática, física, química y estadística;
- sistemas de información, automatización y gestión ambiental.

REGLA DE COMPETENCIAS:
- si una competencia tiene varios cursos y falta SOLO 1, ese único
  faltante no debe generar por sí solo una suficiencia;
- si faltan 2 o más, sí pueden quedar como suficiencia.

REGLAS OBLIGATORIAS:
1. Usa únicamente cursos presentes en las listas entregadas.
2. No inventes cursos.
3. No devuelvas notas.
4. No inventes sílabos ni contenidos no disponibles.
5. Un curso del certificado puede utilizarse máximo una vez.
6. Un curso UPRIT puede recibir máximo una equivalencia.
7. No propongas equivalencias falsas para reducir suficiencias.
8. Educación Física no equivale a Física.
9. Cálculo de Costos no equivale a Cálculo matemático.
10. Programación Neurolingüística no equivale a Programación informática.
11. Redes Sociales no equivale a Redes informáticas.
12. Si la relación académica no es defendible, no la propongas.

{instrucciones}

Devuelve exclusivamente JSON válido.
"""

    prompt_usuario = f"""
CARRERA DESTINO:
INGENIERÍA INDUSTRIAL

TODOS LOS CURSOS REALES DEL CERTIFICADO:
{json.dumps(cursos_alumno, ensure_ascii=False, indent=2)}

CURSOS DEL CERTIFICADO TODAVÍA DISPONIBLES:
{json.dumps(cursos_disponibles, ensure_ascii=False, indent=2)}

TODOS LOS CURSOS DE LA PROFORMA:
{json.dumps(estructura_proforma, ensure_ascii=False, indent=2)}

CURSOS UPRIT TODAVÍA DISPONIBLES:
{json.dumps(destinos_disponibles, ensure_ascii=False, indent=2)}

COMPETENCIAS ACTUALES:
{json.dumps(competencias_actuales, ensure_ascii=False, indent=2)}

SUFICIENCIAS ANTES DE LA SEGUNDA REVISIÓN:
{json.dumps(suficiencias_actuales, ensure_ascii=False, indent=2)}

Devuelve exactamente:

{{
  "equivalencias": [
    {{
      "curso_origen": "",
      "curso_destino": "",
      "nivel_afinidad": "ALTA",
      "requiere_validacion": false,
      "justificacion": ""
    }}
  ]
}}
"""

    try:

        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": prompt_usuario
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=0
        )

        contenido = (
            respuesta
            .choices[0]
            .message
            .content
        )

        if not contenido:
            return []

        datos = json.loads(
            contenido
        )

        propuesta = datos.get(
            "equivalencias",
            []
        )

        if not isinstance(
            propuesta,
            list
        ):
            return []

        return validar_equivalencias(
            propuesta=propuesta,
            cursos_alumno=cursos_disponibles,
            estructura_proforma=destinos_disponibles
        )

    except Exception:
        return []


# ============================================================
# RECOMENDACIONES - INGENIERÍA INDUSTRIAL
# ============================================================

def recomendar_cursos_no_convalidables_industrial(
    cursos_alumno,
    cursos_pendientes,
    convalidaciones_actuales,
    reglas=None
):
    """
    Sugiere al coordinador el mejor curso REAL disponible del
    certificado para revisar un curso UPRIT aún no convalidado.

    No modifica automáticamente las convalidaciones.
    """

    reglas = reglas or {}

    if not cursos_pendientes:
        return []

    origenes_usados = {
        normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_origen"
        )
    }

    cursos_disponibles = [
        dict(
            item
        )
        for item in cursos_alumno or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in origenes_usados
        )
    ]

    if not cursos_disponibles:
        return [
            {
                "curso_destino": curso,
                "curso_sugerido": "",
                "nota": "",
                "afinidad": "SIN CANDIDATO",
                "recomendacion":
                    "Mantener pendiente o revisar sílabos.",
                "justificacion":
                    "No quedan cursos libres del certificado.",
                "requiere_silabo": True
            }
            for curso in cursos_pendientes
        ]

    instrucciones = str(
        reglas.get(
            "instrucciones_especialista",
            ""
        )
        or ""
    ).strip()

    prompt_sistema = f"""
Eres especialista académico universitario senior en
INGENIERÍA INDUSTRIAL y convalidación por competencias.

Debes recomendar, SOLO COMO APOYO AL COORDINADOR, qué curso REAL
del certificado todavía disponible es el mejor candidato para
revisar cada curso UPRIT pendiente.

Debes considerar áreas propias de Ingeniería Industrial:
métodos, trabajo, productividad, operaciones, producción,
investigación de operaciones, logística, calidad, seguridad,
ergonomía, mantenimiento, manufactura, planta, costos,
administración, matemática, física, química, estadística,
automatización, proyectos y gestión ambiental.

REGLAS:
1. Usa únicamente cursos entregados en la lista.
2. No inventes cursos ni notas.
3. Un curso del certificado puede sugerirse máximo una vez.
4. No fuerces equivalencias para reducir suficiencias.
5. Debes revisar TODOS los cursos disponibles antes de responder SIN CANDIDATO.
6. Si existe al menos una relación académica razonable, selecciona el mejor candidato disponible.
7. Si la relación es débil pero todavía defendible para revisión, marca afinidad BAJA.
8. Solo utiliza SIN CANDIDATO cuando ninguna alternativa sea académicamente defendible.
9. Afinidad: ALTA, MEDIA, BAJA o SIN CANDIDATO.
10. La recomendación no constituye aprobación automática.
11. Respeta las incompatibilidades académicas y nunca fuerces equivalencias.

{instrucciones}

Devuelve exclusivamente JSON válido.
"""

    prompt_usuario = f"""
CURSOS UPRIT TODAVÍA PENDIENTES:
{json.dumps(cursos_pendientes, ensure_ascii=False, indent=2)}

CURSOS REALES DEL CERTIFICADO TODAVÍA DISPONIBLES:
{json.dumps(cursos_disponibles, ensure_ascii=False, indent=2)}

Devuelve:

{{
  "recomendaciones": [
    {{
      "curso_destino": "",
      "curso_sugerido": "",
      "afinidad": "ALTA|MEDIA|BAJA|SIN CANDIDATO",
      "recomendacion": "",
      "justificacion": "",
      "requiere_silabo": true
    }}
  ]
}}
"""

    try:

        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": prompt_usuario
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=0
        )

        datos = json.loads(
            respuesta.choices[0].message.content
            or "{}"
        )

        propuestas = datos.get(
            "recomendaciones",
            []
        )

    except Exception:
        propuestas = []

    mapa_origen = {
        normalizar(
            item.get(
                "curso",
                ""
            )
        ): item
        for item in cursos_disponibles
        if item.get(
            "curso"
        )
    }

    mapa_destino = {
        normalizar(
            curso
        ): curso
        for curso in cursos_pendientes
    }

    origenes_recomendados = set()
    destinos_recomendados = set()
    salida = []

    for propuesta in propuestas:

        if not isinstance(
            propuesta,
            dict
        ):
            continue

        destino_norm = normalizar(
            propuesta.get(
                "curso_destino",
                ""
            )
        )

        if (
            destino_norm not in mapa_destino
            or destino_norm in destinos_recomendados
        ):
            continue

        sugerido_norm = normalizar(
            propuesta.get(
                "curso_sugerido",
                ""
            )
        )

        origen_real = mapa_origen.get(
            sugerido_norm
        )

        if (
            sugerido_norm
            and (
                origen_real is None
                or sugerido_norm in origenes_recomendados
            )
        ):
            origen_real = None
            sugerido_norm = ""

        afinidad = normalizar(
            propuesta.get(
                "afinidad",
                "SIN CANDIDATO"
            )
        )

        if afinidad not in {
            "ALTA",
            "MEDIA",
            "BAJA",
            "SIN CANDIDATO"
        }:
            afinidad = "MEDIA"

        nota_real = ""

        if origen_real:
            nota_real = obtener_nota_real(
                origen_real
            )

            origenes_recomendados.add(
                sugerido_norm
            )

        salida.append({
            "curso_destino":
                mapa_destino[
                    destino_norm
                ],
            "curso_sugerido":
                (
                    origen_real.get(
                        "curso",
                        ""
                    )
                    if origen_real
                    else ""
                ),
            "nota":
                nota_real,
            "afinidad":
                afinidad,
            "recomendacion":
                str(
                    propuesta.get(
                        "recomendacion",
                        ""
                    )
                    or ""
                ).strip(),
            "justificacion":
                str(
                    propuesta.get(
                        "justificacion",
                        ""
                    )
                    or ""
                ).strip(),
            "requiere_silabo":
                bool(
                    propuesta.get(
                        "requiere_silabo",
                        True
                    )
                )
        })

        destinos_recomendados.add(
            destino_norm
        )

    for curso in cursos_pendientes:

        if normalizar(
            curso
        ) in destinos_recomendados:
            continue

        salida.append({
            "curso_destino":
                curso,
            "curso_sugerido":
                "",
            "nota":
                "",
            "afinidad":
                "SIN CANDIDATO",
            "recomendacion":
                "Mantener pendiente o revisar sílabos.",
            "justificacion":
                "No se identificó una relación académica defendible.",
            "requiere_silabo":
                True
        })

    return salida


# ============================================================
# RECOMENDACIONES - INGENIERÍA CIVIL
# ============================================================

def recomendar_cursos_no_convalidables_civil(
    cursos_alumno,
    cursos_pendientes,
    convalidaciones_actuales
):
    """
    Sugiere al coordinador qué curso real del certificado podría
    revisarse para cada curso UPRIT todavía no convalidado.

    La sugerencia NO modifica automáticamente la convalidación.
    """

    if not cursos_pendientes:
        return []

    origenes_usados = {
        normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )
        for item in convalidaciones_actuales or []
        if item.get(
            "curso_origen"
        )
    }

    cursos_disponibles = [
        dict(item)
        for item in cursos_alumno or []
        if (
            item.get(
                "curso"
            )
            and normalizar(
                item.get(
                    "curso",
                    ""
                )
            ) not in origenes_usados
        )
    ]

    if not cursos_disponibles:
        return [
            {
                "curso_destino": curso,
                "curso_sugerido": "",
                "nota": "",
                "afinidad": "SIN CANDIDATO",
                "recomendacion": (
                    "Mantener como suficiencia o solicitar sílabos."
                ),
                "justificacion": (
                    "No quedan cursos libres del certificado con "
                    "evidencia suficiente para una recomendación segura."
                ),
                "requiere_silabo": True
            }
            for curso in cursos_pendientes
        ]

    prompt_sistema = """
Eres un especialista universitario senior en INGENIERÍA CIVIL y
convalidación por competencias.

Debes revisar cursos UPRIT que siguen sin convalidarse y recomendar,
SOLO COMO APOYO AL COORDINADOR, qué curso REAL del certificado podría
ser el mejor candidato para revisión.

REGLAS:
1. Solo usa cursos entregados en la lista.
2. No inventes cursos, notas, sílabos ni contenidos.
3. Un curso del certificado puede sugerirse máximo una vez.
4. No fuerces equivalencias para reducir suficiencias.
5. Si no existe candidato razonable, deja curso_sugerido vacío.
6. Afinidad: ALTA, MEDIA, BAJA o SIN CANDIDATO.
7. La recomendación no constituye aprobación automática.
8. Educación Física no equivale a Física.
9. Cálculo de Costos no equivale a Cálculo matemático.

Devuelve exclusivamente JSON válido.
"""

    prompt_usuario = f"""
CURSOS UPRIT TODAVÍA PENDIENTES:
{json.dumps(cursos_pendientes, ensure_ascii=False, indent=2)}

CURSOS REALES DEL CERTIFICADO TODAVÍA DISPONIBLES:
{json.dumps(cursos_disponibles, ensure_ascii=False, indent=2)}

Devuelve:
{{
  "recomendaciones": [
    {{
      "curso_destino": "",
      "curso_sugerido": "",
      "afinidad": "ALTA|MEDIA|BAJA|SIN CANDIDATO",
      "recomendacion": "",
      "justificacion": "",
      "requiere_silabo": true
    }}
  ]
}}
"""

    try:
        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": prompt_usuario
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=0
        )

        datos = json.loads(
            respuesta.choices[0].message.content
            or "{}"
        )

        propuestas = datos.get(
            "recomendaciones",
            []
        )

    except Exception:
        propuestas = []

    mapa_origen = {
        normalizar(
            item.get(
                "curso",
                ""
            )
        ): item
        for item in cursos_disponibles
        if item.get(
            "curso"
        )
    }

    mapa_destino = {
        normalizar(
            curso
        ): curso
        for curso in cursos_pendientes
    }

    origenes_recomendados = set()
    destinos_recomendados = set()
    salida = []

    for propuesta in propuestas:

        if not isinstance(
            propuesta,
            dict
        ):
            continue

        destino_norm = normalizar(
            propuesta.get(
                "curso_destino",
                ""
            )
        )

        if (
            destino_norm not in mapa_destino
            or destino_norm in destinos_recomendados
        ):
            continue

        sugerido_norm = normalizar(
            propuesta.get(
                "curso_sugerido",
                ""
            )
        )

        origen_real = mapa_origen.get(
            sugerido_norm
        )

        if (
            sugerido_norm
            and (
                origen_real is None
                or sugerido_norm in origenes_recomendados
            )
        ):
            origen_real = None
            sugerido_norm = ""

        afinidad = normalizar(
            propuesta.get(
                "afinidad",
                "SIN CANDIDATO"
            )
        )

        if afinidad not in {
            "ALTA",
            "MEDIA",
            "BAJA",
            "SIN CANDIDATO"
        }:
            afinidad = "MEDIA"

        nota_real = ""

        if origen_real:
            nota_real = obtener_nota_real(
                origen_real
            )
            origenes_recomendados.add(
                sugerido_norm
            )

        salida.append({
            "curso_destino":
                mapa_destino[
                    destino_norm
                ],
            "curso_sugerido":
                (
                    origen_real.get(
                        "curso",
                        ""
                    )
                    if origen_real
                    else ""
                ),
            "nota":
                nota_real,
            "afinidad":
                afinidad,
            "recomendacion":
                str(
                    propuesta.get(
                        "recomendacion",
                        ""
                    )
                    or ""
                ).strip(),
            "justificacion":
                str(
                    propuesta.get(
                        "justificacion",
                        ""
                    )
                    or ""
                ).strip(),
            "requiere_silabo":
                bool(
                    propuesta.get(
                        "requiere_silabo",
                        True
                    )
                )
        })

        destinos_recomendados.add(
            destino_norm
        )

    for curso in cursos_pendientes:

        if normalizar(
            curso
        ) in destinos_recomendados:
            continue

        salida.append({
            "curso_destino":
                curso,
            "curso_sugerido":
                "",
            "nota":
                "",
            "afinidad":
                "SIN CANDIDATO",
            "recomendacion":
                "Mantener como suficiencia o solicitar sílabos.",
            "justificacion":
                (
                    "No se identificó una equivalencia adicional "
                    "académicamente defendible."
                ),
            "requiere_silabo":
                True
        })

    return salida


# ============================================================
# DEEPSEEK
# ============================================================

def consultar_deepseek(
    cursos_alumno,
    estructura_proforma,
    carrera_destino="",
    reglas=None
):
    """
    DeepSeek se usa únicamente para determinar AFINIDAD ACADÉMICA.

    No recibe autoridad para crear ni modificar notas.
    """

    reglas = reglas or {}

    instrucciones_especialista = str(
        reglas.get(
            "instrucciones_especialista",
            ""
        )
        or ""
    ).strip()

    prompt_sistema = """
Eres especialista en convalidaciones académicas universitarias.

Debes encontrar equivalencias académicamente razonables entre:
- cursos REALES del certificado;
- cursos REALES de la proforma UPRIT.

NO estás calculando notas.
NO puedes inventar cursos.
NO puedes inventar contenidos de sílabos que no están disponibles.

CRITERIO GENERAL:
No te limites a comparar palabras. Evalúa el significado académico,
el área de conocimiento y la finalidad habitual de la asignatura.

Puedes proponer equivalencias aunque el nombre sea diferente cuando
la relación académica sea clara.

Ejemplos:
- Comunicación puede relacionarse con Lenguaje, Redacción,
  Comunicación Oral y Escrita, Expresión Oral y Escrita.
- Taller de Expresión Escrita puede relacionarse con Redacción.
- Estadística y Probabilidades puede relacionarse con Estadística.
- Fundamentos de Administración puede relacionarse con
  Administración General.
- Psicología del Desarrollo puede relacionarse con Psicología
  Evolutiva o Desarrollo Humano.
- Psicometría puede relacionarse con Medición Psicológica o
  Teoría de los Tests.

REGLAS:
1. Usa únicamente nombres que existan en las listas entregadas.
2. Un curso del certificado puede utilizarse como máximo una vez.
3. Un curso UPRIT puede recibir como máximo una equivalencia.
4. No devuelvas notas.
5. No rechaces una equivalencia solo porque los créditos sean
   distintos.
6. Si la relación académica es razonable, puedes marcarla ALTA
   o MEDIA.
7. Si es claramente de otra área académica, NO la propongas.

BLOQUEOS MÍNIMOS OBLIGATORIOS:
- Educación Física / Deportes / Actividad Física != Física.
- Programación Neurolingüística != Programación informática.
- Redes Sociales != Redes de Computadoras / Redes Informáticas.
- Cálculo de Costos != Cálculo matemático.
- Psiquiatría no equivale automáticamente a Psicología Clínica,
  Psicopatología, Evaluación Psicológica o Psicoterapia.

Devuelve exclusivamente JSON válido.
"""

    if instrucciones_especialista:
        prompt_sistema += (
            "\n\n"
            "INSTRUCCIONES ESPECÍFICAS DE LA CARRERA:\n"
            + instrucciones_especialista
        )

    prompt_usuario = f"""
CARRERA DESTINO:
{carrera_destino}

CURSOS REALES DEL CERTIFICADO:
{json.dumps(
    cursos_alumno,
    ensure_ascii=False,
    indent=2
)}

CURSOS REALES DE LA PROFORMA UPRIT:
{json.dumps(
    estructura_proforma,
    ensure_ascii=False,
    indent=2
)}

Devuelve exactamente:

{{
  "equivalencias": [
    {{
      "curso_origen": "",
      "curso_destino": "",
      "nivel_afinidad": "ALTA",
      "requiere_validacion": false,
      "justificacion": ""
    }}
  ]
}}

IMPORTANTE:
NO INCLUYAS NOTAS.
"""

    try:

        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role":
                        "system",
                    "content":
                        prompt_sistema
                },
                {
                    "role":
                        "user",
                    "content":
                        prompt_usuario
                }
            ],
            response_format={
                "type":
                    "json_object"
            },
            temperature=0
        )

        contenido = (
            respuesta
            .choices[0]
            .message
            .content
        )

        if not contenido:
            return []

        datos = json.loads(
            contenido
        )

        equivalencias = datos.get(
            "equivalencias",
            []
        )

        if not isinstance(
            equivalencias,
            list
        ):
            return []

        return equivalencias

    except Exception:
        # El resto del motor sigue funcionando si DeepSeek falla.
        return []


# ============================================================
# VALIDAR EQUIVALENCIAS DE IA
# ============================================================

def validar_equivalencias(
    propuesta,
    cursos_alumno,
    estructura_proforma
):

    resultado = []
    usados_origen = set()
    usados_destino = set()

    mapa_destino = {
        normalizar(
            item[
                "curso"
            ]
        ):
            item
        for item in estructura_proforma
    }

    for item_ia in propuesta:

        if not isinstance(
            item_ia,
            dict
        ):
            continue

        curso_origen_ia = str(
            item_ia.get(
                "curso_origen",
                ""
            )
        ).strip()

        curso_destino_ia = str(
            item_ia.get(
                "curso_destino",
                ""
            )
        ).strip()

        nivel = str(
            item_ia.get(
                "nivel_afinidad",
                ""
            )
        ).upper().strip()

        requiere_validacion = bool(
            item_ia.get(
                "requiere_validacion",
                False
            )
        )

        justificacion = str(
            item_ia.get(
                "justificacion",
                ""
            )
        ).strip()

        if nivel not in (
            "ALTA",
            "MEDIA"
        ):
            continue

        curso_real = buscar_curso_original(
            curso_origen_ia,
            cursos_alumno
        )

        if curso_real is None:
            continue

        origen_real = curso_real.get(
            "curso",
            ""
        )

        origen_normal = normalizar(
            origen_real
        )

        destino_normal = normalizar(
            curso_destino_ia
        )

        if destino_normal not in mapa_destino:
            continue

        destino_info = mapa_destino[
            destino_normal
        ]

        destino_real = destino_info[
            "curso"
        ]

        if son_areas_incompatibles(
            origen_real,
            destino_real
        ):
            continue

        if origen_normal in usados_origen:
            continue

        if destino_normal in usados_destino:
            continue

        resultado.append(
            crear_equivalencia(
                destino_info=destino_info,
                origen_info=curso_real,
                afinidad=nivel,
                tipo="EQUIVALENCIA SEMÁNTICA",
                requiere_validacion=requiere_validacion,
                justificacion=(
                    justificacion
                    or
                    "Equivalencia académica propuesta por afinidad "
                    "semántica y de competencias."
                )
            )
        )

        usados_origen.add(
            origen_normal
        )

        usados_destino.add(
            destino_normal
        )

    return resultado


def buscar_curso_original(
    nombre_ia,
    cursos_alumno
):

    nombre_normal = normalizar(
        nombre_ia
    )

    for item in cursos_alumno:

        curso = item.get(
            "curso",
            ""
        )

        if normalizar(
            curso
        ) == nombre_normal:
            return item

    mejor_item = None
    mejor_puntaje = 0

    for item in cursos_alumno:

        curso = item.get(
            "curso",
            ""
        )

        puntaje = fuzz.ratio(
            nombre_normal,
            normalizar(
                curso
            )
        )

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_item = item

    if (
        mejor_item is not None
        and mejor_puntaje >= 96
    ):
        return mejor_item

    return None


# ============================================================
# CREAR EQUIVALENCIA
# ============================================================

def crear_equivalencia(
    destino_info,
    origen_info,
    afinidad,
    tipo,
    requiere_validacion,
    justificacion
):

    return {
        "competencia":
            destino_info.get(
                "competencia",
                ""
            ),
        "curso_destino":
            destino_info.get(
                "curso",
                ""
            ),
        "curso_origen":
            origen_info.get(
                "curso",
                ""
            ),
        "nota":
            obtener_nota_real(
                origen_info
            ),
        "creditos_destino":
            destino_info.get(
                "creditos",
                ""
            ),
        "creditos_origen":
            origen_info.get(
                "creditos",
                ""
            ),
        "afinidad":
            afinidad,
        "tipo_equivalencia":
            tipo,
        "requiere_validacion":
            requiere_validacion,
        "justificacion":
            justificacion,
        "estado":
            (
                "REQUIERE VALIDACIÓN ACADÉMICA"
                if requiere_validacion
                else "CONVALIDACIÓN PROPUESTA"
            )
    }


# ============================================================
# ELIMINAR DUPLICADOS
# ============================================================

def eliminar_duplicados_equivalencias(
    equivalencias
):

    resultado = []
    usados_origen = set()
    usados_destino = set()

    for item in equivalencias:

        origen = normalizar(
            item.get(
                "curso_origen",
                ""
            )
        )

        destino = normalizar(
            item.get(
                "curso_destino",
                ""
            )
        )

        if not origen or not destino:
            continue

        if origen in usados_origen:
            continue

        if destino in usados_destino:
            continue

        usados_origen.add(
            origen
        )

        usados_destino.add(
            destino
        )

        resultado.append(
            item
        )

    return resultado



# ============================================================
# ÍNDICE ROBUSTO DE CURSOS Y NOTAS DEL CERTIFICADO
# ============================================================

def construir_indice_certificado(
    cursos_alumno
):
    """
    Construye un índice por nombre normalizado del curso.

    Cada entrada conserva exclusivamente información del MISMO curso
    del certificado. Nunca mezcla notas entre asignaturas.
    """

    indice = defaultdict(
        list
    )

    for item in cursos_alumno or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        curso = str(
            item.get(
                "curso",
                ""
            )
            or ""
        ).strip()

        if not curso:
            continue

        clave = normalizar(
            curso
        )

        if not clave:
            continue

        indice[
            clave
        ].append(
            item
        )

    return indice


def buscar_registro_certificado(
    curso_origen,
    indice_certificado
):
    """
    Devuelve el registro real del certificado para curso_origen.

    Prioridad:
    1. coincidencia normalizada exacta;
    2. coincidencia casi exacta >= 98%, solo si es inequívoca.

    Nunca usa un curso diferente como sustituto.
    """

    clave = normalizar(
        curso_origen
    )

    if not clave:
        return None

    # Coincidencia exacta
    exactos = indice_certificado.get(
        clave,
        []
    )

    if exactos:

        # Si hay varias apariciones, preferimos una que tenga nota real.
        con_nota = [
            item
            for item in exactos
            if obtener_nota_real(
                item
            ) != ""
        ]

        if len(
            con_nota
        ) == 1:
            return con_nota[0]

        if len(
            con_nota
        ) > 1:

            notas = {
                obtener_nota_real(
                    item
                )
                for item in con_nota
            }

            # Solo es seguro si todas las apariciones tienen la misma nota.
            if len(
                notas
            ) == 1:
                return con_nota[0]

        # Si no hay nota, devolvemos el primer registro exacto para
        # conservar nombre/créditos, pero la nota seguirá vacía.
        return exactos[0]

    # Coincidencia casi exacta
    candidatos = []

    for clave_candidata, registros in indice_certificado.items():

        puntaje = fuzz.ratio(
            clave,
            clave_candidata
        )

        if puntaje < 98:
            continue

        for registro in registros:

            nota = obtener_nota_real(
                registro
            )

            candidatos.append(
                (
                    puntaje,
                    clave_candidata,
                    nota,
                    registro
                )
            )

    if not candidatos:
        return None

    candidatos.sort(
        key=lambda x: x[0],
        reverse=True
    )

    mejor_puntaje = candidatos[
        0
    ][0]

    mejores = [
        x
        for x in candidatos
        if x[0] == mejor_puntaje
    ]

    claves_mejores = {
        x[1]
        for x in mejores
    }

    # Solo aceptamos si el mejor resultado corresponde a un único
    # nombre normalizado de curso.
    if len(
        claves_mejores
    ) != 1:
        return None

    con_nota = [
        x
        for x in mejores
        if x[2] != ""
    ]

    if len(
        con_nota
    ) == 1:
        return con_nota[0][3]

    if len(
        con_nota
    ) > 1:

        notas = {
            x[2]
            for x in con_nota
        }

        if len(
            notas
        ) == 1:
            return con_nota[0][3]

    return mejores[0][3]


def rehidratar_nota_equivalencia(
    equivalencia,
    indice_certificado
):
    """
    Garantiza que una equivalencia conserve la nota REAL del curso
    de procedencia.

    Si item["nota"] ya existe, se respeta.
    Si está vacía, se busca otra vez el MISMO curso en el certificado.

    Nunca inventa ni hereda notas de otro curso.
    """

    if not isinstance(
        equivalencia,
        dict
    ):
        return equivalencia

    resultado = dict(
        equivalencia
    )

    nota_actual = obtener_nota_real(
        resultado
    )

    if nota_actual != "":

        resultado[
            "nota"
        ] = nota_actual

        return resultado

    curso_origen = resultado.get(
        "curso_origen",
        ""
    )

    registro = buscar_registro_certificado(
        curso_origen=curso_origen,
        indice_certificado=indice_certificado
    )

    if registro is None:
        resultado[
            "nota"
        ] = ""
        return resultado

    nota_real = obtener_nota_real(
        registro
    )

    resultado[
        "nota"
    ] = nota_real

    # Solo completar créditos si estaban vacíos.
    if (
        not resultado.get(
            "creditos_origen"
        )
        and registro.get(
            "creditos"
        ) not in (
            None,
            ""
        )
    ):
        resultado[
            "creditos_origen"
        ] = registro.get(
            "creditos"
        )

    return resultado


def rehidratar_notas_equivalencias(
    equivalencias,
    cursos_alumno
):
    """
    Revisa TODAS las equivalencias antes de evaluar competencias.
    """

    indice = construir_indice_certificado(
        cursos_alumno
    )

    return [
        rehidratar_nota_equivalencia(
            equivalencia=item,
            indice_certificado=indice
        )
        for item in equivalencias or []
        if isinstance(
            item,
            dict
        )
    ]


# ============================================================
# NOTA REAL
# ============================================================

def obtener_nota_real(
    item
):

    if item is None:
        return ""

    nota = item.get(
        "nota",
        ""
    )

    if nota is None:
        return ""

    try:
        nota = float(
            nota
        )
    except (
        TypeError,
        ValueError
    ):
        return ""

    if nota <= 0 or nota > 20:
        return ""

    if nota.is_integer():
        return int(
            nota
        )

    return round(
        nota,
        2
    )



# ============================================================
# RECUPERAR NOTA REAL DESDE EL CERTIFICADO POR CURSO DE ORIGEN
# ============================================================

def recuperar_nota_desde_certificado(
    curso_origen,
    cursos_alumno
):
    """
    Busca la nota real del MISMO curso de procedencia en la lista
    original del certificado.

    Prioridad:
    1. coincidencia normalizada exacta;
    2. coincidencia casi exacta >= 98, solo si es única.

    Nunca toma la nota de otro curso.
    """

    nombre_objetivo = normalizar(
        curso_origen
    )

    if not nombre_objetivo:
        return ""

    # 1. Coincidencia exacta
    coincidencias_exactas = []

    for item in cursos_alumno or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        curso = item.get(
            "curso",
            ""
        )

        if normalizar(
            curso
        ) == nombre_objetivo:

            nota = obtener_nota_real(
                item
            )

            if nota != "":
                coincidencias_exactas.append(
                    nota
                )

    notas_unicas = list(
        dict.fromkeys(
            coincidencias_exactas
        )
    )

    if len(
        notas_unicas
    ) == 1:
        return notas_unicas[0]

    # 2. Coincidencia casi exacta y única
    candidatos = []

    for item in cursos_alumno or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        curso = item.get(
            "curso",
            ""
        )

        curso_normal = normalizar(
            curso
        )

        if not curso_normal:
            continue

        puntaje = fuzz.ratio(
            nombre_objetivo,
            curso_normal
        )

        if puntaje >= 98:

            nota = obtener_nota_real(
                item
            )

            if nota != "":
                candidatos.append(
                    (
                        puntaje,
                        curso_normal,
                        nota
                    )
                )

    if not candidatos:
        return ""

    candidatos.sort(
        key=lambda x: x[0],
        reverse=True
    )

    mejor_puntaje = candidatos[
        0
    ][0]

    mejores = [
        x
        for x in candidatos
        if x[0] == mejor_puntaje
    ]

    notas_mejores = list(
        dict.fromkeys(
            x[2]
            for x in mejores
        )
    )

    if len(
        notas_mejores
    ) == 1:
        return notas_mejores[0]

    return ""


def completar_notas_desde_certificado(
    convalidaciones_base,
    cursos_alumno
):
    """
    Completa únicamente notas faltantes de equivalencias ya creadas.

    No modifica curso_origen.
    No modifica curso_destino.
    No crea nuevas equivalencias.
    No reemplaza una nota ya presente.
    """

    resultado = []

    for item in convalidaciones_base or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        item_final = dict(
            item
        )

        nota_actual = obtener_nota_real(
            item_final
        )

        if nota_actual == "":

            curso_origen = item_final.get(
                "curso_origen",
                ""
            )

            nota_recuperada = recuperar_nota_desde_certificado(
                curso_origen=curso_origen,
                cursos_alumno=cursos_alumno
            )

            if nota_recuperada != "":
                item_final[
                    "nota"
                ] = nota_recuperada

        resultado.append(
            item_final
        )

    return resultado


# ============================================================
# EVALUAR POR COMPETENCIAS
# ============================================================

def evaluar_por_competencias(
    estructura_proforma,
    convalidaciones_base,
    cursos_alumno=None,
    reglas=None
):
    """
    Aplica la lógica DEFINITIVA de convalidación por competencias.

    REGLAS:

    A) Si TODOS los cursos de una competencia tienen equivalencia:
       - se convalida la competencia;
       - NOTA PARCIAL = nota real de cada curso de procedencia;
       - NOTA CONVALIDANTE = promedio de TODAS las notas parciales
         válidas de la competencia, con tope de 15.

    B) Si falta SOLO 1 curso de la competencia:
       - la competencia SE CONVALIDA;
       - se mantienen llenos los cursos que sí tienen equivalencia;
       - el único curso faltante queda con:
         ASIGNATURA CONVALIDANTE = vacío
         NOTA PARCIAL = vacío
       - NOTA CONVALIDANTE = promedio de las notas parciales
         de los cursos encontrados, con tope de 15.

    C) Si faltan 2 O MÁS cursos:
       - los cursos faltantes pasan a SUFICIENCIA;
       - las equivalencias encontradas NO se borran;
       - su NOTA PARCIAL sigue siendo la nota real del certificado;
       - la NOTA CONVALIDANTE de esa competencia queda pendiente
         hasta resolver las suficiencias.

    D) Si existen más de 7 suficiencias en todo el expediente:
       - NO se bloquea la proforma;
       - analizar_convalidaciones marcará CASO ESPECIAL;
       - generador_word.py emitirá además el reporte especial.

    IMPORTANTE:
    Nunca se inventan notas. Si alguna equivalencia encontrada no
    tiene nota real, la nota convalidante queda vacía en lugar de
    calcularse con información incompleta.
    """

    reglas = reglas or REGLAS_GENERALES

    permitir_un_faltante = bool(
        reglas.get(
            "permitir_un_faltante_en_competencia",
            True
        )
    )

    faltantes_para_suficiencia = int(
        reglas.get(
            "faltantes_para_suficiencia",
            2
        )
    )

    tope_nota_convalidante = int(
        reglas.get(
            "tope_nota_convalidante",
            NOTA_MAXIMA_CONVALIDANTE
        )
    )

    # Última protección antes de evaluar por competencias:
    # recuperar la nota exclusivamente desde el mismo curso de origen.
    if cursos_alumno:
        convalidaciones_base = rehidratar_notas_equivalencias(
            equivalencias=convalidaciones_base,
            cursos_alumno=cursos_alumno
        )

    indice_certificado = construir_indice_certificado(
        cursos_alumno or []
    )

    mapa_convalidaciones = {}

    for item in convalidaciones_base:

        curso_destino = normalizar(
            item.get(
                "curso_destino",
                ""
            )
        )

        if not curso_destino:
            continue

        # La primera equivalencia válida conserva prioridad.
        if curso_destino not in mapa_convalidaciones:
            mapa_convalidaciones[
                curso_destino
            ] = item

    grupos = defaultdict(
        list
    )

    for indice, item in enumerate(
        estructura_proforma
    ):

        competencia_original = str(
            item.get(
                "competencia",
                ""
            )
            or ""
        ).strip()

        # Si una plantilla no permite identificar la competencia,
        # NO agrupamos todos los cursos en una sola competencia
        # artificial. Cada curso queda aislado para evitar promedios
        # erróneos entre áreas académicas diferentes.
        if competencia_original:
            clave_competencia = competencia_original
        else:
            clave_competencia = (
                f"SIN COMPETENCIA IDENTIFICADA #{indice + 1}"
            )

        grupos[
            clave_competencia
        ].append(
            item
        )

    convalidaciones_finales = []
    pendientes = []
    suficiencias = []
    resumen_competencias = []

    for competencia, cursos_competencia in grupos.items():

        encontrados = []
        faltantes = []

        for curso_info in cursos_competencia:

            curso_normal = normalizar(
                curso_info.get(
                    "curso",
                    ""
                )
            )

            equivalencia = mapa_convalidaciones.get(
                curso_normal
            )

            if equivalencia is not None:

                equivalencia = rehidratar_nota_equivalencia(
                    equivalencia=equivalencia,
                    indice_certificado=indice_certificado
                )

                encontrados.append(
                    equivalencia
                )
            else:
                faltantes.append(
                    curso_info
                )

        # ----------------------------------------------------
        # NOTAS PARCIALES REALES DE LOS CURSOS ENCONTRADOS
        # ----------------------------------------------------

        notas_validas = []
        todos_encontrados_tienen_nota = True

        for item in encontrados:

            nota = obtener_nota_real(
                {
                    "nota":
                        item.get(
                            "nota",
                            ""
                        )
                }
            )

            if nota == "":
                todos_encontrados_tienen_nota = False
                continue

            notas_validas.append(
                float(
                    nota
                )
            )

        # Solo calculamos promedio si TODAS las equivalencias
        # encontradas poseen una nota real.
        if (
            encontrados
            and todos_encontrados_tienen_nota
            and len(notas_validas) == len(encontrados)
        ):
            nota_convalidante_calculada = (
                calcular_nota_convalidante(
                    notas=notas_validas,
                    nota_maxima=tope_nota_convalidante
                )
            )
        else:
            nota_convalidante_calculada = ""

        cantidad_total = len(
            cursos_competencia
        )

        cantidad_encontrados = len(
            encontrados
        )

        cantidad_faltantes = len(
            faltantes
        )

        # ----------------------------------------------------
        # CASO 1: TODOS LOS CURSOS ENCONTRADOS
        # ----------------------------------------------------

        if cantidad_faltantes == 0:

            estado_competencia = (
                "COMPETENCIA CONVALIDADA"
            )

            justificacion_competencia = (
                f"Se identificó correspondencia para las "
                f"{cantidad_total} asignaturas de la competencia. "
                f"La nota convalidante corresponde al promedio "
                f"de las notas parciales reales del certificado."
            )

            nota_convalidante_competencia = (
                nota_convalidante_calculada
            )

        # ----------------------------------------------------
        # CASO 2: SOLO 1 CURSO FALTANTE
        # ----------------------------------------------------

        elif (
            permitir_un_faltante
            and cantidad_faltantes == 1
            and cantidad_encontrados >= 1
        ):

            estado_competencia = (
                "COMPETENCIA CONVALIDADA POR COMPETENCIAS"
            )

            justificacion_competencia = (
                f"La competencia contiene {cantidad_total} "
                f"asignaturas y se acreditaron "
                f"{cantidad_encontrados}. Al existir un solo "
                f"curso faltante, la competencia se convalida "
                f"con las asignaturas acreditadas. El curso "
                f"faltante permanece sin Asignatura Convalidante "
                f"y sin Nota Parcial. La Nota Convalidante es el "
                f"promedio de las notas parciales reales de los "
                f"cursos acreditados."
            )

            nota_convalidante_competencia = (
                nota_convalidante_calculada
            )

            # Agregar explícitamente la fila faltante para que
            # generador_word.py sepa dejarla vacía.
            faltante = faltantes[
                0
            ]

            convalidaciones_finales.append({
                "competencia":
                    competencia,
                "curso_destino":
                    faltante.get(
                        "curso",
                        ""
                    ),
                "curso_origen":
                    "",
                "nota":
                    "",
                "creditos_destino":
                    faltante.get(
                        "creditos",
                        ""
                    ),
                "creditos_origen":
                    "",
                "afinidad":
                    "",
                "tipo_equivalencia":
                    "CONVALIDACIÓN POR COMPETENCIA",
                "requiere_validacion":
                    False,
                "justificacion":
                    justificacion_competencia,
                "estado":
                    "CONVALIDACIÓN POR COMPETENCIA - CURSO FALTANTE",
                "nota_convalidante":
                    nota_convalidante_competencia,
                "estado_competencia":
                    estado_competencia,
                "justificacion_competencia":
                    justificacion_competencia
            })

        # ----------------------------------------------------
        # CASO 3: 2 O MÁS CURSOS FALTANTES
        # ----------------------------------------------------

        else:

            if cantidad_faltantes >= faltantes_para_suficiencia:
                estado_competencia = (
                    "COMPETENCIA PENDIENTE - SUFICIENCIA"
                )

                justificacion_competencia = (
                    f"La competencia contiene {cantidad_total} "
                    f"asignaturas; se acreditaron "
                    f"{cantidad_encontrados} y faltan "
                    f"{cantidad_faltantes}. Al alcanzar el umbral "
                    f"de {faltantes_para_suficiencia} asignaturas "
                    f"faltantes, estas pasan a examen de suficiencia."
                )

                nota_convalidante_competencia = ""
            else:
                estado_competencia = (
                    "COMPETENCIA PENDIENTE"
                )

                justificacion_competencia = (
                    f"La competencia contiene {cantidad_total} "
                    f"asignaturas; se acreditaron "
                    f"{cantidad_encontrados} y faltan "
                    f"{cantidad_faltantes}. La competencia queda "
                    f"pendiente de evaluación académica."
                )

                nota_convalidante_competencia = ""

            for faltante in faltantes:

                curso_faltante = str(
                    faltante.get(
                        "curso",
                        ""
                    )
                    or ""
                ).strip()

                if not curso_faltante:
                    continue

                if not es_nombre_curso_valido(
                    curso_faltante
                ):
                    continue

                if (
                    cantidad_faltantes >= faltantes_para_suficiencia
                    and curso_faltante not in suficiencias
                ):
                    suficiencias.append(
                        curso_faltante
                    )

                if curso_faltante not in pendientes:
                    pendientes.append(
                        curso_faltante
                    )

        # ----------------------------------------------------
        # CONSERVAR TODAS LAS EQUIVALENCIAS ENCONTRADAS
        # ----------------------------------------------------

        for item in encontrados:

            item_final = rehidratar_nota_equivalencia(
                equivalencia=item,
                indice_certificado=indice_certificado
            )

            # La nota parcial debe corresponder siempre al mismo
            # curso de procedencia del certificado.
            item_final[
                "nota"
            ] = obtener_nota_real(
                item_final
            )

            item_final[
                "nota_convalidante"
            ] = nota_convalidante_competencia

            item_final[
                "estado_competencia"
            ] = estado_competencia

            item_final[
                "justificacion_competencia"
            ] = justificacion_competencia

            convalidaciones_finales.append(
                item_final
            )

        resumen_competencias.append({
            "competencia":
                competencia,
            "total_asignaturas":
                cantidad_total,
            "asignaturas_con_equivalencia":
                cantidad_encontrados,
            "asignaturas_faltantes":
                cantidad_faltantes,
            "nota_convalidante":
                nota_convalidante_competencia,
            "estado":
                estado_competencia,
            "justificacion":
                justificacion_competencia,
            "cursos_faltantes":
                [
                    item.get(
                        "curso",
                        ""
                    )
                    for item in faltantes
                ]
        })

    # --------------------------------------------------------
    # MANTENER EL ORDEN ORIGINAL DE LA PROFORMA
    # --------------------------------------------------------

    orden = {
        normalizar(
            item.get(
                "curso",
                ""
            )
        ):
            i
        for i, item in enumerate(
            estructura_proforma
        )
    }

    convalidaciones_finales.sort(
        key=lambda x: orden.get(
            normalizar(
                x.get(
                    "curso_destino",
                    ""
                )
            ),
            999999
        )
    )

    return {
        "convalidaciones":
            convalidaciones_finales,
        "pendientes":
            pendientes,
        "suficiencias":
            suficiencias,
        "competencias":
            resumen_competencias
    }


# ============================================================
# CALCULAR NOTA CONVALIDANTE
# ============================================================

def calcular_nota_convalidante(
    notas,
    nota_maxima=None
):

    if not notas:
        return ""

    if nota_maxima is None:
        nota_maxima = NOTA_MAXIMA_CONVALIDANTE

    promedio = (
        sum(
            notas
        )
        / len(
            notas
        )
    )

    # Redondeo convencional: 14.5 -> 15
    nota_final = int(
        promedio
        + 0.5
    )

    return min(
        nota_final,
        int(
            nota_maxima
        )
    )


# ============================================================
# BLOQUEOS DE ÁREAS INCOMPATIBLES
# ============================================================

def son_areas_incompatibles(
    curso_origen,
    curso_destino
):

    origen = normalizar(
        curso_origen
    )

    destino = normalizar(
        curso_destino
    )

    terminos_deporte = [
        "EDUCACION FISICA",
        "ACTIVIDAD FISICA",
        "CULTURA FISICA",
        "DEPORTE",
        "DEPORTIVA",
        "RECREACION",
        "ENTRENAMIENTO DEPORTIVO"
    ]

    destino_fisica = (
        destino == "FISICA"
        or destino.startswith(
            "FISICA "
        )
        or "FISICA I" in destino
        or "FISICA II" in destino
        or "FISICA GENERAL" in destino
    )

    origen_deporte = any(
        item in origen
        for item in terminos_deporte
    )

    if destino_fisica and origen_deporte:
        return True

    origen_fisica = (
        origen == "FISICA"
        or origen.startswith(
            "FISICA "
        )
        or "FISICA I" in origen
        or "FISICA II" in origen
        or "FISICA GENERAL" in origen
    )

    destino_deporte = any(
        item in destino
        for item in terminos_deporte
    )

    if origen_fisica and destino_deporte:
        return True

    if (
        "PROGRAMACION NEUROLINGUISTICA" in origen
        and "PROGRAMACION" in destino
    ):
        return True

    if (
        "REDES SOCIALES" in origen
        and (
            destino == "REDES"
            or "REDES Y SISTEMAS OPERATIVOS" in destino
            or "REDES DE COMPUTADORAS" in destino
            or "REDES INFORMATICAS" in destino
        )
    ):
        return True

    if (
        "TELECOMUNIC" in origen
        and (
            destino == "COMUNICACION"
            or destino.startswith(
                "COMUNICACION "
            )
        )
    ):
        return True

    if (
        "CALCULO DE COSTOS" in origen
        and (
            destino == "CALCULO"
            or destino.startswith(
                "CALCULO "
            )
            or "ANALISIS MATEMATICO" in destino
        )
    ):
        return True

    if (
        "PSIQUIATRIA" in origen
        and any(
            termino in destino
            for termino in [
                "PSICOLOGIA CLINICA",
                "PSICOPATOLOGIA",
                "EVALUACION PSICOLOGICA",
                "PSICOTERAPIA"
            ]
        )
    ):
        return True

    if (
        "PSICOLOGIA SOCIAL" in destino
        and (
            origen == "SOCIOLOGIA"
            or origen.startswith(
                "SOCIOLOGIA "
            )
            or origen == "CIENCIAS SOCIALES"
            or origen.startswith(
                "CIENCIAS SOCIALES "
            )
        )
    ):
        return True

    if (
        "PSICOLOGIA EDUCATIVA" in destino
        and (
            origen == "PEDAGOGIA"
            or origen.startswith(
                "PEDAGOGIA "
            )
            or origen == "DIDACTICA"
            or origen.startswith(
                "DIDACTICA "
            )
        )
    ):
        return True

    if (
        "PSICOPATOLOGIA" in destino
        and "PSICOLOGIA CLINICA" in origen
    ):
        return True

    return False


# ============================================================
# NORMALIZAR
# ============================================================

def lista_unica(
    valores
):
    """
    Devuelve una lista sin duplicados preservando el orden original.

    Se usa para limpiar cursos pendientes/suficiencias sin alterar
    la secuencia de la proforma.
    """

    resultado = []
    vistos = set()

    for valor in valores or []:

        texto = str(
            valor
            or ""
        ).strip()

        if not texto:
            continue

        clave = normalizar(
            texto
        )

        if not clave:
            continue

        if clave in vistos:
            continue

        vistos.add(
            clave
        )

        resultado.append(
            texto
        )

    return resultado


def normalizar(
    texto
):

    if texto is None:
        return ""

    texto = str(
        texto
    )

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(
            caracter
        ) != "Mn"
    )

    texto = texto.upper()

    texto = re.sub(
        r"[^A-Z0-9 ]",
        " ",
        texto
    )

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()
