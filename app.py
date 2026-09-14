import base64
import inspect
import hashlib
import io
import json
import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import pymupdf
import streamlit as st
import streamlit.components.v1 as components

from lector_pdf import leer_pdf
from convalidaciones import analizar_convalidaciones
from generador_word import (
    generar_word,
    extraer_mapa_competencias_desde_formato
)
from datos_alumnos import buscar_alumno
from configuracion_carreras import obtener_carreras


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Sistema de Convalidaciones Académicas - UPRIT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# ASSETS INSTITUCIONALES
# Las imágenes están directamente en la carpeta principal
# SISTEMA_CONVALIDACIONES.
# ============================================================

RUTA_LOGO = BASE_DIR / "logo_uprit.png"
RUTA_FONDO = BASE_DIR / "campus UPRIT.jpg"

# Si por alguna razón no existen, se desactiva el asset
# para que la aplicación siga funcionando sin bloquearse.
if not RUTA_LOGO.exists():
    RUTA_LOGO = None

if not RUTA_FONDO.exists():
    RUTA_FONDO = None


@st.cache_data(show_spinner=False)
def archivo_a_base64(ruta):
    if not ruta:
        return ""

    try:
        with open(ruta, "rb") as archivo:
            return base64.b64encode(
                archivo.read()
            ).decode("utf-8")
    except Exception:
        return ""


logo_b64 = archivo_a_base64(
    RUTA_LOGO
)

fondo_b64 = archivo_a_base64(
    RUTA_FONDO
)


# ============================================================
# COLORES INSTITUCIONALES
# ============================================================

ROJO_UPRIT = "#B5121B"
ROJO_UPRIT_OSCURO = "#8F0E15"
ROJO_SUAVE = "#FCEBED"
GRIS_FONDO = "#F5F6F8"
GRIS_BORDE = "#E4E7EB"
GRIS_TEXTO = "#5E6773"
TEXTO_OSCURO = "#202A36"


# ============================================================
# CSS
# ============================================================

fondo_css = ""

if fondo_b64:
    extension = (
        "png"
        if RUTA_FONDO and RUTA_FONDO.suffix.lower() == ".png"
        else "jpeg"
    )

    fondo_css = f"""
    .stApp {{
        background:
            linear-gradient(
                rgba(255,255,255,0.92),
                rgba(255,255,255,0.96)
            ),
            url("data:image/{extension};base64,{fondo_b64}")
            center center / cover fixed;
    }}
    """
else:
    fondo_css = """
    .stApp {
        background: #F5F6F8;
    }
    """

st.markdown(
    f"""
    <style>

    {fondo_css}

    :root {{
        --uprit-red: {ROJO_UPRIT};
        --uprit-dark: {ROJO_UPRIT_OSCURO};
        --uprit-soft: {ROJO_SUAVE};
        --border: {GRIS_BORDE};
        --text: {TEXTO_OSCURO};
        --muted: {GRIS_TEXTO};
    }}

    html, body, [class*="css"] {{
        font-family: "Segoe UI", Arial, sans-serif;
    }}

    .block-container {{
        max-width: 1500px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }}

    /* Ocultar menú/branding visual innecesario */
    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    /* =====================================================
       HEADER
       ===================================================== */

    .uprit-header {{
        display: flex;
        align-items: center;
        gap: 18px;
        background:
            linear-gradient(
                90deg,
                rgba(255,255,255,0.98) 0%,
                rgba(255,255,255,0.98) 72%,
                rgba(252,235,237,0.98) 100%
            );
        border: 1px solid #ECEDEF;
        border-bottom: 5px solid var(--uprit-red);
        border-radius: 16px;
        padding: 18px 22px;
        margin-bottom: 14px;
        box-shadow: 0 8px 26px rgba(0,0,0,0.06);
    }}

    .uprit-logo {{
        width: 220px;
        max-height: 90px;
        object-fit: contain;
    }}

    .uprit-logo-fallback {{
        color: var(--uprit-red);
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 1px;
        min-width: 180px;
    }}

    .uprit-accent {{
        width: 6px;
        min-height: 70px;
        border-radius: 8px;
        background: var(--uprit-red);
    }}

    .uprit-header-text {{
        flex: 1;
    }}

    .uprit-title {{
        font-size: 28px;
        font-weight: 800;
        color: var(--text);
        line-height: 1.08;
        margin-bottom: 6px;
    }}

    .uprit-subtitle {{
        color: var(--muted);
        font-size: 15px;
    }}

    .uprit-slogan {{
        color: var(--uprit-red);
        font-weight: 700;
        font-size: 13px;
        text-align: right;
        line-height: 1.3;
    }}

    /* =====================================================
       STEPPER
       ===================================================== */

    .stepper {{
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        margin: 8px 0 18px 0;
    }}

    .step {{
        background: rgba(255,255,255,0.96);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 11px 13px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.035);
    }}

    .step.active {{
        border-color: var(--uprit-red);
        background: #FFF7F7;
        box-shadow: 0 4px 14px rgba(181,18,27,0.08);
    }}

    .step-num {{
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: #9AA3AD;
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 30px;
        font-weight: 800;
    }}

    .step.active .step-num {{
        background: var(--uprit-red);
    }}

    .step-label {{
        font-size: 13px;
        font-weight: 700;
        color: #596675;
    }}

    /* =====================================================
       SECCIONES / TARJETAS
       ===================================================== */

    .section-title {{
        background:
            linear-gradient(
                90deg,
                var(--uprit-red),
                #CC202A
            );
        color: white;
        padding: 10px 14px;
        border-radius: 10px 10px 0 0;
        font-size: 15px;
        font-weight: 750;
        margin-bottom: 10px;
    }}

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        border: 1px solid #E5E7EA !important;
        border-radius: 14px !important;
        background: rgba(255,255,255,0.97) !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.045);
    }}

    /* =====================================================
       INPUTS
       ===================================================== */

    .stTextInput input,
    .stNumberInput input {{
        border-radius: 8px !important;
    }}

    div[data-baseweb="select"] > div {{
        border-radius: 8px !important;
    }}

    div[data-testid="stFileUploader"] {{
        border-radius: 10px;
    }}

    /* =====================================================
       BOTONES
       ===================================================== */

    .stButton > button[kind="primary"] {{
        background:
            linear-gradient(
                90deg,
                var(--uprit-red),
                #CF1F2A
            ) !important;
        color: white !important;
        border: none !important;
        border-radius: 9px !important;
        min-height: 45px;
        font-weight: 750 !important;
        box-shadow: 0 4px 14px rgba(181,18,27,0.18);
    }}

    .stButton > button[kind="primary"]:hover {{
        background:
            linear-gradient(
                90deg,
                var(--uprit-dark),
                var(--uprit-red)
            ) !important;
        color: white !important;
    }}

    .stDownloadButton > button {{
        background:
            linear-gradient(
                90deg,
                var(--uprit-red),
                #CF1F2A
            ) !important;
        color: white !important;
        border: none !important;
        border-radius: 9px !important;
        min-height: 45px;
        font-weight: 750 !important;
        width: 100%;
    }}

    .stDownloadButton > button:hover {{
        background:
            linear-gradient(
                90deg,
                var(--uprit-dark),
                var(--uprit-red)
            ) !important;
        color: white !important;
    }}

    /* =====================================================
       METRICAS
       ===================================================== */

    div[data-testid="stMetric"] {{
        background: white;
        border: 1px solid var(--border);
        border-left: 5px solid var(--uprit-red);
        border-radius: 10px;
        padding: 11px 13px;
    }}

    /* =====================================================
       DATAFRAMES
       ===================================================== */

    div[data-testid="stDataFrame"] {{
        border: 1px solid #E4E7EB;
        border-radius: 10px;
        overflow: hidden;
    }}

    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                #FFFFFF 0%,
                #F7F8FA 100%
            );
        border-right: 1px solid #E5E7EB;
    }}

    .sidebar-brand {{
        color: var(--uprit-red);
        font-size: 18px;
        font-weight: 850;
        margin-top: 8px;
    }}

    .sidebar-small {{
        color: #6B7280;
        font-size: 12px;
        margin-top: 2px;
        margin-bottom: 14px;
    }}

    .sidebar-item-active {{
        background: var(--uprit-red);
        color: white;
        padding: 10px 12px;
        border-radius: 8px;
        font-weight: 700;
        margin-bottom: 7px;
    }}

    .sidebar-item {{
        color: #374151;
        padding: 8px 10px;
        border-radius: 8px;
        margin-bottom: 4px;
    }}

    /* =====================================================
       ESTADOS
       ===================================================== */

    .status-ok {{
        display: inline-block;
        background: #EAF8EE;
        color: #217A39;
        border: 1px solid #CFEAD7;
        border-radius: 8px;
        padding: 8px 12px;
        font-weight: 700;
        margin-top: 3px;
    }}

    /* =====================================================
       FOOTER
       ===================================================== */

    .footer-uprit {{
        margin-top: 32px;
        background:
            linear-gradient(
                90deg,
                var(--uprit-dark),
                var(--uprit-red)
            );
        color: white;
        border-radius: 10px;
        padding: 13px 18px;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        gap: 12px;
    }}

    @media (max-width: 900px) {{
        .stepper {{
            grid-template-columns: 1fr 1fr;
        }}

        .uprit-header {{
            flex-direction: column;
            align-items: flex-start;
        }}

        .uprit-logo {{
            width: 180px;
        }}

        .uprit-slogan {{
            text-align: left;
        }}
    }}

    

/* ============================================================
   REDISEÑO VISUAL UPRIT - CLARO, SOBRIO Y FUNCIONAL
   ============================================================ */

:root {{
    --uprit-guinda: #8F0D1A;
    --uprit-rojo: #B5121B;
    --uprit-rojo-2: #C91D2B;
    --uprit-rosa: #FBEDEF;
    --uprit-crema: #FFF9F7;
    --uprit-gris: #F5F6F8;
    --uprit-borde: #E8D7DA;
    --uprit-texto: #2F2430;
    --uprit-muted: #75666B;
}}

/* Barra superior */
[data-testid="stHeader"] {{
    background: #8F0D1A !important;
}}

[data-testid="stHeader"] * {{
    color: white !important;
}}

[data-testid="stToolbar"] {{
    background: transparent !important;
}}

/* Fondo principal */
.stApp {{
    color: var(--uprit-texto) !important;
}}

/* Selectbox */
div[data-baseweb="select"] > div {{
    background: #FFFFFF !important;
    border: 1px solid #D9C5C9 !important;
    color: var(--uprit-texto) !important;
    border-radius: 10px !important;
    min-height: 44px !important;
}}

div[data-baseweb="select"] span,
div[data-baseweb="select"] input {{
    color: var(--uprit-texto) !important;
}}

div[data-baseweb="select"] svg {{
    color: var(--uprit-guinda) !important;
    fill: var(--uprit-guinda) !important;
}}

div[role="listbox"],
ul[role="listbox"] {{
    background: #FFFFFF !important;
    border: 1px solid #E5D6D9 !important;
}}

div[role="option"],
li[role="option"] {{
    background: #FFFFFF !important;
    color: var(--uprit-texto) !important;
}}

div[role="option"]:hover,
li[role="option"]:hover,
div[aria-selected="true"][role="option"],
li[aria-selected="true"][role="option"] {{
    background: var(--uprit-rosa) !important;
    color: var(--uprit-guinda) !important;
}}

/* Uploader */
[data-testid="stFileUploaderDropzone"] {{
    background: rgba(255,255,255,.97) !important;
    border: 1.5px dashed #B5121B !important;
    border-radius: 12px !important;
}}

[data-testid="stFileUploaderDropzone"] * {{
    color: var(--uprit-texto) !important;
}}

[data-testid="stFileUploaderDropzone"] button {{
    background: #8F0D1A !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
}}

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {{
    background: #FFFFFF !important;
    color: var(--uprit-texto) !important;
    border: 1px solid #D9C5C9 !important;
    border-radius: 9px !important;
}}

/* Header institucional */
.uprit-header {{
    background: linear-gradient(100deg, #FFFFFF 0%, #FFF9F7 70%, #FBEDEF 100%) !important;
    border: 1px solid #E9D9DC !important;
    border-bottom: 5px solid #8F0D1A !important;
}}

.uprit-accent {{
    background: #8F0D1A !important;
}}

.uprit-title {{
    color: #2F2430 !important;
}}

.uprit-subtitle {{
    color: #75666B !important;
}}

.uprit-slogan {{
    color: #8F0D1A !important;
}}

/* Pasos */
.step {{
    background: rgba(255,255,255,.97) !important;
    border: 1px solid #E8D7DA !important;
}}

.step.active {{
    background: #FFF5F6 !important;
    border-color: #B5121B !important;
}}

.step.active .step-num {{
    background: #B5121B !important;
}}

.step-label {{
    color: #57494E !important;
}}

/* Títulos de sección */
.section-title {{
    background: linear-gradient(90deg, #8F0D1A, #B5121B) !important;
    color: #FFFFFF !important;
    border-radius: 10px 10px 0 0 !important;
}}

/* Tarjetas informativas */
.info-card-grid {{
    display: grid;
    grid-template-columns: minmax(220px, 2fr) minmax(110px, .8fr) minmax(80px, .55fr);
    gap: 12px;
    margin-top: 4px;
}}

.info-card {{
    background: #FFFFFF;
    border: 1px solid #E8D7DA;
    border-top: 4px solid #8F0D1A;
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 4px 14px rgba(67,34,41,.05);
}}

.info-card-label {{
    color: #75666B;
    font-size: 12px;
    font-weight: 650;
    margin-bottom: 4px;
}}

.info-card-value {{
    color: #2F2430;
    font-size: 20px;
    font-weight: 800;
}}

/* Sidebar simplificado */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #FFFFFF 0%, #FAF7F8 100%) !important;
    border-right: 1px solid #E9E2E4 !important;
}}

.sidebar-brand {{
    color: #8F0D1A !important;
    font-size: 18px !important;
    font-weight: 850 !important;
}}

.sidebar-small {{
    color: #75666B !important;
}}

.sidebar-panel {{
    background: #FFF8F8;
    border: 1px solid #ECDADD;
    border-radius: 12px;
    padding: 12px 13px;
    margin: 12px 0;
}}

.sidebar-panel-title {{
    color: #8F0D1A;
    font-weight: 800;
    margin-bottom: 6px;
}}

.sidebar-panel-text {{
    color: #66565B;
    font-size: 13px;
    line-height: 1.45;
}}

/* Único botón funcional del sidebar */
[data-testid="stSidebar"] .stButton > button {{
    width: 100% !important;
    background: linear-gradient(90deg, #8F0D1A, #B5121B) !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    min-height: 42px !important;
    font-weight: 750 !important;
}}

[data-testid="stSidebar"] .stButton > button:hover {{
    background: #720916 !important;
    color: white !important;
}}

/* Métricas */
div[data-testid="stMetric"] {{
    background: #FFFFFF !important;
    color: var(--uprit-texto) !important;
    border: 1px solid #E8D7DA !important;
    border-left: 5px solid #8F0D1A !important;
    border-radius: 10px !important;
}}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricValue"] {{
    color: var(--uprit-texto) !important;
}}

/* Responsive */
@media (max-width: 900px) {{
    .info-card-grid {{
        grid-template-columns: 1fr;
    }}
}}


/* ============================================================
   PARCHE DE LEGIBILIDAD - UPRIT
   ============================================================ */

/* El fondo fotográfico queda más tenue para no competir con el texto */
[data-testid="stAppViewContainer"]::before {{
    opacity: 0.10 !important;
}}

/* Texto general */
[data-testid="stAppViewContainer"] p,
[data-testid="stAppViewContainer"] label,
[data-testid="stAppViewContainer"] span {{
    color: #30252A;
}}

/* MÉTRICAS: etiquetas y valores siempre oscuros */
div[data-testid="stMetric"] {{
    background: rgba(255,255,255,.98) !important;
    border: 1px solid #E3CDD1 !important;
    border-left: 5px solid #9B1020 !important;
    box-shadow: 0 3px 12px rgba(66,31,39,.05) !important;
}}

div[data-testid="stMetric"] [data-testid="stMetricLabel"],
div[data-testid="stMetric"] [data-testid="stMetricLabel"] *,
div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricValue"] * {{
    color: #2D2025 !important;
    opacity: 1 !important;
}}

div[data-testid="stMetric"] [data-testid="stMetricLabel"] {{
    font-weight: 700 !important;
}}

/* ALERTAS: contraste fuerte y fondos sólidos */
div[data-testid="stAlert"] {{
    opacity: 1 !important;
    border-radius: 10px !important;
}}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span,
div[data-testid="stAlert"] div {{
    opacity: 1 !important;
}}

/* Warning */
div[data-testid="stAlert"]:has([data-testid="stAlertContentWarning"]) {{
    background: #FFF4D6 !important;
    border: 1px solid #E7C45B !important;
}}

div[data-testid="stAlert"]:has([data-testid="stAlertContentWarning"]) *,
[data-testid="stAlertContentWarning"] * {{
    color: #5A4300 !important;
}}

/* Info */
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) {{
    background: #EDF5FF !important;
    border: 1px solid #B9D4F5 !important;
}}

div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) *,
[data-testid="stAlertContentInfo"] * {{
    color: #184E82 !important;
}}

/* Success */
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) {{
    background: #EAF7EF !important;
    border: 1px solid #A9D6B8 !important;
}}

div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) *,
[data-testid="stAlertContentSuccess"] * {{
    color: #155D32 !important;
}}

/* Error */
div[data-testid="stAlert"]:has([data-testid="stAlertContentError"]) {{
    background: #FDECEE !important;
    border: 1px solid #E5A7AE !important;
}}

div[data-testid="stAlert"]:has([data-testid="stAlertContentError"]) *,
[data-testid="stAlertContentError"] * {{
    color: #861626 !important;
}}

/* Compatibilidad adicional para versiones de Streamlit donde :has
   no aplique como esperamos: el contenido siempre será oscuro */
[data-testid="stAlertContentWarning"],
[data-testid="stAlertContentWarning"] * {{
    color: #5A4300 !important;
    opacity: 1 !important;
}}

[data-testid="stAlertContentInfo"],
[data-testid="stAlertContentInfo"] * {{
    color: #184E82 !important;
    opacity: 1 !important;
}}

[data-testid="stAlertContentSuccess"],
[data-testid="stAlertContentSuccess"] * {{
    color: #155D32 !important;
    opacity: 1 !important;
}}

[data-testid="stAlertContentError"],
[data-testid="stAlertContentError"] * {{
    color: #861626 !important;
    opacity: 1 !important;
}}

/* EXPANDERS / DIAGNÓSTICOS */
[data-testid="stExpander"] {{
    background: rgba(255,255,255,.96) !important;
    border: 1px solid #E7D9DC !important;
    border-radius: 10px !important;
}}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary *,
[data-testid="stExpander"] details,
[data-testid="stExpander"] p {{
    color: #30252A !important;
    opacity: 1 !important;
}}

/* TABS: visibles aun cuando no estén activas */
button[data-baseweb="tab"] {{
    color: #65545A !important;
    opacity: 1 !important;
}}

button[data-baseweb="tab"] * {{
    color: inherit !important;
    opacity: 1 !important;
}}

button[data-baseweb="tab"][aria-selected="true"] {{
    color: #B5121B !important;
    font-weight: 800 !important;
}}

/* Captions y textos auxiliares */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] * {{
    color: #65545A !important;
    opacity: 1 !important;
}}

/* Dataframes / editores: mantener fondo sólido */
[data-testid="stDataFrame"],
[data-testid="stDataEditor"] {{
    background: #FFFFFF !important;
    border-radius: 10px !important;
}}

/* Botón principal */
.stButton > button[kind="primary"] {{
    background: linear-gradient(90deg, #9B1020, #C7192D) !important;
    color: #FFFFFF !important;
    border: none !important;
}}

.stButton > button[kind="primary"] *,
.stDownloadButton > button * {{
    color: #FFFFFF !important;
}}

/* Los bloques centrales tienen una leve base blanca para que el
   campus siga visible sin perjudicar la lectura */
[data-testid="stMainBlockContainer"] {{
    background: rgba(255,255,255,.22) !important;
}}


/* ============================================================
   BOTONES UPRIT - TEXTO BLANCO Y CONTRASTE FINAL
   ============================================================ */

/* Nueva convalidación */
[data-testid="stSidebar"] .stButton > button,
[data-testid="stSidebar"] .stButton > button *,
[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button span {{
    color: #FFFFFF !important;
    opacity: 1 !important;
}}

[data-testid="stSidebar"] .stButton > button {{
    background: linear-gradient(90deg, #8F0D1A 0%, #C7192D 100%) !important;
    border: none !important;
    font-weight: 800 !important;
}}

[data-testid="stSidebar"] .stButton > button:hover,
[data-testid="stSidebar"] .stButton > button:hover * {{
    background: #720916 !important;
    color: #FFFFFF !important;
}}

/* Botón Upload / Browse files del cargador PDF */
[data-testid="stFileUploaderDropzone"] button,
[data-testid="stFileUploaderDropzone"] button *,
[data-testid="stFileUploaderDropzone"] button p,
[data-testid="stFileUploaderDropzone"] button span {{
    color: #FFFFFF !important;
    opacity: 1 !important;
}}

[data-testid="stFileUploaderDropzone"] button {{
    background: linear-gradient(90deg, #8F0D1A 0%, #B5121B 100%) !important;
    border: none !important;
    font-weight: 750 !important;
}}

[data-testid="stFileUploaderDropzone"] button:hover,
[data-testid="stFileUploaderDropzone"] button:hover * {{
    background: #720916 !important;
    color: #FFFFFF !important;
}}


/* ============================================================
   MESA DE REVISIÓN - MÁS ESPACIO Y LEGIBILIDAD
   ============================================================ */

[data-testid="stDataEditor"] {{
    width: 100% !important;
}}

[data-testid="stDataEditor"] > div {{
    width: 100% !important;
}}

[data-testid="stDataFrame"] {{
    width: 100% !important;
}}

/* Botones de zoom del certificado */
button[kind="secondary"] {{
    border-radius: 9px !important;
}}

/* Títulos de la mesa de revisión */
h3 {{
    color: #2F2430 !important;
}}


/* ============================================================
   REVISIÓN DE PROFORMA - DISEÑO COMPACTO UPRIT
   ============================================================ */

.revision-title-box {{
    background: linear-gradient(90deg, #8F0D1A 0%, #B5121B 100%);
    color: #FFFFFF;
    border-radius: 12px;
    padding: 14px 18px;
    margin: 8px 0 12px 0;
    box-shadow: 0 4px 12px rgba(143,13,26,.12);
}}

.revision-title-box .rt-main {{
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 3px;
}}

.revision-title-box .rt-sub {{
    font-size: 13px;
    opacity: .92;
}}

.revision-header {{
    display: grid;
    grid-template-columns: 1.45fr 2.2fr .65fr .75fr;
    gap: 10px;
    background: #2F2430;
    color: #FFFFFF;
    border-radius: 10px;
    padding: 10px 12px;
    margin: 10px 0 6px 0;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .2px;
}}

.competencia-badge {{
    display: inline-block;
    background: #FBEDEF;
    color: #8F0D1A;
    border: 1px solid #E7C8CE;
    border-radius: 999px;
    padding: 3px 9px;
    font-size: 11px;
    font-weight: 700;
    margin-top: 4px;
}}

.curso-uprit-name {{
    font-size: 14px;
    font-weight: 800;
    color: #2F2430;
    line-height: 1.25;
    margin-bottom: 2px;
}}

.recomendacion-box {{
    margin-top: 5px;
    padding: 5px 8px;
    border-left: 3px solid #D19B16;
    background: #FFF8DA;
    border-radius: 5px;
    color: #5C470A;
    font-size: 11px;
    line-height: 1.3;
}}

[data-testid="stMetric"] {{
    min-height: 74px !important;
    padding: 8px 10px !important;
}}

[data-testid="stMetricLabel"] {{
    font-size: 11px !important;
}}

[data-testid="stMetricValue"] {{
    font-size: 24px !important;
}}

/* Compactar cada fila de revisión */
div[data-testid="stVerticalBlockBorderWrapper"]:has(.curso-uprit-name) {{
    background: rgba(255,255,255,.97) !important;
    border: 1px solid #E5D7DA !important;
    border-radius: 10px !important;
    box-shadow: 0 2px 8px rgba(66,31,39,.04) !important;
    margin-bottom: 6px !important;
}}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.curso-uprit-name):hover {{
    border-color: #C7192D !important;
    box-shadow: 0 4px 12px rgba(143,13,26,.08) !important;
}}

/* Selectores más claros y sobrios en revisión */
div[data-baseweb="select"] > div {{
    min-height: 42px !important;
    border-radius: 8px !important;
}}

.revision-footer-note {{
    background: #EEF5FF;
    color: #204E7A;
    border: 1px solid #C6DAF2;
    border-radius: 10px;
    padding: 10px 12px;
    font-size: 12px;
    margin-top: 10px;
}}


/* ============================================================
   DESPLEGABLES DEL COORDINADOR - EDITABLES
   ============================================================ */
[data-testid="stSelectbox"] {{
    opacity: 1 !important;
}}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
    cursor: pointer !important;
    border: 1px solid #B5121B !important;
    background: #FFFFFF !important;
}}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover {{
    border-color: #8F0D1A !important;
    box-shadow: 0 0 0 2px rgba(181,18,27,.10) !important;
}}

[data-testid="stSelectbox"] div[data-baseweb="select"] span {{
    color: #2F2430 !important;
}}

[data-testid="stSelectbox"] svg {{
    opacity: 1 !important;
    color: #B5121B !important;
    fill: #B5121B !important;
}}


/* ============================================================
   BOTÓN EDITAR NUEVAMENTE - UPRIT
   ============================================================ */

div.stButton > button[kind="secondary"] {{
    background: #B5121B !important;
    color: #FFFFFF !important;
    border: 1px solid #B5121B !important;
    font-weight: 700 !important;
}}

div.stButton > button[kind="secondary"] p,
div.stButton > button[kind="secondary"] span {{
    color: #FFFFFF !important;
}}

div.stButton > button[kind="secondary"]:hover {{
    background: #970D1C !important;
    color: #FFFFFF !important;
    border-color: #970D1C !important;
}}

div.stButton > button[kind="secondary"]:hover p,
div.stButton > button[kind="secondary"]:hover span {{
    color: #FFFFFF !important;
}}


/* FOOTER - TEXTO BLANCO */
.footer-uprit {{
    background: #B5121B !important;
    color: #FFFFFF !important;
    justify-content: center !important;
    text-align: center !important;
    font-weight: 700 !important;
}}

.footer-uprit span {{
    color: #FFFFFF !important;
}}


/* ============================================================
   CONTADOR DE EXÁMENES DE SUFICIENCIA
   ============================================================ */

.suficiencia-counter {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    border-radius: 14px;
    padding: 14px 18px;
    margin: 12px 0 16px 0;
    border: 1px solid transparent;
    box-shadow: 0 3px 10px rgba(0,0,0,.05);
}}

.suficiencia-counter .sc-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.suficiencia-counter .sc-number {{
    min-width: 58px;
    height: 58px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    font-weight: 900;
    background: rgba(255,255,255,.88);
}}

.suficiencia-counter .sc-title {{
    font-size: 15px;
    font-weight: 800;
    line-height: 1.2;
}}

.suficiencia-counter .sc-sub {{
    font-size: 12px;
    margin-top: 4px;
    opacity: .92;
}}

.suficiencia-counter .sc-status {{
    font-size: 12px;
    font-weight: 800;
    border-radius: 999px;
    padding: 7px 12px;
    background: rgba(255,255,255,.78);
    white-space: nowrap;
}}

.suf-green {{
    background: #E9F8EE;
    border-color: #A9DDB8;
    color: #176B35;
}}

.suf-yellow {{
    background: #FFF7D6;
    border-color: #E7C95B;
    color: #7A5A00;
}}

.suf-orange {{
    background: #FFF0DA;
    border-color: #E9A84C;
    color: #8A4A00;
}}

.suf-red {{
    background: #FDE7E7;
    border-color: #E27A7A;
    color: #9D1C1C;
}}


    @media (max-width: 1200px) {{
        .info-card-grid {{
            grid-template-columns: 1fr 1fr;
        }}

        .info-card-grid .info-card:first-child {{
            grid-column: 1 / -1;
        }}
    }}


    @media (max-width: 1180px) {{
        .stepper {{
            grid-template-columns: repeat(3, 1fr);
        }}
    }}

    @media (max-width: 760px) {{
        .stepper {{
            grid-template-columns: 1fr;
        }}
    }}

</style>
    """,
    unsafe_allow_html=True
)



def formatear_periodo_convalidable(valor):
    if valor is None or valor == "":
        return "No definido"

    try:
        numero = float(valor)
    except (TypeError, ValueError):
        texto = str(valor).strip()
        return texto if texto else "No definido"

    if numero == 1:
        return "1 año"

    if numero.is_integer():
        return f"{int(numero)} años"

    return f"{numero:g} años"


@st.cache_data(show_spinner=False, ttl=120)
def buscar_alumno_cache(nombre_detectado, ruta_excel):
    return buscar_alumno(
        nombre_detectado,
        ruta_excel=ruta_excel
    )


@st.cache_data(show_spinner=False, max_entries=24)
def renderizar_pagina_pdf_cache(pdf_bytes, pagina_indice, factor_render):
    documento_pdf = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    pagina = documento_pdf.load_page(
        pagina_indice
    )

    pix = pagina.get_pixmap(
        matrix=pymupdf.Matrix(
            factor_render,
            factor_render
        ),
        alpha=False
    )

    imagen_png = pix.tobytes("png")
    documento_pdf.close()

    return imagen_png


# ============================================================
# COMPONENTES VISUALES
# ============================================================

def mostrar_header():

    if logo_b64:
        extension_logo = (
            "jpeg"
            if RUTA_LOGO
            and RUTA_LOGO.suffix.lower() in [".jpg", ".jpeg"]
            else "png"
        )

        logo_html = (
            '<img class="uprit-logo" '
            f'src="data:image/{extension_logo};base64,{logo_b64}">'
        )
    else:
        logo_html = (
            '<div class="uprit-logo-fallback">UPRIT</div>'
        )

    html = (
        '<div class="uprit-header">'
        + logo_html
        + '<div class="uprit-accent"></div>'
        + '<div class="uprit-header-text">'
        + '<div class="uprit-title">SISTEMA DE CONVALIDACIONES ACADÉMICAS</div>'
        + '<div class="uprit-subtitle">Evaluación de asignaturas, competencias y suficiencias</div>'
        + '</div>'
        + '<div class="uprit-slogan">DISCIPLINA<br>INNOVACIÓN<br>EXCELENCIA</div>'
        + '</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def mostrar_stepper(paso_activo):

    etiquetas = [
        "Datos y archivo",
        "Análisis del certificado",
        "Convalidaciones",
        "Aprobación del coordinador",
        "Descargar proforma"
    ]

    partes = ['<div class="stepper">']

    for numero, etiqueta in enumerate(
        etiquetas,
        start=1
    ):
        clase = (
            "step active"
            if numero == paso_activo
            else "step"
        )

        partes.append(
            f'<div class="{clase}">'
            f'<span class="step-num">{numero}</span>'
            f'<span class="step-label">{etiqueta}</span>'
            '</div>'
        )

    partes.append('</div>')

    st.markdown(
        "".join(partes),
        unsafe_allow_html=True
    )


def titulo_seccion(texto):

    html = (
        f'<div class="section-title">{texto}</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# VISOR PDF Y REVISIÓN DEL COORDINADOR
# ============================================================

@st.cache_data(show_spinner=False, max_entries=12)
def renderizar_pagina_pdf_local_cache(
    ruta_pdf,
    mtime_pdf,
    pagina_indice,
    factor_render=1.6
):
    """
    Renderiza páginas del reglamento solo cuando cambia el archivo,
    la página o el factor de renderizado.
    """
    documento_pdf = pymupdf.open(
        ruta_pdf
    )

    total_paginas = len(
        documento_pdf
    )

    pagina = documento_pdf.load_page(
        pagina_indice
    )

    pix = pagina.get_pixmap(
        matrix=pymupdf.Matrix(
            factor_render,
            factor_render
        ),
        alpha=False
    )

    imagen = pix.tobytes(
        "png"
    )

    documento_pdf.close()

    return total_paginas, imagen


def mostrar_pdf_local(
    ruta_pdf,
    altura=700
):
    """
    Muestra un PDF local dentro de la aplicación.
    Se utiliza para el Reglamento General de Convalidaciones UPRIT.
    """

    if not ruta_pdf or not os.path.exists(
        ruta_pdf
    ):
        st.warning(
            "No se encontró el archivo del reglamento."
        )
        return

    try:
        mtime_pdf = os.path.getmtime(
            ruta_pdf
        )

        documento_temporal = pymupdf.open(
            ruta_pdf
        )

        total_paginas = len(
            documento_temporal
        )

        documento_temporal.close()

        pagina_elegida = st.selectbox(
            "Página del reglamento",
            options=list(
                range(
                    1,
                    total_paginas + 1
                )
            ),
            key="pagina_reglamento_uprit"
        )

        _, imagen_reglamento = renderizar_pagina_pdf_local_cache(
            ruta_pdf,
            mtime_pdf,
            pagina_elegida - 1,
            1.6
        )

        st.image(
            imagen_reglamento,
            use_container_width=True
        )

    except Exception as error:
        st.error(
            "No se pudo visualizar el reglamento."
        )
        st.caption(
            str(
                error
            )
        )



def mostrar_pdf_subido(
    archivo,
    altura=820
):
    """
    Visor del certificado con ampliación REAL.

    En vez de escalar la imagen dentro del ancho de la columna,
    renderiza la página seleccionada a alta resolución dentro de
    un contenedor HTML con scroll horizontal y vertical.

    El coordinador puede elegir:
    - página;
    - 100%, 150%, 200%, 250% o 300%.
    """

    if archivo is None:
        st.info(
            "No hay certificado cargado."
        )
        return

    try:
        pdf_bytes = archivo.getvalue()

        documento_pdf = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        total_paginas = len(
            documento_pdf
        )

        if total_paginas == 0:
            st.warning(
                "El PDF no contiene páginas visibles."
            )
            return

        st.caption(
            f"Certificado cargado: {total_paginas} página(s)."
        )

        c_pag, c_zoom = st.columns(
            [
                1,
                1
            ]
        )

        with c_pag:
            pagina_elegida = st.selectbox(
                "Página",
                options=list(
                    range(
                        1,
                        total_paginas + 1
                    )
                ),
                key="pagina_certificado_revision"
            )

        with c_zoom:
            zoom_porcentaje = st.selectbox(
                "🔎 Ampliación",
                options=[
                    100,
                    150,
                    200,
                    250,
                    300
                ],
                index=2,
                format_func=lambda x: f"{x}%",
                key="zoom_certificado_revision"
            )

        # Render alto para mantener legibilidad de notas pequeñas.
        factor_render = 2.4

        imagen_png = renderizar_pagina_pdf_cache(
            pdf_bytes,
            pagina_elegida - 1,
            factor_render
        )

        imagen_b64 = base64.b64encode(
            imagen_png
        ).decode(
            "utf-8"
        )

        ancho_visual = int(
            720
            * (
                zoom_porcentaje
                / 100
            )
        )

        html = f"""
        <div style="
            width:100%;
            height:{altura}px;
            overflow:auto;
            background:#ffffff;
            border:1px solid #e3d4d7;
            border-radius:10px;
            padding:10px;
        ">
            <img
                src="data:image/png;base64,{imagen_b64}"
                style="
                    width:{ancho_visual}px;
                    max-width:none;
                    height:auto;
                    display:block;
                "
            />
        </div>
        """

        components.html(
            html,
            height=altura + 20,
            scrolling=False
        )

        st.caption(
            "Use las barras de desplazamiento del visor para "
            "recorrer la página ampliada."
        )

        documento_pdf.close()

    except Exception as error:
        st.error(
            "No se pudo visualizar el certificado PDF."
        )
        st.caption(
            str(
                error
            )
        )


def valor_editor_a_python(valor):
    if pd.isna(valor):
        return ""
    return valor



def corregir_competencias_resultado_desde_formato(
    resultado,
    ruta_formato
):
    """
    Corrige la competencia de cada curso usando la estructura REAL
    del Word.

    Es especialmente importante en Educación, donde las competencias
    están en celdas verticalmente combinadas. El motor puede leer bien
    la asignatura, pero perder el texto de competencia en las filas
    interiores de la combinación.
    """
    if not isinstance(
        resultado,
        dict
    ):
        return resultado

    try:
        mapa = extraer_mapa_competencias_desde_formato(
            ruta_formato
        )
    except Exception:
        mapa = {}

    if not mapa:
        return resultado

    # Estructura de la proforma.
    for item in resultado.get(
        "estructura_proforma",
        []
    ) or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        curso = _normalizar_nombre_carrera(
            item.get(
                "curso",
                ""
            )
        )

        competencia = mapa.get(
            curso
        )

        if competencia:
            item[
                "competencia"
            ] = competencia

    # Equivalencias ya propuestas por el motor.
    for item in resultado.get(
        "convalidaciones",
        []
    ) or []:

        if not isinstance(
            item,
            dict
        ):
            continue

        curso = _normalizar_nombre_carrera(
            item.get(
                "curso_destino",
                ""
            )
        )

        competencia = mapa.get(
            curso
        )

        if competencia:
            item[
                "competencia"
            ] = competencia

    resultado[
        "mapa_competencias_formato"
    ] = mapa

    return resultado


def construir_tabla_revision_completa(
    resultado
):
    """
    Construye una fila por CADA curso de la proforma.

    Si existe convalidación:
        muestra curso de origen y notas.

    Si NO existe:
        deja Asignatura convalidante y Nota parcial en blanco
        para que el coordinador pueda completarlas manualmente.

    También muestra una recomendación, cuando el motor académico
    haya generado una sugerencia para ese curso.
    """

    estructura = resultado.get(
        "estructura_proforma",
        []
    )

    convalidaciones_resultado = resultado.get(
        "convalidaciones",
        []
    )

    recomendaciones = resultado.get(
        "recomendaciones_caso_especial",
        []
    )

    mapa_convalidaciones = {}

    for item in convalidaciones_resultado:
        if not isinstance(
            item,
            dict
        ):
            continue

        destino = _normalizar_nombre_carrera(
            item.get(
                "curso_destino",
                ""
            )
        )

        if not destino:
            continue

        # Preferir la equivalencia que realmente tenga curso de origen.
        existente = mapa_convalidaciones.get(
            destino
        )

        if (
            existente is None
            or (
                valor_vacio(
                    existente.get(
                        "curso_origen"
                    )
                )
                and not valor_vacio(
                    item.get(
                        "curso_origen"
                    )
                )
            )
        ):
            mapa_convalidaciones[
                destino
            ] = item

    mapa_recomendaciones = {
        _normalizar_nombre_carrera(
            item.get(
                "curso_destino",
                ""
            )
        ): item
        for item in recomendaciones
        if isinstance(
            item,
            dict
        )
    }

    filas = []

    for curso_info in estructura:

        if not isinstance(
            curso_info,
            dict
        ):
            continue

        curso_destino = str(
            curso_info.get(
                "curso",
                ""
            )
            or ""
        ).strip()

        if not curso_destino:
            continue

        destino_norm = _normalizar_nombre_carrera(
            curso_destino
        )

        equivalencia = mapa_convalidaciones.get(
            destino_norm,
            {}
        )

        recomendacion = mapa_recomendaciones.get(
            destino_norm,
            {}
        )

        curso_sugerido = str(
            recomendacion.get(
                "curso_sugerido",
                ""
            )
            or ""
        ).strip()

        afinidad_sugerida = str(
            recomendacion.get(
                "afinidad",
                ""
            )
            or ""
        ).strip()

        sugerencia_texto = ""

        if curso_sugerido:
            sugerencia_texto = curso_sugerido

            if afinidad_sugerida:
                sugerencia_texto += (
                    f" ({afinidad_sugerida})"
                )

        elif recomendacion:
            sugerencia_texto = str(
                recomendacion.get(
                    "recomendacion",
                    ""
                )
                or ""
            ).strip()

        filas.append({
            "Competencia":
                (
                    curso_info.get(
                        "competencia"
                    )
                    or equivalencia.get(
                        "competencia"
                    )
                    or ""
                ),
            "Curso UPRIT":
                curso_destino,
            "Asignatura convalidante":
                (
                    equivalencia.get(
                        "curso_origen"
                    )
                    or ""
                ),
            "Nota parcial":
                (
                    equivalencia.get(
                        "nota"
                    )
                    if not valor_vacio(
                        equivalencia.get(
                            "nota"
                        )
                    )
                    else ""
                ),
            "Nota convalidante":
                (
                    equivalencia.get(
                        "nota_convalidante"
                    )
                    if not valor_vacio(
                        equivalencia.get(
                            "nota_convalidante"
                        )
                    )
                    else ""
                ),
            "Afinidad":
                (
                    equivalencia.get(
                        "afinidad"
                    )
                    or ""
                ),
            "Estado":
                (
                    equivalencia.get(
                        "estado"
                    )
                    or (
                        "PENDIENTE DE REVISIÓN DEL COORDINADOR"
                        if valor_vacio(
                            equivalencia.get(
                                "curso_origen"
                            )
                        )
                        else ""
                    )
                ),
            "Recomendación":
                sugerencia_texto,
            "Justificación":
                (
                    equivalencia.get(
                        "justificacion"
                    )
                    or ""
                )
        })

    return pd.DataFrame(
        filas
    )


def marcar_revision_modificada():
    """
    Si el coordinador cambia una equivalencia:
    - se invalida la aprobación previa;
    - se invalidan documentos generados;
    - se fuerza el recálculo visual del contador de suficiencias.
    """
    st.session_state.pop("aprobacion_coordinador", None)
    st.session_state.pop("ruta_word_generado", None)
    st.session_state.pop("ruta_reporte_especial", None)
    st.session_state.pop("ruta_constancia_aprobacion", None)
    st.session_state.pop(
        "cantidad_suficiencias_pendientes_revision",
        None
    )



def contar_suficiencias_pendientes(
    df_revision
):
    """
    Cuenta los cursos UPRIT que todavía requerirían examen de
    suficiencia/revisión manual.

    Se considera pendiente cuando:
    - no tiene asignatura convalidante; o
    - no tiene nota parcial real.

    Se cuenta por curso UPRIT para evitar duplicados.
    """

    if (
        df_revision is None
        or df_revision.empty
    ):
        return 0

    pendientes = set()

    for _, fila in df_revision.iterrows():

        curso_uprit = str(
            fila.get(
                "Curso UPRIT",
                ""
            )
            or ""
        ).strip()

        if not curso_uprit:
            continue

        asignatura = str(
            fila.get(
                "Asignatura convalidante",
                ""
            )
            or ""
        ).strip()

        nota = fila.get(
            "Nota parcial",
            ""
        )

        if (
            not asignatura
            or valor_vacio(
                nota
            )
        ):
            pendientes.add(
                _normalizar_nombre_carrera(
                    curso_uprit
                )
            )

    return len(
        pendientes
    )


def construir_contador_suficiencias(
    cantidad
):
    """
    Semáforo de suficiencias:
    0-3 = verde
    4-5 = amarillo
    6-7 = naranja
    8+  = rojo
    """

    cantidad = int(
        cantidad
        or 0
    )

    if cantidad <= 3:
        clase = "suf-green"
        estado = "ADECUADO"
        mensaje = (
            "El expediente se encuentra dentro de un rango "
            "favorable de suficiencias."
        )

    elif cantidad <= 5:
        clase = "suf-yellow"
        estado = "DENTRO DEL MÁXIMO"
        mensaje = (
            "Se mantiene dentro del máximo ordinario de 5 "
            "exámenes de suficiencia."
        )

    elif cantidad <= 7:
        clase = "suf-orange"
        estado = "REVISIÓN ESPECIAL"
        mensaje = (
            "Supera el umbral ordinario de 5. Revise las "
            "recomendaciones antes de aprobar."
        )

    else:
        clase = "suf-red"
        estado = "SUPERA 7"
        mensaje = (
            "Existen más de 7 cursos sin equivalencia completa. "
            "Debe reducirse el número mediante revisión académica."
        )

    return (
        f'<div class="suficiencia-counter {clase}">'
        f'<div class="sc-left">'
        f'<div class="sc-number">{cantidad}</div>'
        f'<div>'
        f'<div class="sc-title">Exámenes de suficiencia pendientes</div>'
        f'<div class="sc-sub">{mensaje}</div>'
        f'</div>'
        f'</div>'
        f'<div class="sc-status">{estado}</div>'
        f'</div>'
    )



def preparar_revision_con_selectores(
    resultado,
    cursos_certificado
):
    """
    Prepara la revisión del coordinador.

    Para cada curso UPRIT:
    - conserva la equivalencia ya propuesta;
    - crea opciones de cursos del certificado todavía no usados;
    - prioriza la recomendación académica;
    - incorpora la nota real del certificado en la etiqueta;
    - evita repetir una asignatura de origen.
    """

    df = construir_tabla_revision_completa(
        resultado
    )

    if df.empty:
        return df, {}, {}

    mapa_notas = {}
    nombres_originales = {}

    for item in cursos_certificado or []:
        if not isinstance(item, dict):
            continue

        nombre = str(
            item.get("curso", "")
            or ""
        ).strip()

        if not nombre:
            continue

        clave = _normalizar_nombre_carrera(
            nombre
        )

        mapa_notas[clave] = item.get(
            "nota"
        )
        nombres_originales[clave] = nombre

    usados = set()

    for valor in df[
        "Asignatura convalidante"
    ].fillna("").astype(str):

        valor = valor.strip()

        if valor:
            usados.add(
                _normalizar_nombre_carrera(
                    valor
                )
            )

    opciones_por_fila = {}
    etiqueta_a_curso = {}

    for indice, fila in df.iterrows():

        actual = str(
            fila.get(
                "Asignatura convalidante",
                ""
            )
            or ""
        ).strip()

        recomendacion = str(
            fila.get(
                "Recomendación",
                ""
            )
            or ""
        ).strip()

        # La recomendación puede venir como "CURSO (ALTA)".
        recomendacion_limpia = re.sub(
            r"\s+\((?:MUY ALTA|ALTA|MEDIA|BAJA|\d+(?:\.\d+)?%?)\)\s*$",
            "",
            recomendacion,
            flags=re.IGNORECASE
        ).strip()

        claves_prioridad = []

        if actual:
            claves_prioridad.append(
                _normalizar_nombre_carrera(
                    actual
                )
            )

        if recomendacion_limpia:
            clave_rec = _normalizar_nombre_carrera(
                recomendacion_limpia
            )
            if clave_rec in nombres_originales:
                claves_prioridad.append(
                    clave_rec
                )

        # Añadir el resto de cursos aún no utilizados.
        claves_disponibles = []

        for clave in nombres_originales:

            if clave in usados:
                # El curso actual de la fila sí debe seguir disponible
                # en su propia lista.
                if not (
                    actual
                    and clave
                    == _normalizar_nombre_carrera(
                        actual
                    )
                ):
                    continue

            claves_disponibles.append(
                clave
            )

        claves_finales = []

        for clave in (
            claves_prioridad
            + claves_disponibles
        ):
            if (
                clave
                and clave not in claves_finales
            ):
                claves_finales.append(
                    clave
                )

        etiquetas = [
            "— SIN ASIGNAR —"
        ]

        etiqueta_a_curso[
            "— SIN ASIGNAR —"
        ] = ""

        for clave in claves_finales:

            nombre = nombres_originales[
                clave
            ]

            nota = mapa_notas.get(
                clave
            )

            etiqueta = (
                f"{nombre} | Nota: {nota}"
                if not valor_vacio(
                    nota
                )
                else nombre
            )

            etiquetas.append(
                etiqueta
            )

            etiqueta_a_curso[
                etiqueta
            ] = nombre

        opciones_por_fila[
            indice
        ] = etiquetas

    return (
        df,
        opciones_por_fila,
        {
            "mapa_notas":
                mapa_notas,
            "etiqueta_a_curso":
                etiqueta_a_curso
        }
    )


def recalcular_notas_competencia(
    filas
):
    """
    Recalcula la nota convalidante por competencia.

    Regla:
    - usa únicamente notas parciales reales;
    - promedio aritmético con redondeo convencional;
    - máximo 17;
    - si una competencia tiene DOS O MÁS cursos todavía sin
      equivalencia/nota, la nota convalidante queda vacía;
    - con cero o un faltante, se conserva el promedio de las
      equivalencias disponibles.

    Las filas sin competencia NO se agrupan entre sí: cada una se
    trata de forma independiente para evitar promedios falsos.
    """

    df = filas.copy()

    for columna_nota in [
        "Nota parcial",
        "Nota convalidante"
    ]:
        if columna_nota in df.columns:
            df[columna_nota] = df[columna_nota].astype(
                "object"
            )

    if df.empty:
        return df

    # Crear una clave de agrupación segura.
    claves_grupo = []

    for indice, fila in df.iterrows():

        competencia = str(
            fila.get(
                "Competencia",
                ""
            )
            or ""
        ).strip()

        if competencia:
            clave = (
                "COMP::"
                + _normalizar_nombre_carrera(
                    competencia
                )
            )
        else:
            # No unir todos los vacíos en una falsa competencia.
            clave = f"FILA::{indice}"

        claves_grupo.append(
            clave
        )

    df[
        "_clave_competencia"
    ] = claves_grupo

    for clave in df[
        "_clave_competencia"
    ].unique():

        mascara = (
            df[
                "_clave_competencia"
            ]
            == clave
        )

        filas_grupo = df.loc[
            mascara
        ]

        faltantes = 0

        for _, fila in filas_grupo.iterrows():

            asignatura = str(
                fila.get(
                    "Asignatura convalidante",
                    ""
                )
                or ""
            ).strip()

            nota = fila.get(
                "Nota parcial",
                ""
            )

            if (
                not asignatura
                or valor_vacio(
                    nota
                )
            ):
                faltantes += 1

        notas = pd.to_numeric(
            filas_grupo[
                "Nota parcial"
            ],
            errors="coerce"
        ).dropna()

        # Con 2 o más faltantes la competencia todavía no puede
        # recibir una nota convalidante.
        if (
            faltantes >= 2
            or notas.empty
        ):
            promedio = None

        else:

            promedio_decimal = float(
                notas.mean()
            )

            promedio = int(
                promedio_decimal
                + 0.5
            )

            promedio = min(
                promedio,
                17
            )

        df.loc[
            mascara,
            "Nota convalidante"
        ] = (
            promedio
            if promedio is not None
            else ""
        )

    df = df.drop(
        columns=[
            "_clave_competencia"
        ],
        errors="ignore"
    )

    return df



def aplicar_ediciones_tabla_completa(
    resultado,
    df_editado
):
    """
    Convierte la tabla completa editada por el coordinador en la lista
    que se enviará al generador Word.

    Permite crear una equivalencia manual para una fila que originalmente
    estaba en blanco, sin alterar el curso UPRIT ni la competencia.
    """

    estructura = resultado.get(
        "estructura_proforma",
        []
    )

    mapa_estructura = {
        _normalizar_nombre_carrera(
            item.get(
                "curso",
                ""
            )
        ): item
        for item in estructura
        if isinstance(
            item,
            dict
        )
        and item.get(
            "curso"
        )
    }

    salida = []

    for _, fila in df_editado.iterrows():

        curso_destino = str(
            fila.get(
                "Curso UPRIT",
                ""
            )
            or ""
        ).strip()

        if not curso_destino:
            continue

        destino_norm = _normalizar_nombre_carrera(
            curso_destino
        )

        curso_info = mapa_estructura.get(
            destino_norm,
            {}
        )

        curso_origen = str(
            valor_editor_a_python(
                fila.get(
                    "Asignatura convalidante",
                    ""
                )
            )
            or ""
        ).strip()

        nota = valor_editor_a_python(
            fila.get(
                "Nota parcial",
                ""
            )
        )

        nota_convalidante = valor_editor_a_python(
            fila.get(
                "Nota convalidante",
                ""
            )
        )

        item = {
            "competencia":
                (
                    str(
                        fila.get(
                            "Competencia",
                            ""
                        )
                        or ""
                    ).strip()
                    or curso_info.get(
                        "competencia",
                        ""
                    )
                ),
            "curso_destino":
                curso_destino,
            "curso_origen":
                curso_origen,
            "nota":
                nota,
            "nota_convalidante":
                nota_convalidante,
            "afinidad":
                str(
                    fila.get(
                        "Afinidad",
                        ""
                    )
                    or ""
                ).strip(),
            "estado":
                str(
                    fila.get(
                        "Estado",
                        ""
                    )
                    or ""
                ).strip(),
            "justificacion":
                str(
                    fila.get(
                        "Justificación",
                        ""
                    )
                    or ""
                ).strip(),
            "tipo_equivalencia":
                (
                    "REVISIÓN MANUAL DEL COORDINADOR"
                    if curso_origen
                    else ""
                )
        }

        salida.append(
            item
        )

    return salida


def aplicar_ediciones_tabla(
    convalidaciones_originales,
    df_editado
):
    mapa = {}

    for _, fila in df_editado.iterrows():

        destino = _normalizar_nombre_carrera(
            fila.get(
                "Curso UPRIT",
                ""
            )
        )

        if destino:
            mapa[destino] = fila

    salida = []

    for item in convalidaciones_originales:

        nuevo = dict(item)

        destino = _normalizar_nombre_carrera(
            item.get(
                "curso_destino",
                ""
            )
        )

        fila = mapa.get(destino)

        if fila is not None:

            nuevo["curso_origen"] = str(
                valor_editor_a_python(
                    fila.get(
                        "Asignatura convalidante",
                        ""
                    )
                )
                or ""
            ).strip()

            nuevo["nota"] = valor_editor_a_python(
                fila.get(
                    "Nota parcial",
                    ""
                )
            )

            nuevo["nota_convalidante"] = valor_editor_a_python(
                fila.get(
                    "Nota convalidante",
                    ""
                )
            )

            if "Estado" in df_editado.columns:
                nuevo["estado"] = str(
                    valor_editor_a_python(
                        fila.get(
                            "Estado",
                            ""
                        )
                    )
                    or ""
                ).strip()

            if "Justificación" in df_editado.columns:
                nuevo["justificacion"] = str(
                    valor_editor_a_python(
                        fila.get(
                            "Justificación",
                            ""
                        )
                    )
                    or ""
                ).strip()

        salida.append(nuevo)

    return salida


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def valor_vacio(valor):

    if valor is None:
        return True

    if isinstance(
        valor,
        float
    ) and pd.isna(
        valor
    ):
        return True

    return str(
        valor
    ).strip() == ""


def _normalizar_nombre_carrera(texto):

    if texto is None:
        return ""

    texto = unicodedata.normalize(
        "NFD",
        str(
            texto
        )
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(
            caracter
        ) != "Mn"
    )

    return " ".join(
        texto.upper().split()
    )


def es_convalidacion_real(item):

    if not isinstance(
        item,
        dict
    ):
        return False

    return (
        not valor_vacio(
            item.get(
                "curso_destino"
            )
        )
        and
        not valor_vacio(
            item.get(
                "curso_origen"
            )
        )
    )


def obtener_estado_competencia(item):

    estado = (
        item.get(
            "estado_competencia"
        )
        or item.get(
            "estado"
        )
        or ""
    )

    return _normalizar_nombre_carrera(
        estado
    )


def puede_tener_nota_convalidante(item):

    estado = obtener_estado_competencia(
        item
    )

    return "SUFICIENCIA" not in estado


def validar_resultado_antes_de_word(
    convalidaciones
):

    reales = [
        item
        for item in convalidaciones
        if es_convalidacion_real(
            item
        )
    ]

    sin_nota_parcial = [
        item
        for item in reales
        if valor_vacio(
            item.get(
                "nota"
            )
        )
    ]

    sin_nota_convalidante = [
        item
        for item in reales
        if (
            puede_tener_nota_convalidante(
                item
            )
            and valor_vacio(
                item.get(
                    "nota_convalidante"
                )
            )
        )
    ]

    return {
        "reales":
            reales,
        "cantidad_reales":
            len(
                reales
            ),
        "sin_nota_parcial":
            sin_nota_parcial,
        "sin_nota_convalidante":
            sin_nota_convalidante,
        "puede_generar":
            True
    }


def _buscar_archivo_local(
    carpeta,
    nombre_esperado
):

    if not os.path.isdir(
        carpeta
    ):
        return None

    esperado = (
        nombre_esperado
        .lower()
        .strip()
    )

    for nombre in os.listdir(
        carpeta
    ):

        if (
            nombre
            .lower()
            .strip()
            == esperado
        ):

            return os.path.join(
                carpeta,
                nombre
            )

    return None


def _cargar_carreras_respaldo(
    carreras_actuales
):
    """
    Busca configuracion.json de forma RECURSIVA dentro de /Carreras.

    Esto permite estructuras como:

    Carreras/
        Administración de Empresas/
            2 años/
                configuracion.json
                formato.docx
                alumnos.xlsx
            2.5 años/
                configuracion.json
                formato.docx
                alumnos.xlsx
    """

    carreras = dict(
        carreras_actuales
    )

    base_dir = os.path.dirname(
        os.path.abspath(
            __file__
        )
    )

    carpeta_carreras = os.path.join(
        base_dir,
        "Carreras"
    )

    if not os.path.isdir(
        carpeta_carreras
    ):
        return carreras

    nombres_ya_cargados = {
        _normalizar_nombre_carrera(
            nombre
        )
        for nombre in carreras.keys()
    }

    for raiz, _, archivos in os.walk(
        carpeta_carreras
    ):

        nombres_archivos = {
            nombre.lower().strip():
                nombre
            for nombre in archivos
        }

        if "configuracion.json" not in nombres_archivos:
            continue

        ruta_config = os.path.join(
            raiz,
            nombres_archivos[
                "configuracion.json"
            ]
        )

        try:
            with open(
                ruta_config,
                "r",
                encoding="utf-8-sig"
            ) as archivo:
                config = json.load(
                    archivo
                )
        except Exception:
            config = {}

        nombre_carpeta = os.path.basename(
            raiz
        )

        nombre_carrera = (
            str(
                config.get(
                    "nombre",
                    nombre_carpeta
                )
            ).strip()
            or nombre_carpeta
        )

        clave_normalizada = (
            _normalizar_nombre_carrera(
                nombre_carrera
            )
        )

        if clave_normalizada in nombres_ya_cargados:
            continue

        nombre_formato = config.get(
            "formato",
            "formato.docx"
        )

        nombre_alumnos = config.get(
            "archivo_alumnos",
            "alumnos.xlsx"
        )

        ruta_formato_local = (
            _buscar_archivo_local(
                raiz,
                nombre_formato
            )
            or _buscar_archivo_local(
                raiz,
                "formato.docx"
            )
        )

        ruta_alumnos_local = (
            _buscar_archivo_local(
                raiz,
                nombre_alumnos
            )
            or _buscar_archivo_local(
                raiz,
                "alumnos.xlsx"
            )
        )

        config[
            "nombre"
        ] = nombre_carrera

        config[
            "carpeta"
        ] = raiz

        config[
            "ruta_formato"
        ] = (
            ruta_formato_local
            or os.path.join(
                raiz,
                nombre_formato
            )
        )

        config[
            "ruta_alumnos"
        ] = (
            ruta_alumnos_local
            or os.path.join(
                raiz,
                nombre_alumnos
            )
        )

        config.setdefault(
            "archivo_alumnos",
            nombre_alumnos
        )

        config.setdefault(
            "anios_convalidables",
            ""
        )

        config.setdefault(
            "ciclos_convalidables",
            ""
        )

        carreras[
            nombre_carrera
        ] = config

        nombres_ya_cargados.add(
            clave_normalizada
        )

    return carreras



@st.cache_data(show_spinner=False, ttl=60)
def cargar_carreras_cache():
    """
    Cachea durante 60 segundos la lectura de la estructura de carreras,
    configuraciones JSON y rutas de formato/alumnos.
    Reduce el trabajo repetitivo de Streamlit en cada interacción.
    """
    carreras = obtener_carreras()

    return _cargar_carreras_respaldo(
        carreras
    )


# ============================================================
# VIDEO TUTORIAL
# ============================================================

VIDEO_TUTORIAL_URL = "https://youtu.be/Ocv1fXnyQaQ"


def _contenido_tutorial():
    """
    Contenido visual reutilizable del tutorial.
    """

    st.markdown(
        """
        <div style="
            padding: 16px 18px;
            border-radius: 14px;
            background: linear-gradient(135deg, #FFF7F8 0%, #FFFFFF 100%);
            border: 1px solid #E8D7DA;
            border-left: 5px solid #B5121B;
            margin-bottom: 14px;
        ">
            <div style="
                font-size: 20px;
                font-weight: 800;
                color: #2F2430;
                margin-bottom: 5px;
            ">
                Tutorial rápido del Sistema de Convalidaciones
            </div>
            <div style="
                font-size: 14px;
                color: #66565B;
                line-height: 1.5;
            ">
                Conoce el proceso completo: carga del certificado, revisión de notas,
                sugerencias por afinidad, competencias, exámenes de suficiencia,
                aprobación del coordinador y descarga de la proforma.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.video(
        VIDEO_TUTORIAL_URL
    )

    st.caption(
        "El video se reproduce directamente dentro del sistema. "
        "No es necesario salir de la plataforma."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            **1. Carga**  
            Certificado y datos del estudiante.
            """
        )

    with c2:
        st.markdown(
            """
            **2. Revisión**  
            Equivalencias, notas y suficiencias.
            """
        )

    with c3:
        st.markdown(
            """
            **3. Resultado**  
            Aprobación y documentos finales.
            """
        )


if hasattr(st, "dialog"):

    @st.dialog(
        "🎥 Tutorial del Sistema de Convalidaciones",
        width="large"
    )
    def mostrar_tutorial():
        _contenido_tutorial()

else:

    def mostrar_tutorial():
        st.session_state[
            "mostrar_tutorial_fallback"
        ] = True


# ============================================================
# HEADER Y SIDEBAR
# ============================================================

mostrar_header()

with st.sidebar:

    if RUTA_LOGO:
        st.image(
            str(RUTA_LOGO),
            use_container_width=True
        )

    st.markdown(
        '<div class="sidebar-brand">Convalidaciones UPRIT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-small">Sistema académico institucional</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "▶ VER VIDEO TUTORIAL",
        use_container_width=True,
        key="btn_ver_video_tutorial"
    ):
        mostrar_tutorial()

    st.markdown(
        (
            '<div class="sidebar-panel">'
            '<div class="sidebar-panel-title">Flujo de trabajo</div>'
            '<div class="sidebar-panel-text">'
            '1. Seleccionar carrera<br>'
            '2. Cargar certificado<br>'
            '3. Revisar cursos y notas<br>'
            '4. Analizar convalidaciones<br>'
            '5. Revisar equivalencias propuestas<br>'
            '6. Firmar y aprobar por el coordinador<br>'
            '7. Generar y descargar proforma / constancia'
            '</div>'
            '</div>'
        ),
        unsafe_allow_html=True
    )

    if (
        st.session_state.get(
            "mostrar_tutorial_fallback",
            False
        )
        and not hasattr(
            st,
            "dialog"
        )
    ):
        with st.expander(
            "🎥 Tutorial del Sistema de Convalidaciones",
            expanded=True
        ):
            _contenido_tutorial()

            if st.button(
                "✕ CERRAR TUTORIAL",
                use_container_width=True,
                key="btn_cerrar_tutorial_fallback"
            ):
                st.session_state[
                    "mostrar_tutorial_fallback"
                ] = False
                st.rerun()

    if "_nuevo_expediente_id" not in st.session_state:
        st.session_state["_nuevo_expediente_id"] = 0

    if st.button(
        "＋ NUEVA CONVALIDACIÓN",
        use_container_width=True,
        key="btn_nueva_convalidacion"
    ):
        claves_nuevo = [
            "datos_certificado",
            "resultado_convalidacion",
            "cursos_corregidos",
            "ruta_word_generado",
            "ruta_reporte_especial",
            "ruta_constancia_aprobacion",
            "resumen_escritura_word",
            "archivo_procesado",
            "editor_cursos",
            "nombre_alumno",
            "institucion_alumno",
            "dni_alumno",
            "carrera_alumno",
            "telefono_alumno",
            "email_alumno",
            "selector_carrera_destino",
            "_carrera_anterior"
        ]

        for clave in claves_nuevo:
            st.session_state.pop(
                clave,
                None
            )

        # Cambiar este identificador obliga a Streamlit a crear un
        # file_uploader nuevo y vacío en el siguiente rerun.
        st.session_state["_nuevo_expediente_id"] += 1

        st.rerun()

    st.divider()

    st.caption(
        "Universidad Privada de Trujillo"
    )


# ============================================================
# CARGAR CARRERAS
# ============================================================

carreras_disponibles = cargar_carreras_cache()

if not carreras_disponibles:

    st.error(
        "❌ No se encontraron carreras "
        "dentro de la carpeta Carreras."
    )

    st.stop()


# ============================================================
# ORDEN DE CARRERAS
# ============================================================

orden_preferido = [
    "Ingeniería Civil",
    "Ingeniería Industrial",
    "Ingeniería de Sistemas e IA",
    "Psicología"
]

lista_carreras = []

for nombre_preferido in orden_preferido:

    normal_preferido = (
        _normalizar_nombre_carrera(
            nombre_preferido
        )
    )

    for nombre_real in carreras_disponibles:

        if (
            _normalizar_nombre_carrera(
                nombre_real
            )
            == normal_preferido
        ):

            if nombre_real not in lista_carreras:

                lista_carreras.append(
                    nombre_real
                )

for nombre_real in sorted(
    carreras_disponibles.keys()
):

    if nombre_real not in lista_carreras:

        lista_carreras.append(
            nombre_real
        )


# ============================================================
# PASO 1 - CARRERA
# ============================================================

mostrar_stepper(
    1
)

col_carrera, col_info = st.columns(
    [
        1.55,
        1.45
    ],
    gap="large"
)

with col_carrera:

    with st.container(
        border=True
    ):

        titulo_seccion(
            "1. Seleccione la carrera de destino"
        )

        carrera_destino = st.selectbox(
            "Carrera",
            lista_carreras,
            index=None,
            placeholder="Seleccione una carrera...",
            key="selector_carrera_destino"
        )

        if carrera_destino is None:
            st.info(
                "Seleccione la carrera de destino para iniciar "
                "una nueva convalidación."
            )
            st.stop()

        # La configuración siempre se obtiene de la carrera
        # seleccionada EN ESTE rerun. Así se evita reutilizar
        # información de la carrera anterior.
        config_carrera = carreras_disponibles[
            carrera_destino
        ]

        ruta_formato = config_carrera.get(
            "ruta_formato"
        )

        carpeta_carrera = config_carrera.get(
            "carpeta",
            ""
        )

        ruta_alumnos = config_carrera.get(
            "ruta_alumnos"
        )

        if not ruta_alumnos:

            nombre_archivo_alumnos = (
                config_carrera.get(
                    "archivo_alumnos",
                    "alumnos.xlsx"
                )
            )

            ruta_alumnos = os.path.join(
                carpeta_carrera,
                nombre_archivo_alumnos
            )

        anios_convalidables = config_carrera.get(
            "anios_convalidables",
            ""
        )

        ciclos_convalidables = config_carrera.get(
            "ciclos_convalidables",
            ""
        )

        st.info(
            "Se utilizará el plan de estudios, "
            "la proforma y la base de alumnos de "
            "la carrera seleccionada."
        )


with col_info:

    with st.container(
        border=True
    ):

        titulo_seccion(
            "Resumen de la carrera"
        )

        periodo_texto = formatear_periodo_convalidable(
            anios_convalidables
        )

        ciclos_texto = (
            str(ciclos_convalidables)
            if ciclos_convalidables != ""
            else "No definido"
        )

        st.markdown(
            (
                '<div class="info-card-grid">'
                '<div class="info-card">'
                '<div class="info-card-label">Carrera seleccionada</div>'
                f'<div class="info-card-value">{carrera_destino}</div>'
                '</div>'
                '<div class="info-card">'
                '<div class="info-card-label">Periodo convalidable</div>'
                f'<div class="info-card-value">{periodo_texto}</div>'
                '</div>'
                '<div class="info-card">'
                '<div class="info-card-label">Ciclos</div>'
                f'<div class="info-card-value">{ciclos_texto}</div>'
                '</div>'
                '</div>'
            ),
            unsafe_allow_html=True
        )


# ============================================================
# VALIDAR ARCHIVOS DE CARRERA
# ============================================================

if (
    not ruta_formato
    or not os.path.exists(
        ruta_formato
    )
):

    st.error(
        "❌ La carrera fue detectada, "
        "pero no se encontró su proforma Word."
    )

    st.write(
        "**Carrera:**",
        carrera_destino
    )

    st.code(
        str(
            ruta_formato
        )
    )

    st.stop()


if (
    not ruta_alumnos
    or not os.path.exists(
        ruta_alumnos
    )
):

    st.error(
        "❌ La carrera fue detectada, "
        "pero no se encontró su archivo alumnos.xlsx."
    )

    st.write(
        "**Carrera:**",
        carrera_destino
    )

    st.code(
        str(
            ruta_alumnos
        )
    )

    st.stop()


st.markdown('<span class="status-ok">✓ Proforma y base de alumnos cargadas correctamente</span>', unsafe_allow_html=True)


# ============================================================
# LIMPIAR SESIÓN SI CAMBIA CARRERA
# ============================================================

carrera_anterior = st.session_state.get(
    "_carrera_anterior"
)

if (
    carrera_anterior is not None
    and carrera_anterior != carrera_destino
):

    claves_limpiar_carrera = [
        "datos_certificado",
        "resultado_convalidacion",
        "cursos_corregidos",
        "ruta_word_generado",
        "ruta_reporte_especial",
            "ruta_constancia_aprobacion",
        "resumen_escritura_word",
        "archivo_procesado",
        "editor_cursos",
        "nombre_alumno",
        "institucion_alumno",
        "dni_alumno",
        "carrera_alumno",
        "telefono_alumno",
        "email_alumno"
    ]

    for clave in claves_limpiar_carrera:

        if clave in st.session_state:

            del st.session_state[
                clave
            ]

st.session_state[
    "_carrera_anterior"
] = carrera_destino


# ============================================================
# PASO 1 - SUBIR PDF
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

with st.container(
    border=True
):

    titulo_seccion(
        "2. Cargar certificado de estudios"
    )

    archivo_pdf = st.file_uploader(
        "Arrastra el certificado PDF o haz clic para seleccionarlo",
        type=[
            "pdf"
        ],
        key=(
            "archivo_pdf_"
            f"{st.session_state.get('_nuevo_expediente_id', 0)}"
        )
    )

    if archivo_pdf is None:

        st.info(
            "👆 Suba un certificado de estudios "
            "en PDF para comenzar."
        )

        st.stop()

    st.success(
        f"✅ PDF cargado correctamente: {archivo_pdf.name}"
    )


# ============================================================
# IDENTIFICADOR DEL ARCHIVO
# ============================================================

pdf_bytes_actual = archivo_pdf.getvalue()

hash_certificado = hashlib.sha256(
    pdf_bytes_actual
).hexdigest()

identificador_archivo = (
    carrera_destino,
    archivo_pdf.name,
    archivo_pdf.size,
    hash_certificado
)

archivo_nuevo = (
    "archivo_procesado"
    not in st.session_state
    or
    st.session_state[
        "archivo_procesado"
    ] != identificador_archivo
)


# ============================================================
# PROCESAR PDF
# ============================================================

if archivo_nuevo:

    claves_limpiar = [
        "datos_certificado",
        "resultado_convalidacion",
        "cursos_corregidos",
        "ruta_word_generado",
        "ruta_reporte_especial",
        "resumen_escritura_word"
    ]

    for clave in claves_limpiar:

        if clave in st.session_state:

            del st.session_state[
                clave
            ]

    with st.spinner(
        "Se está interpretando el certificado..."
    ):

        try:

            datos = leer_pdf(
                archivo_pdf
            )

            st.session_state[
                "datos_certificado"
            ] = datos

            st.session_state[
                "archivo_procesado"
            ] = identificador_archivo

        except Exception as error:

            st.error(
                "❌ No se pudo procesar el certificado."
            )

            st.exception(
                error
            )

            st.stop()


# ============================================================
# DATOS DEL CERTIFICADO
# ============================================================

datos = st.session_state.get(
    "datos_certificado",
    {}
)

nombre_detectado = datos.get(
    "nombre",
    ""
)


# ============================================================
# BUSCAR ALUMNO EN EXCEL
# ============================================================

resultado_alumno = buscar_alumno_cache(
    nombre_detectado,
    ruta_alumnos
)

# ============================================================
# SEGUNDO INTENTO - NOMBRE ARCHIVO
# ============================================================

if not resultado_alumno.get(
    "encontrado"
):

    nombre_desde_archivo = os.path.splitext(
        archivo_pdf.name
    )[0].upper()

    palabras_quitar = [
        "OK",
        "CERTIFICADO",
        "CERT",
        "NOTAS",
        "ESTUDIOS",
        "COPIA"
    ]

    for palabra in palabras_quitar:

        nombre_desde_archivo = (
            nombre_desde_archivo
            .replace(
                palabra,
                " "
            )
        )

    nombre_desde_archivo = (
        nombre_desde_archivo
        .replace(
            "-",
            " "
        )
        .replace(
            "_",
            " "
        )
        .replace(
            "(",
            " "
        )
        .replace(
            ")",
            " "
        )
    )

    nombre_desde_archivo = " ".join(
        nombre_desde_archivo.split()
    )

    resultado_archivo = buscar_alumno_cache(
        nombre_desde_archivo,
        ruta_alumnos
    )

    if resultado_archivo.get(
        "encontrado"
    ):

        resultado_alumno = resultado_archivo



datos_excel = resultado_alumno.get(
    "datos",
    {}
)


# ============================================================
# PASO 2 - DATOS DEL ESTUDIANTE
# ============================================================

mostrar_stepper(
    2
)

col_estudiante = st.container()

with col_estudiante:

    with st.container(
        border=True
    ):

        titulo_seccion(
            "3. Datos del estudiante"
        )

        nombre_excel = datos_excel.get(
            "nombre",
            ""
        )

        nombre_inicial = (
            nombre_excel
            if nombre_excel
            else datos.get(
                "nombre",
                ""
            )
        )

        dni_excel = datos_excel.get(
            "dni",
            ""
        )

        dni_inicial = (
            dni_excel
            if dni_excel
            else datos.get(
                "dni",
                ""
            )
        )

        telefono_excel = datos_excel.get(
            "telefono",
            ""
        )

        telefono_inicial = (
            telefono_excel
            if telefono_excel
            else datos.get(
                "telefono",
                ""
            )
        )

        email_excel = datos_excel.get(
            "email",
            ""
        )

        email_inicial = (
            email_excel
            if email_excel
            else datos.get(
                "email",
                ""
            )
        )

        c1, c2 = st.columns(
            2
        )

        with c1:

            nombre = st.text_input(
                "Apellidos y nombres",
                value=nombre_inicial,
                key="nombre_alumno"
            )

            dni = st.text_input(
                "DNI",
                value=dni_inicial,
                key="dni_alumno"
            )

            institucion = st.text_input(
                "Universidad / Instituto de procedencia",
                value=datos.get(
                    "institucion",
                    ""
                ),
                key="institucion_alumno"
            )

        with c2:

            carrera_procedencia = st.text_input(
                "Carrera / Especialidad de procedencia",
                value=datos.get(
                    "carrera",
                    ""
                ),
                key="carrera_alumno"
            )

            telefono = st.text_input(
                "Teléfono",
                value=telefono_inicial,
                key="telefono_alumno"
            )

            email = st.text_input(
                "Email",
                value=email_inicial,
                key="email_alumno"
            )

        st.info(
            f"🎯 Carrera UPRIT de destino: **{carrera_destino}**"
        )



# ============================================================
# CURSOS Y NOTAS
# ============================================================

with st.container(
    border=True
):

    titulo_seccion(
        "4. Cursos y notas detectados del certificado"
    )

    cursos = datos.get(
        "cursos",
        []
    )

    if not cursos:

        st.warning(
            "⚠️ No se detectaron cursos automáticamente. "
            "Puede ingresarlos manualmente."
        )

        df_cursos = pd.DataFrame(
            columns=[
                "curso",
                "nota",
                "creditos"
            ]
        )

    else:

        df_cursos = pd.DataFrame(
            cursos
        )

    if "curso" not in df_cursos.columns:
        df_cursos[
            "curso"
        ] = ""

    if "nota" not in df_cursos.columns:
        df_cursos[
            "nota"
        ] = None

    columnas_base = [
        "curso",
        "nota"
    ]

    if "creditos" in df_cursos.columns:

        columnas_base.append(
            "creditos"
        )

    df_cursos = df_cursos[
        columnas_base
    ]

    df_cursos = df_cursos.rename(
        columns={
            "curso":
                "Curso",
            "nota":
                "Nota",
            "creditos":
                "Créditos"
        }
    )

    st.caption(
        "Revise los cursos y notas antes de realizar "
        "la convalidación. Puede corregir manualmente."
    )

    configuracion_columnas = {
        "Curso":
            st.column_config.TextColumn(
                "Curso",
                width="large",
                required=True
            ),
        "Nota":
            st.column_config.NumberColumn(
                "Nota",
                min_value=0,
                max_value=20,
                step=1,
                required=False
            )
    }

    if "Créditos" in df_cursos.columns:

        configuracion_columnas[
            "Créditos"
        ] = st.column_config.NumberColumn(
            "Créditos",
            min_value=0,
            required=False
        )

    df_editado = st.data_editor(
        df_cursos,
        width="stretch",
        hide_index=True,
        num_rows="dynamic",
        column_config=configuracion_columnas,
        key="editor_cursos"
    )

    cursos_corregidos = []

    for _, fila in df_editado.iterrows():

        curso = str(
            fila.get(
                "Curso",
                ""
            )
        ).strip()

        if not curso:
            continue

        nota = fila.get(
            "Nota",
            None
        )

        if pd.isna(
            nota
        ):

            nota = None

        else:

            try:

                nota_num = float(
                    nota
                )

                nota = (
                    int(
                        nota_num
                    )
                    if nota_num.is_integer()
                    else nota_num
                )

            except (
                TypeError,
                ValueError
            ):

                nota = None

        item = {
            "curso":
                curso,
            "nota":
                nota
        }

        if "Créditos" in df_editado.columns:

            creditos = fila.get(
                "Créditos",
                None
            )

            if pd.isna(
                creditos
            ):

                creditos = ""

            else:

                try:

                    creditos_num = float(
                        creditos
                    )

                    creditos = (
                        int(
                            creditos_num
                        )
                        if creditos_num.is_integer()
                        else creditos_num
                    )

                except (
                    TypeError,
                    ValueError
                ):

                    creditos = ""

            item[
                "creditos"
            ] = creditos

        cursos_corregidos.append(
            item
        )

    st.session_state[
        "cursos_corregidos"
    ] = cursos_corregidos

    total_cursos = len(
        cursos_corregidos
    )

    cursos_sin_nota = [
        item
        for item in cursos_corregidos
        if item.get(
            "nota"
        ) is None
    ]

    m1, m2 = st.columns(
        2
    )

    with m1:

        st.metric(
            "Cursos detectados",
            total_cursos
        )

    with m2:

        st.metric(
            "Cursos sin nota",
            len(
                cursos_sin_nota
            )
        )

    if cursos_sin_nota:

        st.warning(
            f"⚠️ Hay {len(cursos_sin_nota)} "
            "cursos cuya nota no pudo ser identificada."
        )


# ============================================================
# DIAGNÓSTICO DE LECTURA
# ============================================================

diagnostico_lectura = datos.get(
    "diagnostico_lectura",
    []
)

if diagnostico_lectura:

    with st.expander(
        "🧪 Diagnóstico de lectura del certificado"
    ):

        df_diagnostico = pd.DataFrame(
            diagnostico_lectura
        )

        df_diagnostico = (
            df_diagnostico.rename(
                columns={
                    "pagina":
                        "Página",
                    "metodo":
                        "Método",
                    "caracteres":
                        "Caracteres"
                }
            )
        )

        st.dataframe(
            df_diagnostico,
            width="stretch",
            hide_index=True
        )


# ============================================================
# PASO 3 - ANALIZAR
# ============================================================

mostrar_stepper(
    3
)

with st.container(
    border=True
):

    titulo_seccion(
        "5. Analizar convalidaciones"
    )

    st.write(
        "El sistema prioriza coincidencias directas por nombre "
        "y, cuando los nombres son distintos, el sistema evalúa "
        "la afinidad académica por significado, área y finalidad "
        "habitual de la asignatura."
    )

    st.caption(
        "Las observaciones o notas no detectadas no bloquearán la "
        "generación de la proforma."
    )

    if st.button(
        "🔍 ANALIZAR CONVALIDACIONES",
        type="primary",
        use_container_width=True
    ):

        if not cursos_corregidos:

            st.warning(
                "No existen cursos válidos para analizar."
            )

        else:

            with st.spinner(
                "🤖 Analizando equivalencias académicas "
                "y competencias..."
            ):

                try:

                    parametros_analizador = (
                        inspect.signature(
                            analizar_convalidaciones
                        ).parameters
                    )

                    argumentos_analisis = {
                        "cursos_alumno":
                            cursos_corregidos,
                        "ruta_formato":
                            ruta_formato
                    }

                    if (
                        "carrera_destino"
                        in parametros_analizador
                    ):

                        argumentos_analisis[
                            "carrera_destino"
                        ] = carrera_destino

                    resultado = analizar_convalidaciones(
                        **argumentos_analisis
                    )

                    resultado = corregir_competencias_resultado_desde_formato(
                        resultado=resultado,
                        ruta_formato=ruta_formato
                    )

                    if not isinstance(
                        resultado,
                        dict
                    ):

                        raise ValueError(
                            "El motor de convalidaciones "
                            "devolvió un resultado inválido."
                        )

                    estructura_detectada = (
                        resultado.get(
                            "estructura_proforma",
                            []
                        )
                    )

                    if not estructura_detectada:

                        raise ValueError(
                            "El motor no pudo leer ninguna "
                            "asignatura de la proforma seleccionada."
                        )

                    st.session_state[
                        "resultado_convalidacion"
                    ] = resultado

                    st.session_state.pop(
                        "aprobacion_coordinador",
                        None
                    )
                    st.session_state.pop(
                        "firma_coordinador_path",
                        None
                    )

                    for clave_documento in [
                        "ruta_word_generado",
                        "ruta_reporte_especial",
                        "resumen_escritura_word"
                    ]:

                        if (
                            clave_documento
                            in st.session_state
                        ):

                            del st.session_state[
                                clave_documento
                            ]

                except Exception as error:

                    st.error(
                        "❌ No se pudo realizar el análisis "
                        "de convalidaciones."
                    )

                    st.exception(
                        error
                    )


# ============================================================
# RESULTADOS
# ============================================================

if (
    "resultado_convalidacion"
    in st.session_state
):

    resultado = st.session_state[
        "resultado_convalidacion"
    ]

    convalidaciones = resultado.get(
        "convalidaciones",
        []
    )

    pendientes = resultado.get(
        "pendientes",
        []
    )

    suficiencias = resultado.get(
        "suficiencias",
        []
    )

    competencias = resultado.get(
        "competencias",
        []
    )

    cursos_no_utilizados = resultado.get(
        "cursos_no_utilizados",
        []
    )

    caso_especial = resultado.get(
        "caso_especial",
        False
    )

    cantidad_suficiencias = resultado.get(
        "cantidad_suficiencias",
        len(
            suficiencias
        )
    )

    maximo_suficiencias = resultado.get(
        "maximo_suficiencias",
        7
    )

    observacion_caso_especial = resultado.get(
        "observacion_caso_especial",
        ""
    )

    suficiencias_iniciales = resultado.get(
        "suficiencias_iniciales",
        list(
            suficiencias
        )
    )

    suficiencias_post_revision_completas = resultado.get(
        "suficiencias_post_revision_completas",
        list(
            suficiencias
        )
    )

    suficiencias_excedentes_revision = resultado.get(
        "suficiencias_excedentes_revision",
        []
    )

    revision_especial_civil_realizada = resultado.get(
        "revision_especial_civil_realizada",
        False
    )

    recomendaciones_caso_especial = resultado.get(
        "recomendaciones_caso_especial",
        []
    )

    reglas_carrera_resultado = resultado.get(
        "reglas_carrera",
        {}
    )

    revision_manual_asistida = bool(
        resultado.get(
            "revision_manual_asistida",
            False
        )
    )

    autoseleccionar_recomendaciones = bool(
        resultado.get(
            "autoseleccionar_recomendaciones",
            False
        )
    )

    # Cualquier carrera que tenga revision_manual_asistida=True
    # utiliza el mismo flujo moderno de revisión por el coordinador.
    es_revision_manual_ui = revision_manual_asistida

    if es_revision_manual_ui:
        caso_especial = False
        observacion_caso_especial = ""
        suficiencias_excedentes_revision = []

    validacion_word = (
        validar_resultado_antes_de_word(
            convalidaciones
        )
    )

    convalidaciones_reales = (
        validacion_word[
            "reales"
        ]
    )

    cantidad_reales = (
        validacion_word[
            "cantidad_reales"
        ]
    )

    convalidaciones_sin_nota_parcial = (
        validacion_word[
            "sin_nota_parcial"
        ]
    )

    convalidaciones_sin_nota_convalidante = (
        validacion_word[
            "sin_nota_convalidante"
        ]
    )


    # ========================================================
    # PASO 3 - RESULTADOS Y REVISIÓN DE CONVALIDACIONES
    # ========================================================

    mostrar_stepper(
        3
    )


    # ========================================================
    # RESUMEN
    # ========================================================

    with st.container(
        border=True
    ):

        titulo_seccion(
            "6. Resultados de convalidación"
        )

        r1, r2, r3, r4 = st.columns(
            4
        )

        with r1:

            st.metric(
                "Competencias",
                len(
                    competencias
                )
            )

        with r2:

            st.metric(
                "Convalidaciones reales",
                cantidad_reales
            )

        with r3:

            st.metric(
                "Suficiencias",
                cantidad_suficiencias
            )

        with r4:

            st.metric(
                "Máximo permitido",
                maximo_suficiencias
            )

        if (
            es_revision_manual_ui
            and revision_manual_asistida
            and len(
                suficiencias_iniciales
            ) > maximo_suficiencias
        ):
            st.info(
                "✏️ Se detectaron más de 7 asignaturas pendientes en la "
                "evaluación inicial. En Ingeniería Industrial no se genera "
                "un CASO ESPECIAL: complete la revisión manual asistida "
                "utilizando las recomendaciones del sistema y confirme cada "
                "equivalencia antes de aprobar."
            )

        if caso_especial:

            st.warning(
                observacion_caso_especial
                if observacion_caso_especial
                else (
                    "CASO ESPECIAL: el expediente supera "
                    "el umbral ordinario de suficiencias."
                )
            )

            if revision_especial_civil_realizada:

                ce1, ce2, ce3 = st.columns(
                    3
                )

                with ce1:
                    st.metric(
                        "Candidatos iniciales",
                        len(
                            suficiencias_iniciales
                        )
                    )

                with ce2:
                    st.metric(
                        "Después de revisión",
                        len(
                            suficiencias_post_revision_completas
                        )
                    )

                with ce3:
                    st.metric(
                        "Suficiencias finales",
                        len(
                            suficiencias
                        )
                    )

                with st.expander(
                    "🔎 Ver revisión especial completa de Ingeniería Civil"
                ):
                    st.write(
                        "**Candidatos antes de la segunda revisión:**"
                    )
                    st.dataframe(
                        pd.DataFrame({
                            "Asignatura":
                                suficiencias_iniciales
                        }),
                        width="stretch",
                        hide_index=True
                    )

                    st.write(
                        "**Faltantes después de la revisión especialista:**"
                    )
                    st.dataframe(
                        pd.DataFrame({
                            "Asignatura":
                                suficiencias_post_revision_completas
                        }),
                        width="stretch",
                        hide_index=True
                    )

                    if suficiencias_excedentes_revision:
                        st.write(
                            "**Pendientes adicionales fuera del máximo de 7:**"
                        )
                        st.dataframe(
                            pd.DataFrame({
                                "Asignatura":
                                    suficiencias_excedentes_revision
                            }),
                            width="stretch",
                            hide_index=True
                        )


        # ====================================================
        # TABS
        # ====================================================

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                f"✅ Convalidaciones ({cantidad_reales})",
                f"🧩 Competencias ({len(competencias)})",
                f"🟡 Pendientes ({len(pendientes)})",
                f"🔵 Suficiencias ({len(suficiencias)})",
                f"📘 No utilizados ({len(cursos_no_utilizados)})",
                f"💡 Recomendaciones ({len(recomendaciones_caso_especial)})"
            ]
        )


        # ====================================================
        # TAB CONVALIDACIONES
        # ====================================================

        with tab1:

            if convalidaciones_reales:

                df_convalidaciones = pd.DataFrame(
                    convalidaciones_reales
                )

                df_convalidaciones = (
                    df_convalidaciones.rename(
                        columns={
                            "competencia":
                                "Competencia",
                            "curso_destino":
                                "Curso UPRIT",
                            "curso_origen":
                                "Asignatura convalidante",
                            "nota":
                                "Nota parcial",
                            "nota_convalidante":
                                "Nota convalidante",
                            "afinidad":
                                "Afinidad",
                            "tipo_equivalencia":
                                "Tipo de equivalencia",
                            "justificacion":
                                "Justificación",
                            "estado":
                                "Estado",
                            "estado_competencia":
                                "Estado de competencia"
                        }
                    )
                )

                columnas_deseadas = [
                    "Competencia",
                    "Curso UPRIT",
                    "Asignatura convalidante",
                    "Nota parcial",
                    "Nota convalidante",
                    "Afinidad",
                    "Tipo de equivalencia",
                    "Estado",
                    "Estado de competencia",
                    "Justificación"
                ]

                columnas_existentes = [
                    columna
                    for columna in columnas_deseadas
                    if columna
                    in df_convalidaciones.columns
                ]

                st.dataframe(
                    df_convalidaciones[
                        columnas_existentes
                    ],
                    width="stretch",
                    hide_index=True
                )

                st.success(
                    f"✅ Se encontraron {cantidad_reales} "
                    "convalidaciones reales."
                )

            else:

                st.warning(
                    "No se encontraron convalidaciones directas."
                )


        # ====================================================
        # TAB COMPETENCIAS
        # ====================================================

        with tab2:

            if competencias:

                df_competencias = pd.DataFrame(
                    competencias
                )

                df_competencias = (
                    df_competencias.rename(
                        columns={
                            "competencia":
                                "Competencia",
                            "total_asignaturas":
                                "Total de asignaturas",
                            "asignaturas_con_equivalencia":
                                "Con equivalencia",
                            "asignaturas_faltantes":
                                "Faltantes",
                            "nota_convalidante":
                                "Nota convalidante",
                            "estado":
                                "Estado",
                            "justificacion":
                                "Justificación",
                            "cursos_faltantes":
                                "Cursos faltantes"
                        }
                    )
                )

                if (
                    "Cursos faltantes"
                    in df_competencias.columns
                ):

                    df_competencias[
                        "Cursos faltantes"
                    ] = df_competencias[
                        "Cursos faltantes"
                    ].apply(
                        lambda x: (
                            ", ".join(
                                x
                            )
                            if isinstance(
                                x,
                                list
                            )
                            else x
                        )
                    )

                columnas_competencia = [
                    "Competencia",
                    "Total de asignaturas",
                    "Con equivalencia",
                    "Faltantes",
                    "Nota convalidante",
                    "Estado",
                    "Cursos faltantes",
                    "Justificación"
                ]

                columnas_competencia = [
                    columna
                    for columna in columnas_competencia
                    if columna
                    in df_competencias.columns
                ]

                st.dataframe(
                    df_competencias[
                        columnas_competencia
                    ],
                    width="stretch",
                    hide_index=True
                )

            else:

                st.info(
                    "No se obtuvo resumen por competencias."
                )


        # ====================================================
        # TAB PENDIENTES
        # ====================================================

        with tab3:

            if pendientes:

                st.dataframe(
                    pd.DataFrame({
                        "Asignatura UPRIT":
                            pendientes
                    }),
                    width="stretch",
                    hide_index=True
                )

            else:

                st.success(
                    "No hay asignaturas pendientes."
                )


        # ====================================================
        # TAB SUFICIENCIAS
        # ====================================================

        with tab4:

            if suficiencias:

                st.dataframe(
                    pd.DataFrame({
                        "Asignatura UPRIT":
                            suficiencias
                    }),
                    width="stretch",
                    hide_index=True
                )

                if not caso_especial:

                    st.info(
                        f"Se identificaron {len(suficiencias)} "
                        "asignaturas candidatas a suficiencia."
                    )

            else:

                st.success(
                    "No se identificaron asignaturas "
                    "que requieran examen de suficiencia."
                )


        # ====================================================
        # TAB NO UTILIZADOS
        # ====================================================

        with tab5:

            if cursos_no_utilizados:

                df_no_utilizados = pd.DataFrame(
                    cursos_no_utilizados
                )

                df_no_utilizados = (
                    df_no_utilizados.rename(
                        columns={
                            "curso":
                                "Curso",
                            "nota":
                                "Nota",
                            "creditos":
                                "Créditos"
                        }
                    )
                )

                st.dataframe(
                    df_no_utilizados,
                    width="stretch",
                    hide_index=True
                )

            else:

                st.info(
                    "Todos los cursos detectados fueron utilizados."
                )


        # ====================================================
        # TAB RECOMENDACIONES
        # ====================================================

        with tab6:

            if recomendaciones_caso_especial:

                st.warning(
                    "Las recomendaciones son referenciales y "
                    "no constituyen aprobación automática."
                )

                df_rec = pd.DataFrame(
                    recomendaciones_caso_especial
                ).rename(
                    columns={
                        "curso_destino":
                            "Curso UPRIT pendiente",
                        "curso_sugerido":
                            "Curso sugerido",
                        "nota":
                            "Nota real",
                        "afinidad":
                            "Afinidad",
                        "recomendacion":
                            "Recomendación",
                        "justificacion":
                            "Justificación",
                        "requiere_silabo":
                            "Requiere sílabo"
                    }
                )

                st.dataframe(
                    df_rec,
                    width="stretch",
                    hide_index=True
                )

            else:

                st.info(
                    "No existen recomendaciones adicionales."
                )


    # ========================================================
    # MESA DE REVISIÓN DEL COORDINADOR
    # ========================================================

    with st.container(
        border=True
    ):

        titulo_seccion(
            "7. Mesa de revisión del coordinador"
        )

        st.write(
            "Contraste el certificado original con la propuesta. "
            "Puede editar la tabla antes de aprobar."
        )

        aprobacion_actual = st.session_state.get(
            "aprobacion_coordinador",
            {}
        )

        aprobado = bool(
            aprobacion_actual.get(
                "aprobado"
            )
        )

        # ====================================================
        # CERTIFICADO ARRIBA - ANCHO COMPLETO
        # ====================================================

        st.markdown(
            "### 📑 Certificado original"
        )

        st.write(
            "Amplíe el certificado y contraste las notas antes de "
            "editar o aprobar la propuesta."
        )

        mostrar_pdf_subido(
            archivo_pdf,
            altura=720
        )

        st.divider()

        # ====================================================
        # TABLA COMPLETA DEBAJO
        # ====================================================

        st.markdown(
            (
                '<div class="revision-title-box">'
                '<div class="rt-main">✏️ Revisión completa de la proforma</div>'
                '<div class="rt-sub">'
                'Valide cada equivalencia antes de aprobar el expediente.'
                '</div>'
                '</div>'
            ),
            unsafe_allow_html=True
        )

        st.warning(
            "👨‍💼 **Coordinador:** revise los cursos propuestos. "
            "En las filas pendientes puede seleccionar una asignatura "
            "del certificado desde la lista desplegable. La nota parcial "
            "se completa automáticamente y el promedio de la competencia "
            "se recalcula sin superar 17."
        )

        df_revision, opciones_por_fila, datos_selectores = (
            preparar_revision_con_selectores(
                resultado=resultado,
                cursos_certificado=cursos_corregidos
            )
        )

        if not df_revision.empty:

            st.caption(
                "En las filas pendientes, seleccione una asignatura del "
                "certificado. La nota parcial se carga automáticamente. "
                "Una asignatura ya utilizada no vuelve a ofrecerse en otra fila."
            )

            if aprobado:
                st.warning(
                    "✏️ Puede seguir modificando los desplegables. "
                    "Si cambia una equivalencia, la aprobación anterior "
                    "se anulará automáticamente y deberá aprobar nuevamente."
                )

            df_trabajo = df_revision.copy()

            # Recuperar selecciones realizadas en reruns anteriores.
            selecciones_guardadas = st.session_state.get(
                "selecciones_revision_coordinador",
                {}
            )

            cursos_usados_dinamicos = set()

            # Primero registrar las equivalencias ya existentes.
            for valor in df_trabajo[
                "Asignatura convalidante"
            ].fillna("").astype(str):

                if valor.strip():
                    cursos_usados_dinamicos.add(
                        _normalizar_nombre_carrera(
                            valor
                        )
                    )

            # ------------------------------------------------
            # CONTADOR DINÁMICO DE SUFICIENCIAS PENDIENTES
            #
            # El placeholder se crea aquí para que visualmente
            # permanezca encima de la tabla, pero su contenido
            # se actualiza DESPUÉS de procesar todos los
            # desplegables del coordinador.
            # ------------------------------------------------

            placeholder_suficiencias = st.empty()

            st.markdown(
                (
                    '<div class="revision-header">'
                    '<div>CURSO UPRIT / COMPETENCIA</div>'
                    '<div>ASIGNATURA CONVALIDANTE</div>'
                    '<div>NOTA PARCIAL</div>'
                    '<div>NOTA CONVALIDANTE</div>'
                    '</div>'
                ),
                unsafe_allow_html=True
            )

            for indice in df_trabajo.index:

                curso_uprit = str(
                    df_trabajo.at[
                        indice,
                        "Curso UPRIT"
                    ]
                )

                actual = str(
                    df_trabajo.at[
                        indice,
                        "Asignatura convalidante"
                    ]
                    or ""
                ).strip()

                recomendacion = str(
                    df_trabajo.at[
                        indice,
                        "Recomendación"
                    ]
                    or ""
                ).strip()

                with st.container(border=True):

                    c1, c2, c3, c4 = st.columns(
                        [1.45, 2.2, 0.65, 0.75]
                    )

                    with c1:

                        competencia_texto = str(
                            df_trabajo.at[
                                indice,
                                "Competencia"
                            ]
                            or ""
                        )

                        st.markdown(
                            (
                                '<div class="curso-uprit-name">'
                                + curso_uprit
                                + '</div>'
                                + '<span class="competencia-badge">'
                                + competencia_texto
                                + '</span>'
                            ),
                            unsafe_allow_html=True
                        )

                    opciones = list(
                        opciones_por_fila.get(
                            indice,
                            ["— SIN ASIGNAR —"]
                        )
                    )

                    # Quitar de esta lista cursos escogidos manualmente
                    # en filas anteriores, excepto el actual.
                    opciones_filtradas = []

                    for etiqueta in opciones:

                        curso_etiqueta = datos_selectores[
                            "etiqueta_a_curso"
                        ].get(
                            etiqueta,
                            ""
                        )

                        clave_etiqueta = _normalizar_nombre_carrera(
                            curso_etiqueta
                        )

                        if (
                            clave_etiqueta
                            and clave_etiqueta in cursos_usados_dinamicos
                            and clave_etiqueta
                            != _normalizar_nombre_carrera(
                                actual
                            )
                        ):
                            continue

                        opciones_filtradas.append(
                            etiqueta
                        )

                    opciones = opciones_filtradas or [
                        "— SIN ASIGNAR —"
                    ]

                    etiqueta_actual = "— SIN ASIGNAR —"

                    if actual:
                        for etiqueta in opciones:
                            if (
                                _normalizar_nombre_carrera(
                                    datos_selectores[
                                        "etiqueta_a_curso"
                                    ].get(
                                        etiqueta,
                                        ""
                                    )
                                )
                                == _normalizar_nombre_carrera(
                                    actual
                                )
                            ):
                                etiqueta_actual = etiqueta
                                break

                    seleccion_previa = selecciones_guardadas.get(
                        str(
                            indice
                        )
                    )

                    if seleccion_previa in opciones:
                        etiqueta_actual = seleccion_previa

                    # Carrera con revisión manual asistida:
                    # si la fila está vacía y existe una recomendación válida,
                    # la dejamos preseleccionada para acelerar la revisión.
                    elif (
                        es_revision_manual_ui
                        and autoseleccionar_recomendaciones
                        and not actual
                        and recomendacion
                    ):

                        recomendacion_limpia = re.sub(
                            r"\s+\((?:MUY ALTA|ALTA|MEDIA|BAJA|\d+(?:\.\d+)?%?)\)\s*$",
                            "",
                            recomendacion,
                            flags=re.IGNORECASE
                        ).strip()

                        for etiqueta in opciones:

                            curso_opcion = datos_selectores[
                                "etiqueta_a_curso"
                            ].get(
                                etiqueta,
                                ""
                            )

                            if (
                                _normalizar_nombre_carrera(
                                    curso_opcion
                                )
                                == _normalizar_nombre_carrera(
                                    recomendacion_limpia
                                )
                            ):
                                etiqueta_actual = etiqueta
                                break

                    indice_default = (
                        opciones.index(
                            etiqueta_actual
                        )
                        if etiqueta_actual in opciones
                        else 0
                    )

                    with c2:

                        seleccion = st.selectbox(
                            "Asignatura convalidante",
                            options=opciones,
                            index=indice_default,
                            key=f"selector_convalidante_{indice}",
                            disabled=False,
                            on_change=marcar_revision_modificada,
                            label_visibility="collapsed"
                        )

                        if recomendacion:

                            if es_revision_manual_ui:
                                texto_recomendacion = (
                                    '💡 <b>Se recomienda:</b> '
                                    + recomendacion
                                    + '<br><span style="font-size:11px;">'
                                    'Revise la afinidad antes de aprobar. '
                                    'Puede cambiar esta opción si considera '
                                    'que existe una equivalencia más adecuada.'
                                    '</span>'
                                )
                            else:
                                texto_recomendacion = (
                                    '💡 <b>Recomendación:</b> '
                                    + recomendacion
                                )

                            st.markdown(
                                (
                                    '<div class="recomendacion-box">'
                                    + texto_recomendacion
                                    + '</div>'
                                ),
                                unsafe_allow_html=True
                            )

                    selecciones_guardadas[
                        str(
                            indice
                        )
                    ] = seleccion

                    curso_elegido = datos_selectores[
                        "etiqueta_a_curso"
                    ].get(
                        seleccion,
                        ""
                    )

                    df_trabajo.at[
                        indice,
                        "Asignatura convalidante"
                    ] = curso_elegido

                    if curso_elegido:

                        clave_elegida = _normalizar_nombre_carrera(
                            curso_elegido
                        )

                        nota_auto = datos_selectores[
                            "mapa_notas"
                        ].get(
                            clave_elegida
                        )

                        df_trabajo.at[
                            indice,
                            "Nota parcial"
                        ] = (
                            nota_auto
                            if not valor_vacio(
                                nota_auto
                            )
                            else ""
                        )

                        cursos_usados_dinamicos.add(
                            clave_elegida
                        )

                    else:
                        df_trabajo.at[
                            indice,
                            "Nota parcial"
                        ] = ""

                    # Recalcular después de cada selección.
                    df_trabajo = recalcular_notas_competencia(
                        df_trabajo
                    )

                    with c3:
                        st.metric(
                            "Nota parcial",
                            (
                                df_trabajo.at[
                                    indice,
                                    "Nota parcial"
                                ]
                                if not valor_vacio(
                                    df_trabajo.at[
                                        indice,
                                        "Nota parcial"
                                    ]
                                )
                                else "—"
                            )
                        )

                    with c4:
                        st.metric(
                            "Nota conv.",
                            (
                                df_trabajo.at[
                                    indice,
                                    "Nota convalidante"
                                ]
                                if not valor_vacio(
                                    df_trabajo.at[
                                        indice,
                                        "Nota convalidante"
                                    ]
                                )
                                else "—"
                            )
                        )

            st.session_state[
                "selecciones_revision_coordinador"
            ] = selecciones_guardadas

            cantidad_suficiencias_pendientes = (
                contar_suficiencias_pendientes(
                    df_trabajo
                )
            )

            st.session_state[
                "cantidad_suficiencias_pendientes_revision"
            ] = cantidad_suficiencias_pendientes

            # ------------------------------------------------
            # SUFICIENCIAS ACTUALES DESPUÉS DE LA EDICIÓN MANUAL
            #
            # Si el coordinador asigna un curso y existe nota parcial,
            # ese curso deja de considerarse pendiente de suficiencia.
            # ------------------------------------------------

            suficiencias_revision_actuales = []

            for _, fila_revision in df_trabajo.iterrows():

                curso_uprit_revision = str(
                    fila_revision.get(
                        "Curso UPRIT",
                        ""
                    )
                    or ""
                ).strip()

                if not curso_uprit_revision:
                    continue

                asignatura_revision = str(
                    fila_revision.get(
                        "Asignatura convalidante",
                        ""
                    )
                    or ""
                ).strip()

                nota_revision = fila_revision.get(
                    "Nota parcial",
                    ""
                )

                if (
                    not asignatura_revision
                    or valor_vacio(
                        nota_revision
                    )
                ):
                    if (
                        curso_uprit_revision
                        not in suficiencias_revision_actuales
                    ):
                        suficiencias_revision_actuales.append(
                            curso_uprit_revision
                        )

            st.session_state[
                "suficiencias_revision_actuales"
            ] = suficiencias_revision_actuales

            # El documento de CASO ESPECIAL se decide con el estado
            # ACTUAL, no con la detección inicial.
            reglas_revision_actual = resultado.get(
                "reglas_carrera",
                {}
            )

            permitir_caso_especial_actual = bool(
                reglas_revision_actual.get(
                    "generar_caso_especial",
                    True
                )
            )

            caso_especial_revision_actual = (
                permitir_caso_especial_actual
                and len(
                    suficiencias_revision_actuales
                ) > 7
            )

            st.session_state[
                "caso_especial_revision_actual"
            ] = caso_especial_revision_actual

            # Si el coordinador ya redujo los pendientes a 7 o menos,
            # cualquier reporte especial generado previamente queda obsoleto.
            if not caso_especial_revision_actual:
                st.session_state.pop(
                    "ruta_reporte_especial",
                    None
                )

            # Actualizar el contador con el estado REAL después
            # de todas las selecciones realizadas en los desplegables.
            placeholder_suficiencias.markdown(
                construir_contador_suficiencias(
                    cantidad_suficiencias_pendientes
                ),
                unsafe_allow_html=True
            )

            st.session_state[
                "convalidaciones_editadas"
            ] = aplicar_ediciones_tabla_completa(
                resultado=resultado,
                df_editado=df_trabajo
            )

            if es_revision_manual_ui:

                filas_sin_asignar = int(
                    df_trabajo[
                        "Asignatura convalidante"
                    ]
                    .fillna("")
                    .astype(str)
                    .str.strip()
                    .eq("")
                    .sum()
                )

                st.markdown(
                    (
                        '<div class="revision-footer-note">'
                        '👨‍💼 <b>Revisión del coordinador:</b> '
                        'las recomendaciones ya aparecen preseleccionadas cuando '
                        'existe un candidato académico disponible. Revise cada una '
                        'antes de aprobar. Cursos todavía sin asignación: '
                        + str(filas_sin_asignar)
                        + '.<br>'
                        '🔒 Un curso del certificado solo puede utilizarse una vez · '
                        'la nota parcial proviene del certificado · '
                        'la nota convalidante se recalcula por competencia · '
                        'máximo 17.'
                        '</div>'
                    ),
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    (
                        '<div class="revision-footer-note">'
                        '🔒 <b>Reglas activas:</b> un curso del certificado solo puede '
                        'usarse una vez · las notas parciales provienen del certificado · '
                        'el promedio se recalcula por competencia · nota convalidante máxima: 17.'
                        '</div>'
                    ),
                    unsafe_allow_html=True
                )

        else:

            st.warning(
                "No se pudo construir la estructura completa "
                "de la proforma."
            )
        st.divider()

        # ====================================================
        # REGLAMENTO INSTITUCIONAL
        # ====================================================

        st.markdown(
            "### 📘 Reglamento de Convalidaciones UPRIT"
        )

        base_app = os.path.dirname(
            os.path.abspath(
                __file__
            )
        )

        ruta_reglamento = os.path.join(
            base_app,
            "reglamento_convalidaciones_uprit.pdf"
        )

        if os.path.exists(
            ruta_reglamento
        ):

            col_reg_1, col_reg_2 = st.columns(
                2
            )

            with col_reg_1:

                with open(
                    ruta_reglamento,
                    "rb"
                ) as archivo_reglamento:

                    st.download_button(
                        "📘 DESCARGAR REGLAMENTO",
                        data=archivo_reglamento.read(),
                        file_name=(
                            "reglamento_convalidaciones_uprit.pdf"
                        ),
                        mime="application/pdf",
                        use_container_width=True
                    )

            with col_reg_2:

                mostrar_reglamento = st.checkbox(
                    "👁️ Mostrar reglamento",
                    key="mostrar_reglamento_uprit"
                )

            if mostrar_reglamento:

                with st.container(
                    border=True
                ):

                    mostrar_pdf_local(
                        ruta_reglamento,
                        altura=650
                    )

        else:

            st.warning(
                "Coloque el archivo "
                "`reglamento_convalidaciones_uprit.pdf` "
                "en la carpeta principal del sistema."
            )

        st.divider()

        # ====================================================
        # PASO 4 - APROBACIÓN DEL COORDINADOR
        # ====================================================

        mostrar_stepper(
            4
        )

        st.markdown(
            "### ✍️ Firma y aprobación del coordinador"
        )

        st.info(
            "La validación del coordinador se registra mediante "
            "**FIRMAR Y APROBAR**. Esta aprobación genera una constancia "
            "independiente de revisión; la proforma oficial conserva "
            "las firmas institucionales que ya forman parte del formato."
        )

        st.info(
            "Antes de aprobar, confirme que contrastó el certificado "
            "con **todas las filas de la proforma**, incluidas las que "
            "quedaron sin asignatura convalidante. Puede completar o "
            "corregir la tabla mientras el expediente no esté aprobado."
        )

        nombre_coordinador = st.text_input(
            "Nombre del coordinador",
            value=aprobacion_actual.get(
                "nombre",
                ""
            ),
            disabled=aprobado,
            key="nombre_coordinador_revision"
        )

        aceptacion = st.checkbox(
            "He revisado el certificado y la propuesta y autorizo "
            "la validación del expediente.",
            value=aprobado,
            disabled=aprobado,
            key="aceptacion_revision_coordinador"
        )

        if not aprobado:

            if st.button(
                "✍️ FIRMAR Y APROBAR",
                type="primary",
                use_container_width=True,
                key="btn_aprobar_coordinador"
            ):

                if not nombre_coordinador.strip():

                    st.error(
                        "Ingrese el nombre del coordinador."
                    )

                elif not aceptacion:

                    st.error(
                        "Confirme la revisión antes de aprobar."
                    )

                else:

                    # La firma es una validación interna mediante el botón.
                    # No se solicita cargar una imagen de firma.
                    ruta_firma = None

                    fecha = datetime.now(
                        ZoneInfo(
                            "America/Lima"
                        )
                    ).strftime(
                        "%d/%m/%Y %H:%M"
                    )

                    st.session_state[
                        "firma_coordinador_path"
                    ] = ruta_firma

                    st.session_state[
                        "aprobacion_coordinador"
                    ] = {
                        "aprobado":
                            True,
                        "nombre":
                            nombre_coordinador.strip(),
                        "cargo":
                            "Coordinador de "
                            + carrera_destino,
                        "fecha":
                            fecha
                    }

                    st.rerun()

        else:

            st.success(
                "✅ Expediente aprobado por "
                f"{aprobacion_actual.get('nombre', '')} "
                f"el {aprobacion_actual.get('fecha', '')}."
            )

            st.caption(
                "La aprobación bloquea temporalmente la edición. "
                "Si necesita corregir algo, use **EDITAR NUEVAMENTE**. "
                "Las selecciones realizadas se conservarán."
            )

            if st.button(
                "✏️ EDITAR NUEVAMENTE",
                use_container_width=True,
                key="btn_editar_nuevamente"
            ):

                # Quitar únicamente la aprobación y los documentos
                # generados. Se conservan las selecciones/editados
                # para que el coordinador continúe desde donde quedó.
                st.session_state.pop(
                    "aprobacion_coordinador",
                    None
                )

                st.session_state.pop(
                    "ruta_word_generado",
                    None
                )

                st.session_state.pop(
                    "ruta_reporte_especial",
                    None
                )

                st.session_state.pop(
                    "ruta_constancia_aprobacion",
                    None
                )

                st.rerun()


    # ========================================================
    # PASO 5 - RESULTADO FINAL
    # ========================================================

    aprobacion_para_paso_final = st.session_state.get(
        "aprobacion_coordinador",
        {}
    )

    if aprobacion_para_paso_final.get(
        "aprobado"
    ):
        mostrar_stepper(
            5
        )

    # ========================================================
    # GENERAR WORD
    # ========================================================

    with st.container(
        border=True
    ):

        titulo_seccion(
            "8. Generar proforma oficial"
        )

        aprobacion_coordinador = st.session_state.get(
            "aprobacion_coordinador",
            {}
        )

        expediente_aprobado = bool(
            aprobacion_coordinador.get(
                "aprobado"
            )
        )

        convalidaciones_para_word = st.session_state.get(
            "convalidaciones_editadas",
            convalidaciones
        )

        # Utilizar los pendientes REALES después de la edición manual.
        suficiencias_para_word = st.session_state.get(
            "suficiencias_revision_actuales",
            suficiencias
        )

        cantidad_suficiencias_actual = len(
            suficiencias_para_word
        )

        reglas_carrera_word = resultado.get(
            "reglas_carrera",
            {}
        )

        permitir_caso_especial_word = bool(
            reglas_carrera_word.get(
                "generar_caso_especial",
                True
            )
        )

        caso_especial_actual = st.session_state.get(
            "caso_especial_revision_actual",
            (
                permitir_caso_especial_word
                and cantidad_suficiencias_actual > 7
            )
        )

        # Si ya no corresponde caso especial, eliminar cualquier
        # referencia antigua para que no vuelva a aparecer el botón.
        if not caso_especial_actual:
            st.session_state.pop(
                "ruta_reporte_especial",
                None
            )

        datos_para_word = {
            "nombre":
                nombre,
            "institucion":
                institucion,
            "carrera":
                carrera_procedencia,
            "carrera_procedencia":
                carrera_procedencia,
            "carrera_destino":
                carrera_destino,
            "dni":
                dni,
            "telefono":
                telefono,
            "email":
                email
        }

        if cantidad_reales == 0:

            st.warning(
                "⚠️ No se encontraron convalidaciones directas. "
                "La proforma se podrá generar para revisión."
            )

        if convalidaciones_sin_nota_parcial:

            st.warning(
                f"⚠️ Hay {len(convalidaciones_sin_nota_parcial)} "
                "convalidaciones con nota parcial no detectada."
            )

            with st.expander(
                "Ver cursos emparejados sin nota parcial"
            ):

                st.dataframe(
                    pd.DataFrame(
                        convalidaciones_sin_nota_parcial
                    ),
                    width="stretch",
                    hide_index=True
                )

        if convalidaciones_sin_nota_convalidante:

            st.warning(
                f"⚠️ Hay {len(convalidaciones_sin_nota_convalidante)} "
                "filas sin nota convalidante calculada."
            )

            with st.expander(
                "Ver cursos sin nota convalidante"
            ):

                st.dataframe(
                    pd.DataFrame(
                        convalidaciones_sin_nota_convalidante
                    ),
                    width="stretch",
                    hide_index=True
                )

        if caso_especial_actual:

            st.warning(
                "⚠️ CASO ESPECIAL: actualmente existen "
                f"{cantidad_suficiencias_actual} cursos pendientes "
                "de suficiencia. Deben reducirse a 7 o menos "
                "mediante la revisión académica."
            )

        if es_revision_manual_ui:

            st.info(
                "📄 Revise y ajuste manualmente las equivalencias recomendadas. "
                "Después de aprobar, el sistema generará la proforma oficial "
                "sin documento adicional de CASO ESPECIAL."
            )

        elif (
            not caso_especial_actual
            and cantidad_suficiencias_actual <= 7
        ):

            st.success(
                "✅ La revisión manual dejó "
                f"{cantidad_suficiencias_actual} curso(s) pendiente(s) "
                "de suficiencia. Ya no corresponde generar un documento "
                "de CASO ESPECIAL."
            )

        else:

            st.info(
                "📄 Puede generar la proforma aunque existan "
                "observaciones. Si corresponde, se generará también "
                "el documento independiente de CASO ESPECIAL."
            )


        # ====================================================
        # BOTÓN GENERAR
        # ====================================================

        if not expediente_aprobado:

            st.warning(
                "⚠️ El coordinador debe aprobar el expediente "
                "antes de generar la proforma oficial."
            )

        if st.button(
            "📄 GENERAR PROFORMA WORD",
            type="primary",
            use_container_width=True,
            disabled=(
                not expediente_aprobado
            )
        ):

            try:

                parametros_generador = (
                    inspect.signature(
                        generar_word
                    ).parameters
                )

                argumentos_word = {
                    "datos_alumno":
                        datos_para_word,
                    "convalidaciones":
                        convalidaciones_para_word,
                    "suficiencias":
                        suficiencias_para_word
                }

                if (
                    "ruta_formato"
                    in parametros_generador
                ):

                    argumentos_word[
                        "ruta_formato"
                    ] = ruta_formato

                if (
                    "competencias"
                    in parametros_generador
                ):

                    argumentos_word[
                        "competencias"
                    ] = competencias

                if (
                    "caso_especial"
                    in parametros_generador
                ):

                    argumentos_word[
                        "caso_especial"
                    ] = caso_especial_actual

                if (
                    "observacion_caso_especial"
                    in parametros_generador
                ):

                    argumentos_word[
                        "observacion_caso_especial"
                    ] = (
                        observacion_caso_especial
                        if caso_especial_actual
                        else ""
                    )

                if (
                    "suficiencias_iniciales"
                    in parametros_generador
                ):
                    argumentos_word[
                        "suficiencias_iniciales"
                    ] = suficiencias_iniciales

                if (
                    "suficiencias_post_revision_completas"
                    in parametros_generador
                ):
                    argumentos_word[
                        "suficiencias_post_revision_completas"
                    ] = suficiencias_post_revision_completas

                if (
                    "suficiencias_excedentes_revision"
                    in parametros_generador
                ):
                    argumentos_word[
                        "suficiencias_excedentes_revision"
                    ] = suficiencias_excedentes_revision

                if (
                    "recomendaciones_caso_especial"
                    in parametros_generador
                ):
                    argumentos_word[
                        "recomendaciones_caso_especial"
                    ] = recomendaciones_caso_especial

                if (
                    "aprobacion_coordinador"
                    in parametros_generador
                ):
                    argumentos_word[
                        "aprobacion_coordinador"
                    ] = aprobacion_coordinador

                if (
                    "firma_coordinador_path"
                    in parametros_generador
                ):
                    argumentos_word[
                        "firma_coordinador_path"
                    ] = st.session_state.get(
                        "firma_coordinador_path"
                    )

                ruta_word = generar_word(
                    **argumentos_word
                )

                if (
                    not ruta_word
                    or not os.path.exists(
                        ruta_word
                    )
                ):

                    raise FileNotFoundError(
                        "El generador terminó, pero no se "
                        "encontró el archivo Word principal."
                    )

                st.session_state[
                    "ruta_word_generado"
                ] = ruta_word

                ruta_especial = getattr(
                    generar_word,
                    "ultimo_reporte_especial",
                    None
                )

                if (
                    caso_especial_actual
                    and ruta_especial
                    and os.path.exists(
                        ruta_especial
                    )
                ):

                    st.session_state[
                        "ruta_reporte_especial"
                    ] = ruta_especial

                else:

                    st.session_state.pop(
                        "ruta_reporte_especial",
                        None
                    )

                ruta_constancia = getattr(
                    generar_word,
                    "ultima_constancia_aprobacion",
                    None
                )

                if (
                    ruta_constancia
                    and os.path.exists(
                        ruta_constancia
                    )
                ):

                    st.session_state[
                        "ruta_constancia_aprobacion"
                    ] = ruta_constancia

                else:

                    st.session_state.pop(
                        "ruta_constancia_aprobacion",
                        None
                    )

                resumen_escritura = getattr(
                    generar_word,
                    "ultimo_resumen_escritura",
                    {}
                )

                if isinstance(
                    resumen_escritura,
                    dict
                ):

                    st.session_state[
                        "resumen_escritura_word"
                    ] = resumen_escritura

                st.success(
                    "✅ Proforma Word generada correctamente."
                )

                if ruta_constancia:
                    st.success(
                        "✅ También se generó una constancia independiente "
                        "de revisión y aprobación."
                    )

                if (
                    ruta_especial
                    and not es_revision_manual_ui
                ):

                    st.warning(
                        "⚠️ También se generó el documento "
                        "de CASO ESPECIAL."
                    )

            except Exception as error:

                st.error(
                    "❌ No se pudo generar el documento Word."
                )

                st.exception(
                    error
                )


        # ====================================================
        # DESCARGA WORD
        # ====================================================

        ruta_word_guardado = st.session_state.get(
            "ruta_word_generado"
        )

        if (
            ruta_word_guardado
            and os.path.exists(
                ruta_word_guardado
            )
        ):

            with open(
                ruta_word_guardado,
                "rb"
            ) as archivo_word:

                contenido_word = (
                    archivo_word.read()
                )

            st.download_button(
                label="⬇ DESCARGAR PROFORMA WORD",
                data=contenido_word,
                file_name=os.path.basename(
                    ruta_word_guardado
                ),
                mime=(
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True
            )


        # ====================================================
        # DESCARGA CASO ESPECIAL
        # ====================================================

        ruta_reporte_especial = st.session_state.get(
            "ruta_reporte_especial"
        )

        if (
            caso_especial_actual
            and ruta_reporte_especial
            and os.path.exists(
                ruta_reporte_especial
            )
        ):

            with open(
                ruta_reporte_especial,
                "rb"
            ) as archivo_especial:

                contenido_especial = (
                    archivo_especial.read()
                )

            st.download_button(
                label="⬇ DESCARGAR CASO ESPECIAL",
                data=contenido_especial,
                file_name=os.path.basename(
                    ruta_reporte_especial
                ),
                mime=(
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True
            )



        # ====================================================
        # DESCARGA CONSTANCIA DE APROBACIÓN
        # ====================================================

        ruta_constancia_aprobacion = (
            st.session_state.get(
                "ruta_constancia_aprobacion"
            )
        )

        if (
            ruta_constancia_aprobacion
            and os.path.exists(
                ruta_constancia_aprobacion
            )
        ):

            with open(
                ruta_constancia_aprobacion,
                "rb"
            ) as archivo_constancia:

                contenido_constancia = (
                    archivo_constancia.read()
                )

            st.download_button(
                label="⬇ DESCARGAR CONSTANCIA DE APROBACIÓN",
                data=contenido_constancia,
                file_name=os.path.basename(
                    ruta_constancia_aprobacion
                ),
                mime=(
                    "application/"
                    "vnd.openxmlformats-"
                    "officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True
            )


        # ----------------------------------------------------
        # VOLVER A EDITAR DESPUÉS DE DESCARGAR
        # ----------------------------------------------------

        if st.session_state.get(
            "aprobacion_coordinador",
            {}
        ).get(
            "aprobado"
        ):

            st.info(
                "¿Necesita hacer un cambio después de descargar? "
                "Puede reabrir la revisión sin perder las selecciones realizadas."
            )

            if st.button(
                "✏️ VOLVER A EDITAR LA CONVALIDACIÓN",
                use_container_width=True,
                key="btn_volver_editar_post_descarga"
            ):

                st.session_state.pop(
                    "aprobacion_coordinador",
                    None
                )

                st.session_state.pop(
                    "ruta_word_generado",
                    None
                )

                st.session_state.pop(
                    "ruta_reporte_especial",
                    None
                )

                st.session_state.pop(
                    "ruta_constancia_aprobacion",
                    None
                )

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer-uprit">'
    '<span>Elaborado por el Ing. Enrique Jannier Boy Vasquez</span>'
    '</div>',
    unsafe_allow_html=True
)
