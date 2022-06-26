# 1) Escrever um programa que lê 5 valores para a, um de cada vez, e conta
# quantos destes valores são negativos, escrevendo esta informação.
cont = 0
for a in range(5):
    a = int(input('Informe um valor: '))
    if a < 0:
        cont += 1
print(f'Valores negativos = {cont}')
    