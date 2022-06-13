# 19)Faça um programa que receba os coeficientes a, b e c da equação a seguir, e
#encontre as raízes por meio da fórmula de bhaskara.

#  ax2 + bx + c
#  Delta = b2 - 4 * a * c 

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b **2) - 4 * a * c

print(f'O valor de Delta é: {delta}')
r_delta = delta ** (1/2)

x_1 = (-b + (r_delta)) / (2 * a)
x_2 = (-b - (r_delta)) / (2 * a)

print(f'Valor de x1 é: {x_1}')
print(f'Valor de x2 é: {x_2}')


