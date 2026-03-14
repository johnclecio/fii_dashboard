import streamlit as st
import json

from dados import buscar_dados

st.title("📊 Dashboard de FIIs")

# carregar carteira
with open("carteira.json") as f:
    carteira = json.load(f)

# buscar dados
df = buscar_dados(carteira)

# calcular valor investido
df["Valor Investido"] = df["Preço"] * df["Cotas"]

# totais
total_investido = df["Valor Investido"].sum()
renda_total = df["Renda Mensal"].sum()

# métricas
col1, col2 = st.columns(2)

col1.metric("💰 Total Investido", f"R$ {total_investido:,.2f}")
col2.metric("💵 Renda Mensal", f"R$ {renda_total:,.2f}")

# tabela
st.dataframe(df)

# gráfico
st.bar_chart(df.set_index("Ticker")["Renda Mensal"])