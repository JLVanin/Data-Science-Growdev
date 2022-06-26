# 3) Modifique o programa anterior para que utilize apenas uma lista e em cada
# posição da lista armazene um dicionário com o nome e a média.

alunos = []
for i in range(3):
    nome = input('Informe o nome: ')
    nota_1 = float(input('Informe a nota 1: '))
    nota_2 = float(input('Informe a nota 2: '))
    media = (nota_1 + nota_2) / 2 

    aluno = {'nome': nome, 'media': media}
    alunos.append(aluno)
for i in range(3):
    aluno = alunos[i]
    if aluno['media'] >= 7:
        print(f'Nome:{aluno["nome"]}\nMédia:{aluno["media"]}')
