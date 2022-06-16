# 9) Escreva um programa que receba o nome de 10 pessoas e para cada
# pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
# a) Rio de Janeiro
# b) Bahia
# c) Minas Gerais
# Após, informar qual foi o destino mais visitado e qual o menos visitado.

rio_de_janeiro = bahia = minas_gerais = cont = 0
while (cont < 3):
    nome = str(input('Informe seu nome: '))
    destino = int(input('Informe o número correspondente à cidade visitada: \nRIO DE JANEIRO [1]\nBAHIA [2]\nMINAS GERAIS [3]\n'))
    if destino == 1:
        rio_de_janeiro += 1
    elif destino == 2:
        bahia += 1
    elif destino == 3:
        minas_gerais += 1
    cont += 1
if rio_de_janeiro > bahia and rio_de_janeiro > minas_gerais:
    print('\nRIO DE JANEIRO foi o lugar mais visitado')
elif bahia > rio_de_janeiro and bahia > minas_gerais:
    print('\nBAHIA foi o lugar mais visitado')
elif minas_gerais > rio_de_janeiro and minas_gerais > bahia:
    print('\nMINAS GERAIS foi o lugar mais visitado')
if rio_de_janeiro < bahia and rio_de_janeiro < minas_gerais:
    print('RIO DE JANEIRO foi o lugar menos visitado')
elif bahia < rio_de_janeiro and bahia < minas_gerais:
    print('BAHIA foi o lugar menos visitado')
elif minas_gerais < rio_de_janeiro and minas_gerais < bahia:
    print('MINAS GERAIS foi o lugar menos visitado')

# print(rio_de_janeiro)
# print(minas_gerais)
# print(bahia)