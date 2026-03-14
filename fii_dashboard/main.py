import json
import schedule
import time

from dados import buscar_dados
from graficos import grafico_renda
from simulador import simular


# carregar carteira
with open("carteira.json") as f:
    carteira = json.load(f)

    


# buscar dados dos FIIs
df = buscar_dados(carteira)

print("Colunas:", df.columns)

df["Valor Investido"] = df["Preço"] * df["Cotas"]

print("\nTeste valor investido:")
print(df[["Ticker","Preço","Cotas","Valor Investido"]])

# calcular valor investido
df["Valor Investido"] = df["Preço"] * df["Cotas"]

# mostrar tabela completa
print("\nTabela da carteira:\n")
print(df[["Ticker","Preço","Cotas","Dividendo","Renda Mensal","Valor Investido"]])




print(df)


# renda mensal total
renda_total = df["Renda Mensal"].sum()

print("\nRenda mensal estimada:", renda_total)


# total investido
total_investido = df["Valor Investido"].sum()

print("\nTotal investido:", total_investido)

df["% Carteira"] = (df["Valor Investido"] / df["Valor Investido"].sum()) * 100


# gráfico da renda
grafico_renda(df)


# simulação de investimento
resultado = simular(20000, 0.01, 120)

print("\nValor futuro:", resultado[-1])


# tarefa automática
def job():
    print("Atualizando carteira...")
    df = buscar_dados(carteira)
    print(df)


schedule.every().day.at("18:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(60)