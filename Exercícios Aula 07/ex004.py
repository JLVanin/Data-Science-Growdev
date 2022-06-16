# 4) Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
# ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
# que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa.

linhas = int(input('Informe o número para linhas: '))
colunas = int(input('Informe o número de colunas: '))

def desenhaRetangulo(linhas, colunas):
    linhas = abs(linhas)
    colunas = abs(colunas)
    if linhas < 1:
        linhas = 1
    if colunas < 1:
        colunas = 1
    if linhas > 20:
        linhas = 20
    if colunas > 20:
        colunas = 20
    print('+', end = '')
    for i in range(colunas):
        print('-', end = '')
    print('+')
    for i in range(linhas):
        print('|', end = '')
        for j in range(colunas):
            print(' ', end = '')
        print('|')
    print('+', end = '')
    for i in range(colunas):
        print('-', end = '')
    print('+')
desenhaRetangulo(linhas, colunas)