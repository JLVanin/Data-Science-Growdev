# 6) Crie um programa que leia continuamente a altura e o sexo de uma lista de
# pessoas salvando todas as informações em listas, até que uma altura
# negativa seja fornecida. Ao final, sabendo que a média de altura para as
# mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,
# escreva as seguintes informações:
# a) quantas mulheres da lista estão acima da média nacional de altura
# para mulheres, e quantas estão abaixo;
# b) quantos homens da lista estão acima da média nacional de altura para
# homens, e quantos estão abaixo.

m_ac = []
m_ab = []
h_ac = []
h_ab = []

while True:
    altura = float(input('Altura: '))
    sexo = ' '
    if altura < 0:
        break
    while sexo not in 'MF':
        sexo = str(input('Sexo: M/F: ')).strip().upper()[0]
    if sexo == 'M' and altura > 1.73:
        h_ac.append(sexo)
    elif sexo == 'M' and altura < 1.73:
        h_ab.append(sexo)
    elif sexo == 'F' and altura > 1.60:
        m_ac.append(sexo)
    elif sexo == 'F' and altura < 1.60:
        m_ab.append(sexo)
        
print(f'Mulheres com altura acima da média nacional: {len(m_ac)}')
print(f'Mulheres com altura abaixo da média nacional: {len(m_ab)}')
print(f'Homens com altura acima da média nacional: {len(h_ac)}')
print(f'Homens com altura abaixo da média nacional: {len(h_ab)}')
