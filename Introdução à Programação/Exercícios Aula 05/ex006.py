# 6) Em uma eleição presidencial existem quatro candidatos. Os votos são
# informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
# a) 1,2 = voto para os respectivos candidatos
# b) 3 = voto nulo
# c) 4 = voto em branco;
# Elabore um programa que leia o código de votação de 5 candidatos. Calcule e escreva:
# a) total de votos para cada candidato
# b) total de votos nulos
# c) total de votos em branco

candidato_a = canditado_b = voto_nulo = voto_em_branco = cont = 0
while (cont < 5):
    voto = int(input(' Digite [1] para o candidato (A) \n Digite [2] para o candidato (B) \n Digite [3] para NULO \n Digite [4] para BRANCO \n'))
    if voto == 1:
        candidato_a += 1
    elif voto == 2:
        canditado_b += 1
    elif voto == 3:
        voto_nulo += 1
    elif voto == 4:
        voto_em_branco += 1
    cont += 1

print(f'Votos Candidato (A): {candidato_a}')
print(f'Votos Candidato (B): {canditado_b}')
print(f'Votos NULOS: {voto_nulo}')
print(f'Votos em BRANCO: {voto_em_branco}')



