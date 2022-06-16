# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 4) Qual foi o gasto por ano?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

gastos_ano = {}

for linha in info:
    ano = linha['ano']
    gasto = linha['compra']
    if ano not in gastos_ano:
        gastos_ano[ano] = gasto
    else:
        gastos_ano[ano] += gasto

for ano, gasto in gastos_ano.items():
    print(f'No ano de {ano} o total de gastos foi de R$ {gasto}')
