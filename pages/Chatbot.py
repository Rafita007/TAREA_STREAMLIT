import streamlit as st
import openai
import os
import PyPDF2
from openai import OpenAI

# 🔑 Define aquí tu API Key de OpenAI (reemplázala con la tuya)
API_KEY = "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"

client = OpenAI(api_key=API_KEY)  # Crear el cliente de OpenAI con la API Key

st.title("📄 Chatbot con OpenAI y RAG")

# 📌 Función para extraer texto de un PDF
def extraer_texto_pdf(pdf_file):
    texto = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for pagina in pdf_reader.pages:
        texto += pagina.extract_text() + "\n"
    return texto

# 📌 Función para generar respuestas con OpenAI
def generar_respuesta(mensaje, contexto=""):
    try:
        # Usamos el método adecuado con el cliente OpenAI
        completion = client.chat.completions.create(  # Usando el nuevo método correcto
            model="gpt-4",  # Usa el modelo adecuado
            messages=[
                {"role": "system", "content": "Eres un asistente experto en análisis de documentos."},
                {"role": "user", "content": f"Contexto: {contexto}\n\nPregunta: {mensaje}"}
            ]
        )

        # Obtener la respuesta del modelo correctamente
        respuesta = completion.choices[0].message.content
        return respuesta

    except Exception as e:
        st.error(f"❌ Error en la API: {str(e)}")
        return ""

# 📌 Inicializar estados de sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

if "contexto" not in st.session_state:
    st.session_state.contexto = ""

# 📌 Cargar archivo PDF
archivo_pdf = st.file_uploader("📂 Sube un PDF para mejorar el chatbot", type=["pdf"])
if archivo_pdf:
    st.session_state.contexto = extraer_texto_pdf(archivo_pdf)
    st.success("✅ PDF cargado y procesado correctamente. Ahora puedes hacer preguntas sobre su contenido.")

# 📌 Mostrar el historial de conversación
for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# 📌 Entrada del usuario
ingreso_usuario = st.chat_input("📝 Escribe tu mensaje...")
if ingreso_usuario:
    st.session_state.historial.append({"role": "user", "content": ingreso_usuario})
    with st.chat_message("user"):
        st.markdown(ingreso_usuario)
    
    # 📌 Obtener la respuesta del chatbot con contexto del PDF
    respuesta_bot = ""
    with st.chat_message("assistant"):
        respuesta_area = st.empty()
        respuesta_bot = generar_respuesta(ingreso_usuario, st.session_state.contexto)
        respuesta_area.markdown(respuesta_bot)
    
    st.session_state.historial.append({"role": "assistant", "content": respuesta_bot})