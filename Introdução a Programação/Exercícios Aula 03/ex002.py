# 2) Faça um algoritmo que receba um valor negativo e retorne o seu valor
# absoluto (ex: recebe -5 e retorna 5).

num = int(input('Informe um valor negativo: '))
if num < 0:
    num *= -1
    print(f'O valor absoluto é {num}')
