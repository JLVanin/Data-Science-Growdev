# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 1) Procure quem foi a pessoa que mais gastou?

from dados import abr_dados, dicionario

arquivo = 'compras.csv'

dados = abr_dados(arquivo)

info = dicionario(dados)

maior_compra = -1
indice_maior_compra = 0

for indice, linha in enumerate(info):
    if linha['compra'] > maior_compra:
        maior_compra = linha['compra']
        indice_maior_compra = indice

pessoa = info[indice_maior_compra]

print(f"A pessoa que mais gastou foi: {pessoa['nome']} {pessoa['sobrenome']}\nCompra no valor de R$ {pessoa['compra']}")
