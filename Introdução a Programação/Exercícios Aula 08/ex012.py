# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 12)Qual o valor gasto em compras por jovens do ano de 2010 até 2015?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

soma = 0

for i in range(len(info)):
    if info[i]['ano'] >= 2010 and info[i]['ano'] <= 2015 and info[i]['idade'] >= 18 and info[i]['idade'] <= 25:
        soma += info[i]['compra']
print('O valor gasto em compras por jovens do ano de 2010 até 2015 foi de R$', soma)