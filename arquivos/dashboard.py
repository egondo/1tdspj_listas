#pip install pandas
#pip install streamlit
#pip install matplotlib

import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.header("Dashboard de análise de faturamento")
dado_txt = st.file_uploader("arquivo faturamento")

if dado_txt:

    df = pd.read_csv(dado_txt, sep=";")

    df['total'] = df['quantidade'] * df['preco']

    df['dia'] = df['data'].apply(lambda y: int(y.split("/")[0]))
    df['mes'] = df['data'].apply(lambda y: int(y.split("/")[1]))

    df_ac_loja = pd.pivot_table(df, index="mes", columns="loja", aggfunc="sum", values="total")

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df_ac_loja)

    with col2:
        df_ac_loja.plot(kind="bar")
        plt.title('Faturamento mensal por loja')
        plt.xlabel('mes')
        plt.ylabel('total')
        st.pyplot(plt.gcf())

    df_total_produto = pd.pivot_table(df, index="mes", columns="produto", aggfunc="sum", values="total")

    list_produto = df['produto'].unique()
    prod_selecionado = st.selectbox("Produto", options=list_produto)

    if prod_selecionado:
        colA, colB = st.columns([3, 1])
        with colA:
            df_grafico = df_total_produto[prod_selecionado]
            st.bar_chart(df_grafico)

        with colB:
            df_lojas = pd.pivot_table(df.query(f'produto =="{prod_selecionado}"'), index="loja", aggfunc="sum", values="total")
            fig1, ax1 = plt.subplots()
            ax1.pie(df_lojas['total'], labels=['Centro', 'Jardins', 'Saúde', 'Tatuapé'], autopct='%1.1f%%',
            shadow=True, startangle=90)
            ax1.axis('equal')  
            st.pyplot(fig1)