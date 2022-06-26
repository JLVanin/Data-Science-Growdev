# 7) Escreva um programa que leia 10 valores e encontre o maior e o menor
# deles. Mostre o resultado.
maior = menor = 0
lista = []
for valor in range(3):
    lista.append(int(input(f'Digite o valor na posição {valor}: ')))
    if valor == 0:
        maior = menor = lista[valor]
    else:
        if lista[valor] > maior:
            maior = lista[valor]
        if lista[valor] < menor:
            menor = lista[valor]

print(f'Maior valor digitado foi {maior}')
print(f'Menor valor digitado foi {menor}')