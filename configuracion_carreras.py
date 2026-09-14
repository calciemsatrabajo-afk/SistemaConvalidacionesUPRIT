import json
import os
import unicodedata


# ============================================================
# RUTAS BASE
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CARPETAS_CARRERAS = os.path.join(
    BASE_DIR,
    "Carreras"
)


# ============================================================
# NORMALIZAR TEXTO AUXILIAR
# ============================================================

def normalizar_nombre(texto):
    if texto is None:
        return ""

    texto = str(texto).strip()

    texto = unicodedata.normalize(
        "NFC",
        texto
    )

    return texto


# ============================================================
# BUSCAR ARCHIVO SIN DEPENDER DE MAYÚSCULAS / TILDES
# ============================================================

def buscar_archivo_en_carpeta(
    carpeta,
    nombre_esperado
):
    """
    Busca un archivo dentro de una carpeta sin depender
    estrictamente de mayúsculas/minúsculas.

    Devuelve la ruta encontrada o None.
    """

    if not os.path.isdir(carpeta):
        return None

    esperado = nombre_esperado.lower().strip()

    for nombre in os.listdir(carpeta):

        if nombre.lower().strip() == esperado:
            return os.path.join(
                carpeta,
                nombre
            )

    return None


# ============================================================
# OBTENER CARRERAS
# ============================================================

def obtener_carreras():
    """
    Lee todas las carpetas dentro de Carreras.

    Una carrera será cargada si:
    - existe configuracion.json válido;
    - existe la proforma indicada;
    - existe el Excel indicado.

    También agrega información de diagnóstico para poder saber
    por qué una carrera no fue cargada.
    """

    carreras = {}
    diagnostico = []

    if not os.path.exists(
        CARPETAS_CARRERAS
    ):
        diagnostico.append({
            "carpeta":
                CARPETAS_CARRERAS,
            "estado":
                "ERROR",
            "detalle":
                "No existe la carpeta Carreras."
        })

        return carreras

    for nombre_carpeta in sorted(
        os.listdir(
            CARPETAS_CARRERAS
        )
    ):

        ruta_carpeta = os.path.join(
            CARPETAS_CARRERAS,
            nombre_carpeta
        )

        if not os.path.isdir(
            ruta_carpeta
        ):
            continue

        # ----------------------------------------------------
        # BUSCAR configuracion.json
        # ----------------------------------------------------

        ruta_config = buscar_archivo_en_carpeta(
            ruta_carpeta,
            "configuracion.json"
        )

        if not ruta_config:

            diagnostico.append({
                "carpeta":
                    nombre_carpeta,
                "estado":
                    "IGNORADA",
                "detalle":
                    "No existe configuracion.json."
            })

            continue

        # ----------------------------------------------------
        # LEER JSON
        # ----------------------------------------------------

        try:

            with open(
                ruta_config,
                "r",
                encoding="utf-8-sig"
            ) as archivo:

                config = json.load(
                    archivo
                )

        except Exception as error:

            diagnostico.append({
                "carpeta":
                    nombre_carpeta,
                "estado":
                    "ERROR",
                "detalle":
                    f"configuracion.json inválido: {error}"
            })

            continue

        # ----------------------------------------------------
        # DATOS DE CONFIGURACIÓN
        # ----------------------------------------------------

        nombre_carrera = normalizar_nombre(
            config.get(
                "nombre",
                nombre_carpeta
            )
        )

        nombre_formato = config.get(
            "formato",
            "formato.docx"
        )

        nombre_alumnos = config.get(
            "archivo_alumnos",
            "alumnos.xlsx"
        )

        # ----------------------------------------------------
        # BUSCAR FORMATO
        # ----------------------------------------------------

        ruta_formato = buscar_archivo_en_carpeta(
            ruta_carpeta,
            nombre_formato
        )

        if not ruta_formato:

            diagnostico.append({
                "carpeta":
                    nombre_carpeta,
                "estado":
                    "ERROR",
                "detalle":
                    f"No se encontró {nombre_formato}."
            })

            continue

        # ----------------------------------------------------
        # BUSCAR EXCEL
        # ----------------------------------------------------

        ruta_alumnos = buscar_archivo_en_carpeta(
            ruta_carpeta,
            nombre_alumnos
        )

        if not ruta_alumnos:

            diagnostico.append({
                "carpeta":
                    nombre_carpeta,
                "estado":
                    "ERROR",
                "detalle":
                    f"No se encontró {nombre_alumnos}."
            })

            continue

        # ----------------------------------------------------
        # COMPLETAR CONFIG
        # ----------------------------------------------------

        config["nombre"] = (
            nombre_carrera
        )

        config["carpeta"] = (
            ruta_carpeta
        )

        config["ruta_formato"] = (
            ruta_formato
        )

        config["ruta_alumnos"] = (
            ruta_alumnos
        )

        carreras[
            nombre_carrera
        ] = config

        diagnostico.append({
            "carpeta":
                nombre_carpeta,
            "estado":
                "OK",
            "detalle":
                f"Cargada como {nombre_carrera}"
        })

    # Guardar diagnóstico global para poder consultarlo
    obtener_carreras.ultimo_diagnostico = (
        diagnostico
    )

    return carreras


# ============================================================
# OBTENER DIAGNÓSTICO
# ============================================================

def obtener_diagnostico_carreras():

    obtener_carreras()

    return getattr(
        obtener_carreras,
        "ultimo_diagnostico",
        []
    )


# ============================================================
# OBTENER CONFIGURACIÓN DE UNA CARRERA
# ============================================================

def obtener_configuracion_carrera(
    nombre_carrera
):

    carreras = obtener_carreras()

    return carreras.get(
        nombre_carrera
    )


# ============================================================
# OBTENER RUTA DE FORMATO
# ============================================================

def obtener_ruta_formato(
    nombre_carrera
):

    config = (
        obtener_configuracion_carrera(
            nombre_carrera
        )
    )

    if not config:
        return None

    ruta_formato = config.get(
        "ruta_formato"
    )

    if (
        ruta_formato
        and os.path.exists(
            ruta_formato
        )
    ):
        return ruta_formato

    return None


# ============================================================
# OBTENER RUTA DE ALUMNOS
# ============================================================

def obtener_ruta_alumnos(
    nombre_carrera
):

    config = (
        obtener_configuracion_carrera(
            nombre_carrera
        )
    )

    if not config:
        return None

    ruta_alumnos = config.get(
        "ruta_alumnos"
    )

    if (
        ruta_alumnos
        and os.path.exists(
            ruta_alumnos
        )
    ):
        return ruta_alumnos

    return None
