import re
import unicodedata
from pathlib import Path

import pandas as pd
from rapidfuzz import fuzz


# ============================================================
# CARPETA PRINCIPAL DEL PROYECTO
# ============================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent


# ============================================================
# NORMALIZAR TEXTO
# ============================================================

def normalizar(texto):

    if texto is None:
        return ""

    try:
        if pd.isna(texto):
            return ""
    except:
        pass

    texto = str(texto)

    # Quitar caracteres invisibles frecuentes de Excel
    texto = texto.replace("\xa0", " ")

    texto = texto.strip()

    # Quitar tildes
    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    # Mayúsculas
    texto = texto.upper()

    # Quitar signos y puntuación
    texto = re.sub(
        r"[^A-Z0-9 ]",
        " ",
        texto
    )

    # Eliminar espacios dobles
    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()


# ============================================================
# NORMALIZAR PARA COMPARAR SIN IMPORTAR ORDEN
# ============================================================

def nombre_ordenado(texto):

    texto = normalizar(texto)

    palabras = texto.split()

    palabras = sorted(palabras)

    return " ".join(palabras)


# ============================================================
# OBTENER RUTA DEL EXCEL DE LA CARRERA
# ============================================================

def obtener_ruta_excel(ruta_excel=None):

    # --------------------------------------------------------
    # NUEVO SISTEMA MULTICARRERA
    # --------------------------------------------------------

    if ruta_excel:

        archivo = Path(ruta_excel)

        if not archivo.is_absolute():
            archivo = CARPETA_PROYECTO / archivo

        return archivo

    # --------------------------------------------------------
    # COMPATIBILIDAD CON SISTEMA ANTIGUO
    #
    # Si por algún motivo app.py todavía no envía una ruta,
    # utilizará alumnos.xlsx de la carpeta principal.
    # --------------------------------------------------------

    return CARPETA_PROYECTO / "alumnos.xlsx"


# ============================================================
# CARGAR EXCEL
# ============================================================

def cargar_alumnos(ruta_excel=None):

    archivo_alumnos = obtener_ruta_excel(
        ruta_excel
    )

    if not archivo_alumnos.exists():

        return None, (
            f"No se encontró el archivo de alumnos: "
            f"{archivo_alumnos}"
        )

    try:

        df = pd.read_excel(
            archivo_alumnos,
            dtype=str
        )

    except Exception as error:

        return None, str(error)

    # --------------------------------------------------------
    # NORMALIZAR NOMBRES DE COLUMNAS
    # --------------------------------------------------------

    df.columns = [
        normalizar(columna).lower()
        for columna in df.columns
    ]

    df = df.fillna("")

    return df, None


# ============================================================
# LIMPIAR NÚMEROS DE EXCEL
# ============================================================

def limpiar_numero(valor):

    if valor is None:
        return ""

    valor = str(valor).strip()

    # Ejemplo:
    # 42190101.0 -> 42190101

    if re.fullmatch(
        r"\d+\.0",
        valor
    ):
        valor = valor[:-2]

    return valor


# ============================================================
# CONVERTIR FILA
# ============================================================

def convertir_fila(fila):

    return {

        "nombre":
            str(
                fila.get(
                    "nombre",
                    ""
                )
            ).strip(),

        "dni":
            limpiar_numero(
                fila.get(
                    "dni",
                    ""
                )
            ),

        "telefono":
            limpiar_numero(
                fila.get(
                    "telefono",
                    ""
                )
            ),

        "email":
            str(
                fila.get(
                    "email",
                    ""
                )
            ).strip()
    }


# ============================================================
# COMPARAR NOMBRES
# ============================================================

def calcular_afinidad(
    nombre_pdf,
    nombre_excel
):

    pdf = normalizar(
        nombre_pdf
    )

    excel = normalizar(
        nombre_excel
    )

    if not pdf or not excel:
        return 0

    # --------------------------------------------------------
    # CASO 1: EXACTAMENTE IGUALES
    # --------------------------------------------------------

    if pdf == excel:
        return 100

    # --------------------------------------------------------
    # CASO 2:
    # MISMAS PALABRAS, DIFERENTE ORDEN
    # --------------------------------------------------------

    if (
        nombre_ordenado(pdf)
        ==
        nombre_ordenado(excel)
    ):
        return 100

    # --------------------------------------------------------
    # CASO 3: COMPARACIÓN FLEXIBLE
    # --------------------------------------------------------

    puntuacion1 = fuzz.token_set_ratio(
        pdf,
        excel
    )

    puntuacion2 = fuzz.token_sort_ratio(
        pdf,
        excel
    )

    puntuacion3 = fuzz.WRatio(
        pdf,
        excel
    )

    return max(
        puntuacion1,
        puntuacion2,
        puntuacion3
    )


# ============================================================
# BUSCAR ALUMNO
# ============================================================

def buscar_alumno(
    nombre_detectado,
    ruta_excel=None
):

    nombre_pdf = normalizar(
        nombre_detectado
    )

    if not nombre_pdf:

        return {
            "encontrado": False,
            "tipo": "NOMBRE_VACIO",
            "afinidad": 0,
            "datos": {}
        }

    # --------------------------------------------------------
    # LEER EXCEL DE LA CARRERA SELECCIONADA
    # --------------------------------------------------------

    df, error = cargar_alumnos(
        ruta_excel
    )

    if df is None:

        return {
            "encontrado": False,
            "tipo": "SIN_BASE",
            "afinidad": 0,
            "datos": {},
            "error": error
        }

    # --------------------------------------------------------
    # VERIFICAR COLUMNAS
    # --------------------------------------------------------

    columnas_necesarias = [
        "nombre",
        "dni",
        "telefono",
        "email"
    ]

    for columna in columnas_necesarias:

        if columna not in df.columns:

            return {
                "encontrado": False,
                "tipo": "COLUMNA_FALTANTE",
                "afinidad": 0,
                "datos": {},
                "columna_faltante": columna,
                "columnas_excel": list(df.columns)
            }

    # --------------------------------------------------------
    # PASO 1:
    # BUSCAR COINCIDENCIA EXACTA
    # --------------------------------------------------------

    for _, fila in df.iterrows():

        nombre_excel = normalizar(
            fila["nombre"]
        )

        if not nombre_excel:
            continue

        if nombre_pdf == nombre_excel:

            return {
                "encontrado": True,
                "tipo": "EXACTA",
                "afinidad": 100,
                "datos": convertir_fila(
                    fila
                ),
                "nombre_pdf": nombre_detectado,
                "nombre_excel": fila["nombre"]
            }

    # --------------------------------------------------------
    # PASO 2:
    # MISMAS PALABRAS SIN IMPORTAR EL ORDEN
    # --------------------------------------------------------

    nombre_pdf_ordenado = nombre_ordenado(
        nombre_pdf
    )

    for _, fila in df.iterrows():

        nombre_excel = fila[
            "nombre"
        ]

        if (
            nombre_pdf_ordenado
            ==
            nombre_ordenado(
                nombre_excel
            )
        ):

            return {
                "encontrado": True,
                "tipo": "EXACTA",
                "afinidad": 100,
                "datos": convertir_fila(
                    fila
                ),
                "nombre_pdf": nombre_detectado,
                "nombre_excel": nombre_excel
            }

    # --------------------------------------------------------
    # PASO 3:
    # BÚSQUEDA APROXIMADA
    # --------------------------------------------------------

    mejor_fila = None
    mejor_nombre = ""
    mejor_afinidad = 0

    candidatos = []

    for _, fila in df.iterrows():

        nombre_excel = str(
            fila["nombre"]
        ).strip()

        if not nombre_excel:
            continue

        afinidad = calcular_afinidad(
            nombre_pdf,
            nombre_excel
        )

        candidatos.append({
            "nombre": nombre_excel,
            "afinidad": round(
                afinidad,
                1
            )
        })

        if afinidad > mejor_afinidad:

            mejor_afinidad = afinidad
            mejor_fila = fila
            mejor_nombre = nombre_excel

    # --------------------------------------------------------
    # ORDENAR LOS MEJORES CANDIDATOS
    # --------------------------------------------------------

    candidatos = sorted(
        candidatos,
        key=lambda x: x["afinidad"],
        reverse=True
    )

    candidatos = candidatos[:5]

    # --------------------------------------------------------
    # ACEPTAR 75% O MÁS
    # --------------------------------------------------------

    if (
        mejor_fila is not None
        and
        mejor_afinidad >= 75
    ):

        return {
            "encontrado": True,
            "tipo": "APROXIMADA",
            "afinidad": round(
                mejor_afinidad,
                1
            ),
            "datos": convertir_fila(
                mejor_fila
            ),
            "nombre_pdf": nombre_detectado,
            "nombre_excel": mejor_nombre,
            "candidatos": candidatos
        }

    # --------------------------------------------------------
    # NO ENCONTRADO
    # --------------------------------------------------------

    return {
        "encontrado": False,
        "tipo": "NO_ENCONTRADO",
        "afinidad": round(
            mejor_afinidad,
            1
        ),
        "datos": {},
        "nombre_pdf": nombre_detectado,
        "mejor_candidato": mejor_nombre,
        "candidatos": candidatos
    }