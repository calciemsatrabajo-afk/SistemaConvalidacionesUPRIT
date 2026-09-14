import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

respuesta = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "Responde de forma breve."
        },
        {
            "role": "user",
            "content": "Responde únicamente: CONEXION CORRECTA"
        }
    ]
)

print(respuesta.choices[0].message.content)