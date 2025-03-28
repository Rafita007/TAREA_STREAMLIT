import streamlit as st
import openai

def analizar_respuestas(conversacion, api_key):
    prompt = f"""
    Eres un psicólogo virtual. Analiza la siguiente conversación y proporciona un resumen breve sobre la personalidad y estado emocional del usuario.
    Conversación:
    {conversacion}
    Resultado:
    """
    
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un psicólogo virtual empático y analítico."},
                  {"role": "user", "content": prompt}],
        api_key=api_key
    )
    return respuesta["choices"][0]["message"]["content"]

st.title("🧠 Psicólogo Virtual")
st.write("Habla con el psicólogo virtual y recibe un análisis sobre tu estado emocional.")

api_key = "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"  # Reemplázala con tu API Key de OpenAI
historial = st.text_area("Escribe sobre cómo te sientes hoy:")

if st.button("Obtener Análisis"):
    if historial.strip():
        resultado = analizar_respuestas(historial, api_key)
        st.subheader("📝 Análisis del Psicólogo Virtual")
        st.write(resultado)
    else:
        st.error("Por favor, escribe algo para analizar.")
