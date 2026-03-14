import streamlit as st
import yfinance as yf
import pandas as pd
import json

st.title("📊 Dashboard de FIIs")

with open("carteira.json") as f:
    carteira = json.load(f)

dados = []

for ticker, cotas in carteira.items():

    ativo = yf.Ticker(ticker + ".SA")

    hist = ativo.history(period="1mo")

    preco = hist["Close"].iloc[-1]

    div = ativo.dividends.tail(1)

    if len(div) > 0:
        dividendo = div.iloc[0]
    else:
        dividendo = 0

    renda = dividendo * cotas

    dados.append({
        "FII": ticker,
        "Preço": preco,
        "Cotas": cotas,
        "Dividendo": dividendo,
        "Renda Mensal": renda
    })

df = pd.DataFrame(dados)

st.dataframe(df)

renda_total = df["Renda Mensal"].sum()

st.metric("💰 Renda mensal estimada", f"R$ {renda_total:.2f}")

st.bar_chart(df.set_index("FII")["Renda Mensal"])
