# Desafio
# Crie um algoritmo que funcione como um jogo de loteria, conforme as seguintes regras:
# a) O algoritmo deve gerar três números aleatórios entre 0 e 9;
# b) O usuário deve fornecer um palpite com três números, também entre 0 e 9;
# c) Cada um dos palpites do usuário deve ser comparado com os números
# aleatórios, de acordo com a tabela abaixo:
# Números Correspondentes Número de pontos
# Nenhum número coincidente 0
# Acertar um número 10
# Acertar dois números 100
# Acertar os três números, mas não na mesma ordem em que foram gerados 1000
# Acertar três números na mesma ordem que os números aleatórios 1.000.000

from random import randint
print('Informe três números entre 0 e 9')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digiteo terceiro número: '))

na1 = randint(0,9)
na2 = randint(0,9)
na3 = randint(0,9)

if n1 == na1 and n2 == na2 and n3 == na3:
    print("Acertou todos os números em ordem")
elif (n1 + n2 + n3) - (na1 + na2 + na3) == 0 and (n1 != na1 or n2 != na2 or n3 != na3):
    print("Acertou todos os números mas não em ordem")
else:
    n1_hit = n1 == na1 or n1 == na2 or n1 == na3
    n2_hit = n2 == na1 or n2 == na2 or n2 == na3
    n3_hit = n3 == na1 or n3 == na2 or n3 == na3

    acertos = 0

    if n1_hit:
        acertos += 1
    if n2_hit:
        acertos += 1
    if n3_hit:
        acertos += 1

    print(f"Acertos: {acertos}")

