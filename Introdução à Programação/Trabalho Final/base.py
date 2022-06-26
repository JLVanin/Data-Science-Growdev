
from funcoes import data_frame

dados = data_frame('alunos.csv')

alunos = 0
for i in dados:
    if i['ano'] == 3:
        alunos += 1
        
alunos_aprovados_sem_exame = 0
for i in dados:
    if i['ano'] == 3 and i['faltas'] <= 15 and i['nota_exame'] == 0:
        alunos_aprovados_sem_exame += 1

alunos_aprovados_com_exame = 0   
for i in dados:
    if i['ano'] == 3 and i['faltas'] <= 15 and i['nota_exame'] > 0 and i['nota_exame'] > 5:
        alunos_aprovados_com_exame +=1

alunos_reprovados_falta =0
monitoriaa = 0
for i in dados:
    if i['ano']== 3 and i['faltas'] > 15:
        alunos_reprovados_falta +=1
        if i['monitoria'] == 'True':
            monitoriaa += 1

alunos_reprovados_nota =0
monitoria= 0
for i in dados:
    if i['ano'] == 3 and i['faltas'] <= 15 and i['nota_exame'] >0 and i['nota_exame'] <=5:
        alunos_reprovados_nota +=1
        if i['monitoria'] == 'True':
            monitoria +=1

print(alunos)
print(alunos_aprovados_sem_exame)
print(alunos_aprovados_com_exame)
print(alunos_reprovados_falta)
print(alunos_reprovados_nota)
