# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 5) Qual foi o ano com maior gasto?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

gastos = {}

for linha in info:
    ano = linha['ano']
    gasto = linha['compra']
    if ano not in gastos:
        gastos[ano] = gasto
    else:
        gastos[ano] += gasto

maior_gasto = 0

for ano in gastos:
    if gastos[ano] > maior_gasto:
        maior_gasto = gastos[ano]
        maior_ano = ano

print(f'O ano com maior gasto foi: {maior_ano}\nCom gasto de R$ {maior_gasto}')