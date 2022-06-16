# 3) Escrever um programa que lê um valor N inteiro e positivo e que calcula e
# escreve o valor de E.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + … + 1 / N!

from math import factorial

num = int(input('Informe um valor inteiro e positivo: '))
e = 1
for i in range(1, num + 1 ):
    e += 1 / factorial(i)
print(f'Valor de E = {e}')