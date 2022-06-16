# 1) Faça um Programa que leia um vetor de 10 números reais e mostre-os na
# ordem inversa.

lista = []
for i in range(3):
    num = float(input(f'Digite o número na posição {i}: '))
    lista.append(num)
    inv_lista = lista[::-1]
print(f'\nLista digitada {lista}')
print(f'Lista inversa {inv_lista}')