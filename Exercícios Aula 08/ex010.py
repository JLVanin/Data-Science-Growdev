# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 10)Qual foi o ano em que os homens mais usaram o crédito?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

ano = []
for i in info:
    if i['sexo'] == "M" and i['pagamento'] == "credito":
        ano.append(i['ano'])

count = {}
for i in ano:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

anos_count = 0
for ano in count:
    if count[ano] > anos_count:
        anos_count = count[ano]
        ano_credito = ano
        
print(f'O ano em que os homens mais usaram o crédito foi: {ano_credito}')