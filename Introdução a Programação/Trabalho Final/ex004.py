'''4) De todos os alunos que reprovaram quantos foram por falta e quantos foram
por nota, e quantos foram por ambas as causas?'''

from funcoes import data_frame

dados = data_frame('alunos.csv')

alunos_reprovados_faltas = alunos_reprovados_nota = reprovados_ambas = 0

for i in dados:
    if i['faltas'] > 15:
        alunos_reprovados_faltas += 1

for i in dados:
    if i['faltas'] <=15 and i['nota_exame'] > 0 and i['nota_exame'] <= 5:
        alunos_reprovados_nota += 1

for i in dados:
    if i['faltas'] > 15 and i['nota_exame'] > 0 and i['nota_exame'] <= 5:
        reprovados_ambas += 1

print('---'*14)
print(f'Alunos reprovados por falta: \033[1m{alunos_reprovados_faltas}\033[0m')
print(f'Alunos reprovados por nota: \033[1m{alunos_reprovados_nota}\033[0m')  
print(f'Alunos reprovados por ambas as causas: \033[1m{reprovados_ambas}\033[0m')     
print('---'*14)
