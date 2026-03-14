def simular(capital, taxa, meses):

    valor = capital

    historico = []

    for m in range(meses):

        renda = valor * taxa

        valor += renda

        historico.append(valor)

    return historico
