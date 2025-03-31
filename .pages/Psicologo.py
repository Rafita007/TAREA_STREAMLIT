import streamlit as st
import openai

# Define tu API Key aquí
api_key = "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"

def analizar_respuestas(conversacion):
    client = openai.Client(api_key=api_key)
    prompt = f"Eres un psicólogo virtual. Analiza la siguiente conversación y proporciona un resumen breve sobre la personalidad y estado emocional del usuario. Responde de manera natural como si fueras un amigo\n\nConversación:\n{conversacion}\n\nResultado:"
    
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un psicólogo virtual empático y analítico."},
            {"role": "user", "content": prompt}
        ]
    )
    return respuesta.choices[0].message.content

st.title("🧠 Psicólogo Virtual")
st.write("Habla con el psicólogo virtual y recibe un análisis sobre tu personalidad y estado emocional.")

historial = st.text_area("Escribe aquí:")

if st.button("Obtener Análisis"):
    if historial.strip():
        resultado = analizar_respuestas(historial)
        st.subheader("📝 Análisis del Psicólogo Virtual")
        st.write(resultado)
    else:
        st.error("Por favor, escribe algo para analizar.")