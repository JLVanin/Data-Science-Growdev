# 20) Dado que uma empresa possui valores variáveis de suas ações ao longo do
# tempo, e que existe sempre uma taxa (que também é variável) a ser paga
# para realizar transações de compra e venda, escreva um programa que peça
# a quantidade de ações compradas, o valor da ação naquele período e qual a
# taxa que foi paga, peça também as mesmas informações em relação a venda
# de ações. O programa deve exibir:
# a) O valor total gasto na compra de ações
# b) O valor pago em taxa durante a compra
# c) O valor total ganho na venda das ações
# d) O valor pago na venda
# e) O valor de diferença total entre a compra e a venda

valor_c = float(input('Digite o valor da ação: '))
qnt_c = int(input('Digite a quantidade de ações que deseja comprar: '))
taxa_c = float(input('Taxa de transação: '))

total_c = (qnt_c * valor_c - taxa_c)

print(f'Total gasto na compra R$ {total_c}')
print('==='*20)
valor_v = float(input('Digite o valor de venda da ação: '))
qnt_v = int(input('Digite a quantidade de ações que deseja vender: '))
taxa_v = float(input('Taxa de transação: '))

total_v = qnt_v * valor_v - taxa_v

lucro = (total_v - total_c - taxa_v - taxa_c)
dif = (valor_v - valor_c)
if lucro >0:
    print(f'Seu lucro foi de R$ {lucro}')
else:
    print(f'Seu prejuizo foi de {lucro}')

print(f'A diferença entre o valor de compra e venda foi de R$ {dif:.2f}')


