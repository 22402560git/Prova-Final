import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Total de Mortes em cada dia - Região Sudeste", page_icon="📊", layout="wide")

tabela = pd.read_excel("acidentes.xlsx", header=None, skiprows=3)

st.title("Painel Streamlit do total de mortes na região sudeste")
st.write("Análise de mortes diárias dos estados de Minas Gerais e Rio de Janeiro.")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

df = pd.DataFrame(tabela)


CORES = {"Rio de Janeiro": "#FF6B6B", "Minas Gerais": "#00F5D4"}

if opcao == "Tabela":
    st.header("Tabela de barras")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)
    st.caption("Mortes diárias nos estados do Rio de Janeiro e Minas Gerais.")
else:
    st.header("Gráficos do Total de Mortes — Região Sudeste")

    st.subheader("Gráfico de Barras Agrupadas")
    fig = px.bar(df_tabela, x="DIA DA SEMANA", y="TOTAL DE ACIDENTES", color="NOMEUP", barmode="group",
                 title="Total de mortes no dia", color_discrete_map=CORES, template="plotly_dark")
    fig.update_xaxes(type="category")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
st.caption("Fonte indicada no material: — https://dados.pbh.gov.br/")