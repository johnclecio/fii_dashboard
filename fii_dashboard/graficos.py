import matplotlib.pyplot as plt

def grafico_renda(df):

    plt.bar(df["Ticker"], df["Renda Mensal"])

    plt.title("Renda passiva por FII")

    plt.xlabel("FII")

    plt.ylabel("Dividendos")

    plt.show()
