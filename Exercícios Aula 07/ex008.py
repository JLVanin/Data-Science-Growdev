# 8) Escreva uma função que conte o número de espaços em branco em uma
# frase passada como parâmetro.

frase = str(input('Digite uma frase: '))

def conta_espaços(frase):
    return frase.count(' ')

print(conta_espaços(frase))