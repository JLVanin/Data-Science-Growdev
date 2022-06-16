# 10)Escreva um programa que recebe 10 valores e imprima o somatório dos
# elementos.
soma = 0
for i in range(10):
    valores = int(input(f'Digite o valor na posição {i}: '))
    soma += valores
print(f'A soma dos valores é: {soma}')
