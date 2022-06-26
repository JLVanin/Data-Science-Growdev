# 8) Um carpinteiro esculpe placas personalizadas para estabelecimentos
# comerciais e deseja um programa que faça orçamentos das placas que
# produz, considerando as seguintes informações:
# a) O valor mínimo de qualquer placa é de R$ 300,00;
# b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus
# não possuem nenhum custo extra;
# c) Frases com até 12 caracteres estão incluídas no valor mínimo; para
# frases maiores, são cobrados R$ 15,00 por caractere;
# d) Para placas com dizeres brancos ou pretos não se cobra adicional,
# mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.
# Baseado nessas informações, construa um algoritmo que leia o número de
# um orçamento, o nome do cliente, tipo de madeira (angelim ou pinus),
# número de caracteres da mensagem e a cor dos caracteres (branco, preto ou
# dourado). Ao final, imprima todos os dados de entrada e o preço da placa
# orçada.

num_orcamento = int(input('Digite o número do orçamento: '))
nome_cliente = str(input('Informe o nome do cliente: '))
print('Escolha o tipo de madeira... \n Para ANGELIM digite 1 \n Para PINUS digite 2')
madeira = int(input('Digite um número para escolher o tipo de madeira: '))
num_caracteres = int(input('Informe o número de caracteres da mensagem: '))
print('Escolha a cor dos caracteres... \n Para PRETO digite 1 \n Para BRANCO digite 2 \n Para DOURADO digite 3')
cor_caracteres = int(input('Digite um número para escolher a cor dos caracteres: '))
madeira_1 = 'ANGELIN'
madeira_2 = 'PINUS'
cor_1 = 'PRETO'
cor_2 = 'BRANCO'
cor_3 = 'DOURADO'
if madeira == 1 and num_caracteres > 12 and cor_caracteres == 1:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_1} \n Valor da placa R$ {300 + 150 + ((num_caracteres - 12) * 15)}')
elif madeira == 1 and num_caracteres > 12 and cor_caracteres == 2:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_2} \n Valor da placa R$ {300 + 150 + ((num_caracteres - 12) * 15)}')
elif madeira == 1 and num_caracteres > 12 and cor_caracteres == 3:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_3} \n Valor da placa R$ {300 + 150 + ((num_caracteres - 12) * 15) + 60}')
elif madeira == 1 and num_caracteres <= 12 and cor_caracteres == 1:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_1} \n Valor da placa R$ {300 + 150}')
elif madeira == 1 and num_caracteres <= 12 and cor_caracteres == 2:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_2} \n Valor da placa R$ {300 + 150}')
elif madeira == 1 and num_caracteres <= 12 and cor_caracteres == 3:
    print(f'Madeira: {madeira_1} \n Frase com {num_caracteres} caracteres na cor {cor_3} \n Valor da placa R$ {300 + 150 + 60}')
elif madeira == 2 and num_caracteres > 12 and cor_caracteres == 1:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_1} \n Valor da placa R$ {300 + ((num_caracteres - 12) * 15)}')
elif madeira == 2 and num_caracteres > 12 and cor_caracteres == 2:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_2} \n Valor da placa R$ {300 + ((num_caracteres - 12) * 15)}')
elif madeira == 2 and num_caracteres > 12 and cor_caracteres == 3:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_3} \n Valor da placa R$ {300 + ((num_caracteres - 12) * 15) + 60}')
elif madeira == 2 and num_caracteres <= 12 and cor_caracteres == 1:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_1} \n Valor da placa R$ {300}')
elif madeira == 2 and num_caracteres <= 12 and cor_caracteres == 2:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_2} \n Valor da placa R$ {300}')
elif madeira == 2 and num_caracteres <= 12 and cor_caracteres == 3:
    print(f'Madeira: {madeira_2} \n Frase com {num_caracteres} caracteres na cor {cor_3} \n Valor da placa R$ {300 + 60}')
    