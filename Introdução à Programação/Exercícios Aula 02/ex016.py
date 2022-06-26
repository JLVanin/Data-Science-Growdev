# 16) Faça um programa que receba o cateto oposto e o cateto adjacente de um
# triângulo e retorne a hipotenusa do mesmo.

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2)** (1/2)

print(f'A hipotenusa vai medir {hi:.2f}')