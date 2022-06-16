# 9) Escreva um algoritmo que receba um número e escreva “Par” caso esse
# número seja par e escreva “Impar” caso esse número seja impar.

num = int(input('Digite um número: '))

resultado = num % 2
if resultado == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')