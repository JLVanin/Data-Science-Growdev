# 8) Crie uma estrutura bidimensional utilizando listas com sublistas para para
# representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
# lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor
# numérico que significa:
# 0 - Água
# 1 - Navio
# Para cada posição escolha esses valores aleatoriamente, respeitando a regra
# de que não podem existir mais de 20 navios no tabuleiro. Após os valores
# serem distribuídos, o programa deve pedir ao usuário uma posição do
# tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
# até que o usuário derrote todos os navios ou chegue ao limite de 35
# tentativas.

from random import randint

linha = []
coluna = []
tabuleiro = [[0 for x in range(20)] for x in range(20)]
for linha in range(20):
    coluna = randint(0,19)
    tabuleiro[linha][coluna] = 1

tentativas = 0
acertos = 0
while True:
    linha = int(input('Informe uma linha de 0 - 19: '))
    coluna = int(input('Informe uma coluna de 0 - 19: '))
    if tabuleiro[linha][coluna] == 1:
        print('Você acertou: ')
        tabuleiro[linha][coluna] == 0
        acertos += 1 
    else:
        print('Você errou: ')
    tentativas += 1
    if tentativas == 35 or acertos == 20:
        break
if acertos == 20:
    print('Você ganhou!')
else:
    print('Você perdeu!')


