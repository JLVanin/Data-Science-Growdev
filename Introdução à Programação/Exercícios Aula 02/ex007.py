# 7) Escreva um algoritmo que leia a idade de uma pessoa expressa em anos,
# meses e dias e mostre-a expressa apenas em dias. Considere ano = 365
# dias, mês = 31 dias.

idade_anos = int(input('Digite a idade em anos: '))
idade_meses = int(input('Digite a idade em meses: '))
idade_dias = int(input('Digite a idade em dias: '))
ano = 365 
meses = 31 
idade_em_dias = (idade_anos * 365) + (idade_meses * 31) + idade_dias
print('Sua idade em dias é : {}'.format(idade_em_dias))
