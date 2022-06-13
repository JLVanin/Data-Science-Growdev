#3) Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular,
#utilizando a fórmula.
#VOLUME = COMPRIMENTO * LARGURA * ALTURA

print('Calculo de volume de uma caixa retangular')
print('===' * 15)
print('Digite as medidas em Centímetros')

com = float(input('Digite o comprimento: '))
lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))

volume = com * lar * alt
litros = volume / 1000

print('O volume da caixa em cm³ {}'.format(volume))
print('O volume da caixa em litros {}'.format(litros))
