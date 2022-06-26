'''2) Quantos alunos do 1º ano foram aprovados sem exame?'''

from funcoes import data_frame

dados = data_frame('alunos.csv')

alunos_aprovados = 0

for i in dados:
    if i['ano']== 1 and i['nota_exame']== 0 and i['faltas'] <= 15:
        alunos_aprovados += 1
        
print('---'*14)
print(f'Alunos do 1º ano aprovados sem exame: \033[1m{alunos_aprovados}\033[0m')
print('---'*14)
