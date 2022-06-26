# 5) Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
# se a soma de dois deles resulta no terceiro.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

if num_1 + num_2 == num_3 or num_2 + num_3 == num_1 or num_3 + num_1 == num_2:
    print('A soma entre dois dos números digitados resulta no terceiro!')
else:
    print('A soma entre dois dos números digitados não tem como resultado o terceiro!')
    