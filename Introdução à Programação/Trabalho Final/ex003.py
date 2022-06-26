''' 3) Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria?'''

from funcoes import data_frame

dados = data_frame('alunos.csv')

alunos_reprovados = {
    'monitoria': 0,
    'alunos': 0
}

for i in dados:
    if i['ano']== 3 and i['faltas'] > 15:
        alunos_reprovados['alunos'] +=1
        if i['monitoria'] == 'True':
            alunos_reprovados['monitoria'] += 1

for i in dados:
    if i['ano'] == 3 and i['faltas'] <= 15 and i['nota_exame'] >0 and i['nota_exame'] <=5:
        alunos_reprovados['alunos'] +=1
        if i['monitoria'] == 'True':
            alunos_reprovados['monitoria'] += 1

print('---'*16)
print(f'Alunos do 3º ano reprovados: \033[1m{alunos_reprovados["alunos"]}\033[0m')
print(f'Alunos reprovados que procuraram monitoria: \033[1m{alunos_reprovados["monitoria"]}\033[0m')
print('---'*16)
