# 3) Um brechó revende produtos usados, e fixa o preço de venda de cada
# produto conforme o valor de sua aquisição. Se o preço de aquisição de um
# produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45%
# maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de
# venda.

valor_aquisição = float(input('Digite o valor do produto: '))
if valor_aquisição <= 50:
    valor_venda = valor_aquisição + (valor_aquisição * 45 / 100)
    print(f'Valor de venda do produto é R$ {valor_venda}')
else:
   valor_venda = valor_aquisição + (valor_aquisição * 30 / 100)
   print(f'Valor de venda do produto é R$ {valor_venda}')


