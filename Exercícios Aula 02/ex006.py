# 6) Escreva um programa que receba a posição de dois pontos em um espaço
# 2D, ou seja, cada ponto tem coordenadas x e y, e calcule a distância entre
# esses dois pontos, exibindo-a na tela.

x_1 = int(input('Digita a primeira coordenada de A_x: '))
y_1 = int(input('Digita a segunda coordenada de A_y: '))
x_2 = int(input('Digita a primeira coordenada de B_x: '))
y_2 = int(input('Digita a segunda coordenada de B_y: '))

dist_a = (x_1, y_1)
dist_b = (x_2, y_2)

dist = ((x_2 - x_1)**2 + (y_2 - y_1)**2) **(1/2)

print(f'A distância entre A {dist_a} e B {dist_b} é: {dist:.2f}')