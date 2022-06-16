# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 6) Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?
# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

jovens = 0
adultos = 0
idosos = 0

for pessoa in info:
    if pessoa['idade'] >= 18 and pessoa['idade'] <= 25:
        jovens += 1
    elif pessoa['idade'] >= 26 and pessoa['idade'] <= 59:
        adultos += 1
    else:
        idosos += 1

print(f'Jovens: {jovens} pessoas\nAdultos: {adultos} pessoas\nIdosos: {idosos} pessoas')
