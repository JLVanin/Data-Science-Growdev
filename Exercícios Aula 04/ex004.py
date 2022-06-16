# 4) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado na
# fórmula abaixo):
# c/5 = f-32/9

temp_f = float(input('Informe a temperatura em °F: '))
temp_c = (temp_f - 32) * (5 / 9)

print(f'Temperatura em °C: {temp_c:.2f}')