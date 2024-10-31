import streamlit as st
import requests
import pandas as pd

st.markdown("Consulta Mídias")
with st.form("ConsultaMidias"):
    titulo = st.text_input("Informe parte do título aqui")
    botao = st.form_submit_button("Consulta")

    if botao:
        url = f"http://127.0.0.1:5000/midias/titulo/{titulo}"
        resp = requests.get(url)
        print(resp)
        if resp.status_code == 200:
            df = pd.DataFrame(resp.json())    
            st.write(df)
        else:
            st.write("Erro na consulta")
