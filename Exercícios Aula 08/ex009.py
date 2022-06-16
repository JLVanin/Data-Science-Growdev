# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 9) Qual o sobrenome que mais aparece na base de dados?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

sobrenome_quant = {} 

for i in info: 
    sobrenome = i['sobrenome'] 
    if sobrenome in sobrenome_quant: 
        sobrenome_quant[sobrenome] += 1 
    else: 
        sobrenome_quant[sobrenome] = 1

mais_sobrenome = 0

for sobrenome in sobrenome_quant:
    if sobrenome_quant[sobrenome] > mais_sobrenome:
        mais_sobrenome = sobrenome_quant[sobrenome]
        sobrenome_mais = sobrenome

print(f'O sobrenome que mais aparece na base de dados é: {sobrenome_mais}')
