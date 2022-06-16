# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 2) Busque qual são os anos da base de dados?

from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

anos = []

for linha in info:
    anos.append(linha['ano'])

resultado_anos = []

for elemento in anos:
    if elemento not in resultado_anos:
        resultado_anos.append(elemento)
        
#anos = list(set(anos))
print(f'Os anos da base de dados são:\n{resultado_anos}')
