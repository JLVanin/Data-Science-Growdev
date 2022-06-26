# 4) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$2000,00.
# Escreva um programa que receba as informações necessárias de 5 pessoas
# conforme a descrição e responda às questões a, b, c e d anteriores.

media_salario = media_filhos = cont = cont_p = 0
for pessoas in range(5):
    salario = float(input('Informe o sálario: '))
    num_filhos = int(input('Informe o número de filhos: '))
    cont += 1   
    media_salario += salario / 5
    media_filhos += num_filhos / 5
    if cont == 1:
        maior = salario
    else:
        if salario > maior:
            maior = salario
    if salario < 2000:
        cont_p += 1
        prct_pessoas = cont_p * 100 / 5
      
print(f'Média de sálario {media_salario:.2f}')
print(f'Média de filhos {media_filhos:.0f}')
print(f'Maior sálario {maior}')
print(f'Percentual de pessoas com sálario de até R$ 2000 ({prct_pessoas}) %')