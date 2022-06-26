# 2) Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a
# média das notas e armazene nome e média cada uma em uma lista, ao final
# imprima o nome e o número de alunos com média maior ou igual a 7.0.

nomes = []
medias = []
for i in range(3):
    nome = input('Informe o nome: ')
    nota_1 = float(input('Informe a nota 1: '))
    nota_2 = float(input('Informe a nota 2: '))
    media = (nota_1 + nota_2) / 2 

    nomes.append(nome)
    medias.append(media)
for i in range(3):
    if medias[i] >= 7:
        print(f'Nome:{nomes[i]}\nMédia:{medias[i]}')
