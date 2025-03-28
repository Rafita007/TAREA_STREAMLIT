import streamlit as st
import openai

# Define tu API Key aquí
api_key = "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"

def analizar_respuestas(conversacion):
    client = openai.Client(api_key=api_key)
    prompt = f"Eres un psicólogo virtual. Analiza la siguiente conversación y proporciona un resumen breve sobre la personalidad y estado emocional del usuario. Responde de manera natural y lo más humano posible\n\nConversación:\n{conversacion}\n\nResultado:"
    
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

historial = st.text_area("Escribe aquí:")

if st.button("Obtener Análisis"):
    if historial.strip():
        resultado = analizar_respuestas(historial)
        st.subheader("📝 Análisis del Psicólogo Virtual")
        st.write(resultado)
    else:
        st.error("Por favor, escribe algo para analizar.")