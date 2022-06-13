# 27) Conversão de graus Celsius para Fahrenheit – Crie um algoritmo que
# converta graus Celsius em Fahrenheit. A fórmula é a seguinte:

# F =9/5 C + 32

# O programa deve solicitar ao usuário que insira uma temperatura em graus
# Celsius e, em seguida, exiba a temperatura convertida em Fahrenheit. Após
# construir esse algoritmo, modifique-o para que converta graus Fahrenheit em
# graus Celsius.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32

print(f'A temperatura de {c} °C corresponde a {f} °F')

fr = float(input('Informe a temperatura em °F: '))
cl = (fr - 32) / 1.8

print(f'A temperatura de {fr} °F corresponde a {cl} °C')
