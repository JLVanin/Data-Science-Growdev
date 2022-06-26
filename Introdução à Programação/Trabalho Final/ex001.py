'''1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?'''

from funcoes import data_frame

dados = data_frame('alunos.csv')

dic_escola = {}

for i in dados:
    escola = i['escola']
    if escola in dic_escola:            
        dic_escola[escola] = dic_escola[escola] + 1
    else:            
        dic_escola[escola] = 1

lista_escola = sorted(dic_escola.items())

alunos = 0
nome_escola = ''
for i in lista_escola:
    if i[1] > alunos:
        alunos = i[1]
        nome_escola = i[0]

print('---'*16)
for escola in lista_escola:
    print(f'Escola: {escola[0]:^16}  Alunos estudando: \033[1m{escola[1]}\033[0m')
print('---'*16)

print(f'Escola com mais alunos: {nome_escola} - Alunos estudando: \033[1m{alunos}\033[0m')
print('---'*22)

