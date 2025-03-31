import streamlit as st

st.set_page_config(page_title="Mi App", page_icon="📚", layout="wide")

st.title("Bienvenido a Mi Aplicación")
st.write("Selecciona una opción en el menú de la izquierda para continuar.")

# Streamlit muestra automáticamente las páginas dentro de "pages/"
st.sidebar.success("Selecciona una opción en el menú.")