# 6) Numa determinada escola, os critérios de aprovação são os seguintes:
# a) O aluno deve ter, no máximo, 25% de faltas;
# b) A nota final deve ser igual ou superior a 7,00.
# Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres,
# o número total de aulas e o número de faltas, mostrando ao final a situação
# do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por
# média”, considerando que a reprovação por faltas se sobrepõe a reprovação
# por nota.

media_1b = float(input('Média do 1° bimestre: '))
media_2b = float(input('Média do 2° bimestre: '))
media_3b = float(input('Médias do 3° bimestre: '))
media_4b = float(input('Média do 4° bimestre: '))
num_aulas = int(input('Número de aulas: '))
num_faltas = int(input('Número de faltas: '))
nota_final = (media_1b + media_2b + media_3b + media_4b) / 4 
faltas = (num_aulas * 25) / 100
print(f'Média final {nota_final:.2f}')
if num_faltas > faltas:
    print('Aluno REPROVADO por FALTAS!')
elif nota_final >= 7.0:
    print('Aluno APROVADO!')
else:
    print('Aluno REPROVADO por MÉDIA! ')