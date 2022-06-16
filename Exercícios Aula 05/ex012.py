# 12) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Informe o número de termos que quer mostar: '))
termo_1 = 0
termo_2 = 1
soma = 1

for i in range(0, n):
    print(termo_1)
    soma = termo_2 + termo_1
    termo_1 = termo_2
    termo_2 = soma