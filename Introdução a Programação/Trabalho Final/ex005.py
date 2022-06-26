''' 5) Qual a média de todas as notas (do 1º e 2º semestre) dos alunos do 2º ano?'''

from funcoes import data_frame

dados = data_frame('alunos.csv')

media_semestre_1 = []
media_semestre_2 = []

for i in dados:
    if i['ano'] == 2:
        media_semestre_1.append(i['nota_semestre_1'])
        media_semestre_2.append(i['nota_semestre_2'])

media_1 = sum(media_semestre_1) / len(media_semestre_1)    
media_2 = sum(media_semestre_2) / len(media_semestre_2)
media_total = (media_1 + media_2) / 2

print('\n\tMédia de todas as notas dos alunos do 2º ano')
print('---'*18)
print(f'Média do 1º semestre: \033[1m{media_1:.2f}\033[0m')
print(f'Média do 2º semestre: \033[1m{media_2:.2f}\033[0m')
print(f'Média do Total das notas: \033[1m{media_total:.2f}\033[0m')
print('---'*18)
