import os
import json
from openai import OpenAI


def obtener_cliente():
    api_key = os.getenv("DEEPSEEK_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable DEEPSEEK_API_KEY."
        )

    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )


def analizar_titulo_deepseek(
    texto_documento,
    carrera_destino,
    cursos_destino
):
    """
    Analiza un título o diploma cuando el documento
    no contiene suficientes asignaturas.

    IMPORTANTE:
    No debe inventar cursos ni afirmar convalidaciones.
    """

    cliente = obtener_cliente()

    lista_cursos = "\n".join(
        f"- {curso}"
        for curso in cursos_destino
    )

    prompt = f"""
Analiza el siguiente documento académico.

DOCUMENTO:
{texto_documento}

CARRERA UNIVERSITARIA DE DESTINO:
{carrera_destino}

CURSOS DE REFERENCIA DE LA CARRERA DE DESTINO:
{lista_cursos}

OBJETIVO:
Evaluar la compatibilidad académica general entre el título,
programa o carrera técnica detectada en el documento y la
carrera universitaria de destino.

REGLAS OBLIGATORIAS:

1. No inventes asignaturas que no aparezcan en el documento.
2. No afirmes que un curso está convalidado.
3. Si el documento solo contiene un título o diploma,
   analiza únicamente la afinidad general del campo profesional.
4. Identifica la institución de procedencia si aparece.
5. Identifica el programa, título o especialidad.
6. Justifica el resultado utilizando áreas académicas
   y profesionales relacionadas.
7. Explica también las principales diferencias o áreas
   no cubiertas.
8. El porcentaje representa COMPATIBILIDAD ACADÉMICA GENERAL,
   no porcentaje de cursos convalidados.
9. Si falta un plan de estudios de procedencia, indícalo
   expresamente.
10. No inventes una fuente web ni una URL.

Devuelve exclusivamente un objeto JSON válido con esta estructura:

{{
    "tipo_documento": "titulo",
    "institucion_detectada": "",
    "programa_detectado": "",
    "porcentaje": 0,
    "nivel": "",
    "areas_afines": [],
    "areas_no_cubiertas": [],
    "justificacion": "",
    "advertencia": ""
}}
"""

    response = cliente.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un evaluador académico. "
                    "Debes responder en JSON. "
                    "No inventes cursos, instituciones, "
                    "mallas ni fuentes."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={
            "type": "json_object"
        },
        max_tokens=2000,
        stream=False
    )

    contenido = response.choices[0].message.content

    if not contenido:
        raise ValueError(
            "DeepSeek devolvió una respuesta vacía."
        )

    return json.loads(contenido)