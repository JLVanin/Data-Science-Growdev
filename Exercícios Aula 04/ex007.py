# 7) Após construir o algoritmo anterior, crie mais duas versões dele para prever
# as seguintes situações:
# a) Um aluno pode ficar em recuperação se possuir frequência suficiente
# (superior a 75%) e média superior a 5 mas inferior a 7;
# b) Caso um aluno reprove por média e faltas, sua situação deve ser
# “Reprovado por Média e Faltas” (ao invés de simplesmente
# “Reprovado por Faltas” como antes).

media_1b = float(input('Média do 1° bimestre: '))
media_2b = float(input('Média do 2° bimestre: '))
media_3b = float(input('Médias do 3° bimestre: '))
media_4b = float(input('Média do 4° bimestre: '))
num_aulas = int(input('Número de aulas: '))
num_faltas = int(input('Número de faltas: '))
nota_final = (media_1b + media_2b + media_3b + media_4b) / 4 
faltas = (num_aulas * 25) / 100
print(f'Média final {nota_final:.2f}')

if num_faltas > faltas and nota_final < 5.0:
    print('Aluno REPROVADO por MÉDIA e FALTAS!')
elif num_faltas > faltas:
    print('Aluno REPROVADO por FALTAS!')
elif nota_final < 5.0:
    print('Aluno REPROVADO!')
elif nota_final >= 7.0:
    print('Aluno APROVADO!')
elif nota_final >= 5.0 and nota_final < 7.0:
    print('Aluno em RECUPERAÇÃO! ')
