# 26) Escreva um programa que aceite uma quantidade de minutos e o converta
# em horas e dias. Por exemplo, 6.000 minutos equivalem a 100 horas e é igual
# a 4.167 dias.

min = int(input('Digite a quantidade de minutos: '))

horas = min / 60
dias = horas / 24

print(f'{min} minutos equivalem a {horas:.2f} horas e {dias:.3f} dias.')