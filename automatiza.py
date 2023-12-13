import pandas as pd

tabela = pd.read_excel('dados_manserv.xlsx')

tabela["Valor Total"] = tabela["Consumo"] * tabela["Preço"]

# Exporta tabela com outro nome

tabela.to_excel("dados_manserv_resultado.xlsx", index=False)
