# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 7) Qual é a faixa etária que mais gasta?

from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

compras_jovens = 0
compras_adultos = 0
compras_idosos = 0

for i in info:
    if i["idade"] >= 18 and i["idade"] <= 25:
        compras_jovens += i["compra"]
    if i["idade"] >= 26 and i["idade"] <= 59:
        compras_adultos += i["compra"]
    if i["idade"] >= 60:
        compras_idosos += i["compra"]

if compras_jovens > compras_adultos and compras_jovens > compras_idosos:
    print("A faixa etária que mais gasta é a de: JOVENS")
elif compras_adultos > compras_jovens and compras_adultos > compras_idosos:
    print("A faixa etária que mais gasta é a de: ADULTOS")
else:
    print("A faixa etária que mais gasta é a de: IDOSOS")