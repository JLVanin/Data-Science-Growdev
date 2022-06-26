# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 3) Qual a porcentagem de homens e mulheres na base de dados?
from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

homens = 0
mulheres = 0

for i in info:
    if i['sexo'] == 'M':
        homens += 1
    if i['sexo'] == 'F':
        mulheres += 1
total = homens + mulheres
p_homens = (homens / total) * 100
p_mulheres = (mulheres / total) * 100

print(f'A porcentagem de homens na base de dados é: {p_homens}%\nA porcentagem de mulheres na base de dados é: {p_mulheres}%.')
