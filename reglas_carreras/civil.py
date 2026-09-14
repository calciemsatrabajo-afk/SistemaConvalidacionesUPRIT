# ============================================================
# REGLAS PARTICULARES - INGENIERÍA CIVIL
# ============================================================
#
# Este archivo SOLO afecta a Ingeniería Civil.
#
# REGLAS POR COMPETENCIAS:
# - todos los cursos encontrados -> competencia convalidada;
# - si falta solo 1 curso -> la competencia se convalida por defecto;
# - la nota convalidante se calcula con las notas parciales reales;
# - redondeo convencional;
# - nota convalidante máxima = 15;
# - con 2 o más cursos faltantes -> candidatos a suficiencia.
#
# CASO ESPECIAL:
# - umbral ordinario = 5 candidatos a suficiencia;
# - si hay más de 5, se activa una SEGUNDA REVISIÓN;
# - esa revisión recibe TODOS los candidatos reales, SIN RECORTARLOS;
# - DeepSeek revisa nuevamente todo el certificado y toda la proforma
#   como especialista en Ingeniería Civil;
# - solo DESPUÉS de esa revisión se aplica el máximo de 7 suficiencias;
# - si permanecen más de 7 faltantes reales, los excedentes quedan
#   como PENDIENTES DE REVISIÓN ACADÉMICA, nunca como convalidados.
# ============================================================

REGLAS = {
    "permitir_un_faltante_en_competencia": True,
    "faltantes_para_suficiencia": 2,
    "tope_nota_convalidante": 15,

    # Umbral que dispara la revisión especial.
    "umbral_caso_especial": 5,

    # Máximo que puede quedar en la tabla final de suficiencias.
    "maximo_suficiencias": 7,
    "maximo_suficiencias_final": 7,

    # Obligatorio en Civil cuando se supera el umbral.
    "reevaluar_caso_especial_con_ia": True,

    # Estructura particular de la proforma de Civil.
    "detectar_competencia_a_la_izquierda_de_asignatura": True,
}
