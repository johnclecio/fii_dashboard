import yfinance as yf
import pandas as pd

def buscar_dados(carteira):

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
            "Ticker": ticker,
            "Preço": preco,
            "Cotas": cotas,
            "Dividendo": dividendo,
            "Renda Mensal": renda
        })

    df = pd.DataFrame(dados)

    return df
