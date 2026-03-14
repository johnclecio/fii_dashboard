import json

from dados import buscar_dados

from graficos import grafico_renda

from simulador import simular

import schedule
import time


with open("carteira.json") as f:

    carteira = json.load(f)


df = buscar_dados(carteira)

print(df)


total = df["Renda Mensal"].sum()

print("\nRenda mensal estimada:", total)


grafico_renda(df)


resultado = simular(20000,0.01,120)

print("\nValor futuro:", resultado[-1])





def job():
    print("Atualizando carteira")

schedule.every().day.at("18:00").do(job)

while True:

    schedule.run_pending()

    time.sleep(60)
