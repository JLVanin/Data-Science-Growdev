# 21) Uma pessoa resolveu fazer uma aplicação em uma poupança programada.
# Para calcular seu rendimento, ela deverá fornecer o valor constante da
# aplicação mensal, a taxa e o número de meses. Sabendo-se que a fórmula
# usada para este cálculo é:

# P * (1 + i)n − 1 / i

# onde:
# ● i = taxa
# ● P = aplicação mensal
# ● n= número de meses
# Crie um programa que receba os coeficientes necessários e realize o cálculo.

apl = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 5 para 5%): "))
mês = int(input('Número de meses: '))

saldo = (apl * (1 + (taxa / 100))**mês)
print(f'O saldo em {mês} meses de aplicação é de R${saldo:.2f}')
lucro = saldo - apl
print(f'Com lucro de R$ {lucro:.2f} no período.')