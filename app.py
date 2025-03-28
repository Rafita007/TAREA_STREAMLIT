import streamlit as st
import requests

def obtener_clima(ciudad):
    url = f"https://wttr.in/{ciudad}?format=%t"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        try:
            temperatura = int(respuesta.text.replace("°C", "").strip())
            return temperatura
        except ValueError:
            return None
    else:
        return None

def obtener_recomendacion(temperatura):
    from openai import OpenAI
    cliente = OpenAI(api_key="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")
    prompt = f"La temperatura es {temperatura}°C. ¿Cómo debería vestirme?"
    respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

st.title("Asesor de Vestimenta según el Clima")
ciudad = st.text_input("Ingresa tu ciudad:")

if st.button("Obtener Clima y Recomendación"):
    temperatura = obtener_clima(ciudad)
    if temperatura is not None:
        recomendacion = obtener_recomendacion(temperatura)
        
        st.write(f"### Clima en {ciudad}")
        st.write(f"**Temperatura:** {temperatura}°C")
        st.write(f"**Recomendación:** {recomendacion}")
    else:
        st.error("No se pudo obtener el clima. Verifica el nombre de la ciudad.")