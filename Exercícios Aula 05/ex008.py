# 8) Escreva um programa que leia a idade e salário de 10 pessoas. Informe em seguida:
# a) Qual é a média de idade entre as pessoas?
# b) Quantas pessoas há por faixa etária, considerando:
# i) jovens < 18
# ii) 18 <= adultos < 60
# iii) idosos >= 60
# c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.

media_idade = jovens = adultos = idosos = cont = salario_j = salario_a = salario_i = 0
for i in range(10):
    idade = int(input('Informe sua idade: '))
    salario = float(input('Informe seu salário: '))
    media_idade += idade / 10
    cont += 1
    if idade < 18:
        jovens += 1    
        salario_j += salario
    elif idade >= 18 and idade < 60:
        adultos += 1
        salario_a += salario
    elif idade >= 60:
        idosos += 1
        salario_i += salario

if salario_j > salario_a and salario_a < salario_i and salario_i < salario_a:
    print('\nFaixa etária que acumula o maior salário: JOVENS')
elif salario_a > salario_j and salario_j < salario_i and salario_i < salario_j:
    print('\nFaixa etária que acumula o maior salário: ADULTOS')
else:
    salario_i > salario_a and salario_a < salario_j and salario_j < salario_a
    print('\nFaixa etária que acumula o maior salário: IDOSOS')

print(f'A média de idade: {media_idade:.0f} anos')
print(f'JOVENS: {jovens}')
print(f'ADULTOS: {adultos}')
print(f'IDOSOS: {idosos}')
# print(salario_j)  
# print(salario_a)
# print(salario_i)
