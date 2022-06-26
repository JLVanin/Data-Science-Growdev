# 5) Construa um programa que permita a um usuário informar uma série de
# números, até que um número negativo seja fornecido. Ao final, imprima o
# somatório desses números, a média, o valor máximo e o mínimo.
# Desconsidere o último número (negativo) informado pelo usuário.

num = soma = cont = maior = menor = 0
lista = []
num = int(input('Digite um número: '))
while True:
    cont += 1 
    soma += num
    media = soma / cont
    lista.append(num)
    num = int(input('Digite um número: '))
    if num < 0:
        break
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
print(f'\nNúmeros digitados:\n {lista}')
print(f'Soma entre os números é: {soma}\nA média é: {media:.2f}\nValor máximo: {maior}\nValor mínimo: {menor}\n')



