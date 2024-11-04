import streamlit as st
import requests

def converte_dicionario_lista(dados: list, chave: str) -> list:
    lista = ['']
    for info in dados:
        lista.append(info[chave])
    return lista

def busca(lista: list, chave: str, valor: str) -> int:
    for reg in lista:
        if reg[chave] == valor:
            return reg['id']
    return -1
 
st.markdown("Assistir/Preferencias mídias")

midias = requests.get("http://127.0.0.1:5000/midias")
usuarios = requests.get("http://127.0.0.1:5000/usuarios")
if midias.status_code == 200 and usuarios.status_code == 200:

    list_usuarios = converte_dicionario_lista(usuarios.json(), 'nome')
    list_midias = converte_dicionario_lista(midias.json(), 'titulo')

    with st.form("form"):
        col1, col2 = st.columns(2)
        with col1:
            user = st.selectbox("usuários", options=list_usuarios)
        
        with col2:
            midia = st.selectbox("filmes", options=list_midias)
        
        escolha = st.radio("Escolha", options=["assistir", "minha lista"])
        botao = st.form_submit_button("Associa")

        if botao:

            id_usuario = busca(usuarios.json(), 'nome', user)
            id_midia = busca(midias.json(), 'titulo', midia)

            url = "http://127.0.0.1:5000/midias/preferencia"
            if escolha == 'assistir':
                esc = 1
            else:
                esc = 2

            dado_json = {"id_usuario": id_usuario, "id_midia": id_midia, "tipo": esc}

            resp = requests.post(url, json=dado_json)
            if resp.status_code == 201:
                st.markdown(resp.json()['title'])
            else:
                st.markdown(resp.json()['title'])
else:
    st.markdown("Não foi possível trazer a lista de usuários e/ou de mídias")