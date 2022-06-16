# 5) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e
# colunas, com um número em cada posição e no qual a soma das linhas,
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
# lado 3, com números de 1 a 9:
# 8 3 4
# 1 5 9
# 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados
# mágicos com as características acima. Dica: produza todas as combinações
# possíveis e verifique a soma quando completar cada quadrado.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um valor: '))
def quadrado_magico(matriz):
    # Verifica se a soma das linhas são iguais
    if matriz[0][0] + matriz[0][1] + matriz[0][2] != matriz[1][0] + matriz[1][1] + matriz[1][2]:
        return False
    if matriz[1][0] + matriz[1][1] + matriz[1][2] != matriz[2][0] + matriz[2][1] + matriz[2][2]:
        return False
    if matriz[2][0] + matriz[2][1] + matriz[2][2] != matriz[0][0] + matriz[0][1] + matriz[0][2]:
        return False
    # Verifica se a soma das colunas são iguais
    if matriz[0][0] + matriz[1][0] + matriz[2][0] != matriz[0][1] + matriz[1][1] + matriz[2][1]:
        return False
    if matriz[0][1] + matriz[1][1] + matriz[2][1] != matriz[0][2] + matriz[1][2] + matriz[2][2]:
        return False
    if matriz[0][2] + matriz[1][2] + matriz[2][2] != matriz[0][0] + matriz[1][0] + matriz[2][0]:
        return False
    # Verifica se a soma das diagonais são iguais
    if matriz[0][0] + matriz[1][1] + matriz[2][2] != matriz[0][2] + matriz[1][1] + matriz[2][0]:
        return False
    return True



if (quadrado_magico(matriz)):
    print("Quadrado mágico encontrado")
else:
    print("Não foi possível encontrar um quadrado mágico")