import streamlit as st
from datasource.csv import CSVCollector
from contracts.catalogo import Catalogo

st.title("Portal de Dados")
st.write("Bem-vindo ao Portal de Dados!")

schema = {
    "Nome": str,
    "Idade": int,
    "Cidade": str
}

csv_collector = CSVCollector(schema, cell_range=None)

dados = csv_collector.start()

if dados is not None:
    st.success("Dados carregados com sucesso")
    st.dataframe(dados)
else:
    st.info("Aguardando upload do arquivo CSV")
