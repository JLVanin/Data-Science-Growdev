# 23) Faça um programa que receba um valor no intervalo entre 0 e 1000, e
# converta para o valor correspondente ao intervalo -1 e 1.

valor = int(input('Digite um valor entre 0 e 1000: '))

dif = valor / 500 - 1
print(f'O valor {valor} convertido ao intervalo -1 e 1 é {dif}')