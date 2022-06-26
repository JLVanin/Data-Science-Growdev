# 1) Escreva um algoritmo que receba dois números, exiba as opções:
# a) 1 - adição
# b) 2 - subtração
# Então peça ao usuário para escolher uma das opções. Caso escolha a opção
# 1 o algoritmo deve realizar a soma dos dois números lidos e exibir. Caso
# escolha a opção 2 o algoritmo deve realizar a subtração dos dois números
# lidos e exibir

print('Para adição digite 1.')
print('Para subtração digite 2.')
operador = int(input('Digite o operador: '))
print('---' * 15)
num_1 = float(input('Digite um valor: '))
num_2 = float(input('Digite outro valor: '))

if operador == 1:
    print(f'{num_1} + {num_2} = {num_1 + num_2}')
elif operador == 2:
    print(f'{num_1} - {num_2} = {num_1 - num_2}') 
else:
    print('Operador inválido')
print('---' * 15)


