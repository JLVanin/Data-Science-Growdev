# 24) Escreva um algoritmo que leia as 3 notas de um aluno e calcule a média final
# deste aluno. Considerar que a média é ponderada e que o peso das notas é:
# 20%, 30% e 50%, respectivamente.

nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
nota_3 = float(input('Digite a nota 3: '))

peso_1 =  20 / 100
peso_2 =  30 / 100
peso_3 =  50 / 100

s_peso = peso_1 + peso_2 + peso_3

media = (nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3) / s_peso

print(media)

