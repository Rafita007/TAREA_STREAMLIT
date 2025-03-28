import streamlit as st
import openai

def analizar_respuestas(conversacion, api_key):
    client = openai.Client(api_key=api_key)
    prompt = f"Eres un psicólogo virtual. Analiza la siguiente conversación y proporciona un resumen breve sobre la personalidad y estado emocional del usuario.\n\nConversación:\n{conversacion}\n\nResultado:"  
    
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un psicólogo virtual empático y analítico."},
            {"role": "user", "content": prompt}
        ]
    )
    return respuesta.choices[0].message.content

st.title("🧠 Psicólogo Virtual")
st.write("Habla con el psicólogo virtual y recibe un análisis sobre tu estado emocional.")

api_key = st.secrets["openai_api_key"]  # Asegúrate de configurar tu clave en Streamlit Secrets
historial = st.text_area("Escribe sobre cómo te sientes hoy:")

if st.button("Obtener Análisis"):
    if historial.strip():
        resultado = analizar_respuestas(historial, api_key)
        st.subheader("📝 Análisis del Psicólogo Virtual")
        st.write(resultado)
    else:
        st.error("Por favor, escribe algo para analizar.")