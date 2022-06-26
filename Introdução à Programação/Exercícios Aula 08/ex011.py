# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 11) Qual opção de pagamento é mais utilizada em cada faixa etária?

from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

pagamento_jovens = {}
pagamento_adultos = {}
pagamento_idosos = {}

for i in info:
    if i["idade"] >= 18 and i["idade"] <= 25:
        jovens = i["pagamento"]
        if jovens in pagamento_jovens:
            pagamento_jovens[jovens] += 1
        else:
            pagamento_jovens[jovens] = 1
    if i["idade"] >= 26 and i["idade"] <= 59:
        adultos = i["pagamento"]
        if adultos in pagamento_adultos:
            pagamento_adultos[adultos] += 1
        else:
            pagamento_adultos[adultos] = 1
    if i["idade"] >= 60:
        idosos = i["pagamento"]
        if idosos in pagamento_idosos:
            pagamento_idosos[idosos] += 1
        else:
            pagamento_idosos[idosos] = 1

jovens_pgt = adultos_pgt = idosos_pgt = 0

for jovens, adultos, idosos in pagamento_jovens, pagamento_adultos, pagamento_idosos:
    if pagamento_jovens[jovens] > jovens_pgt:
        jovens_pgt = pagamento_jovens[jovens]
        opcao_jovens_pgt = jovens
    if pagamento_adultos[adultos] > adultos_pgt:
        adultos_pgt = pagamento_adultos[adultos]
        opcao_adultos_pgt = adultos
    if pagamento_idosos[idosos] > idosos_pgt:
        idosos_pgt = pagamento_idosos[idosos]
        opcao_idosos_pgt = idosos

print(f'Opção de pagamento mais utilizada por faixa etária:\nJovens: {opcao_jovens_pgt}\nAdultos: {opcao_adultos_pgt}\nIdosos: {opcao_idosos_pgt}')

