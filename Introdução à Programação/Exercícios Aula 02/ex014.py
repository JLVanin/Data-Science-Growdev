# 14) Escreva um programa que leia dois números e faça a adição, subtração,
# divisão e multiplicação dos dois números, e após, exiba os 4 resultados
# calculados.

p_1 = int(input('Digite um número: '))
p_2 = int(input('Digite outro número: '))

sm = p_1 + p_2
sb = p_1 - p_2
mlt = p_1 * p_2
dv = p_1 / p_2

print(f'A soma dos valores é: {sm}')
print(f'A subtração dos valores é: {sb}')
print(f'A multiplicação dos valores é: {mlt}')
print(f'A divisão dos valores é: {dv:.2f}')