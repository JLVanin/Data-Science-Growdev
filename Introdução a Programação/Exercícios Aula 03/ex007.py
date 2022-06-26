# 7) Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros
# e verifique se o resultado da soma é maior que o terceiro número lido.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

if (num_1 + num_2) > num_3:
    print(f'A soma entre {num_1} e {num_2} é maior que {num_3}')
else:
    print(f'O resultado da soma entre {num_1} e {num_2} não é maior que o terceiro número.')