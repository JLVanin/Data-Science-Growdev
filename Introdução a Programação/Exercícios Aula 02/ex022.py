# 22) Uma receita de biscoitos exige os seguintes ingredientes para produzir 48
# unidades:
# a) 1,5 xícaras de açúcar
# b) 1 xícara de manteiga
# c) 2,75 xícaras de farinha
# Crie um algoritmo que pergunte ao usuário quantos biscoitos ele deseja fazer
# e calcule a quantidade correspondente dos ingredientes.

biscoitos = int(input('Digite a quantidade de biscoitos que deseja fazer: '))
print(f'Para fazer {biscoitos} biscoitos você vai precisar de:')
ac = 1.5 / 48
ma = 1 / 48
fa = 2.75 / 48
print('{:.2f} xícaras de açúcar'.format(biscoitos * ac))
print('{:.2f} xícaras de manteiga'.format(biscoitos * ma))
print('{:.2f} xícaras de farinha'.format(biscoitos * fa))