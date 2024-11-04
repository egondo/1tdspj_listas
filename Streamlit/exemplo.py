#pip install streamlit
import streamlit as st
import requests

st.write("Hello World!")

st.page_link("exemplo.py", label="Cadastra", icon="🏠")
st.page_link("pages/consulta.py", label="Consulta", icon="1️⃣")
st.page_link("pages/assistir.py", label="Assistir filme")


with st.form("Formulario cadastro de filme"):
    titulo = st.text_input("Título: ")
    categoria = st.text_input("Categoria: ")
    tipo = st.radio("Tipo da mídia", ["Filme", "Série"])

    botao = st.form_submit_button("Cadastra")

    if botao:
        if tipo == "Filme":
            midia = {"titulo": titulo, "categoria": categoria, "tipo": "F"}
        else:   
            midia = {"titulo": titulo, "categoria": categoria, "tipo": "S"}

        url = "http://127.0.0.1:5000/midias"
        resp = requests.post(url, json=midia)
        if resp.status_code == 201:
            st.warning("Mídia cadastrada com sucesso")
        else:
            info = resp.json()
            st.warning(info['title'])