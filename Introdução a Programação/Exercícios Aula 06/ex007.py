# 7) Crie um programa que calcule a folha de pagamento de uma empresa, conforme as instruções a seguir:
# a) O usuário pode inserir continuamente os nomes dos empregados até que escolha a opção de finalizar o informe de dados;
# b) Após informar o nome de cada empregado, o usuário deverá informar o valor do salário da hora trabalhada desse empregado e quantas horas ele trabalhou;
# c) O programa deve calcular o salário bruto de cada empregado, a percentagem de imposto retido na fonte (com base na tabela abaixo),
# o valor do imposto retido na fonte e o salário líquido (pagamento bruto menos imposto retido na fonte);
# d) Depois que o usuário inserir os dados do último empregado, o programa deve exibir o salário bruto, salário líquido, percentual de imposto e valor do imposto para cada funcionário;
# e) Por último, o programa deve exibir a soma de todas as horas trabalhadas, o total da folha de pagamento bruta, o total de imposto e a folha de pagamento líquida total.
# Percentuais de imposto
# Salário bruto Percentual
# Até R$ 2.999,99 10%
# Entre R$ 3.000,00 e R$ 5.499,99 13%
# Entre R$ 5.500,00 e R$ 7.999,99 16%
# Acima de R$ 8.000,00 20%

nome_funcionarios = []
valor_hora = []
hora_trabalhada = []
salario_bruto = []
imposto = []
salario_liquido = []

while True:
    nome_funcionarios.append(input('Nome do funcionário: '))
    valor_hora.append(float(input('Valor da hora trabalhada: ')))
    hora_trabalhada.append(int(input('Quantas horas trabalhadas: ')))
    
    if input('Deseja inserir outro funcionário? s/n ') == 'n':
        break

    for i in range(len(nome_funcionarios)):
        salario_bruto.append(valor_hora[i] * hora_trabalhada[i])

        if salario_bruto[i] <= 3000:
            aliquota = 10
            imposto = salario_bruto[i] * 10 / 100
            salario_liquido = salario_bruto[i] - imposto
        elif salario_bruto[i] >= 3000 and salario_bruto[i] < 5500:
            aliquota = 13
            imposto = salario_bruto[i] * 13 / 100
            salario_liquido[i] = salario_bruto[i] - imposto
        elif salario_bruto[i] >= 5500 and salario_bruto[i] < 8000:
            aliquota = 16
            imposto = salario_bruto[i] * 16 / 100
            salario_liquido[i] = salario_bruto[i] - imposto
        elif salario_bruto[i] > 8000:
            aliquota = 20
            imposto = salario_bruto[i] * 20 / 100
            salario_liquido[i] = salario_bruto[i] - imposto

print(f'NOME: {nome_funcionarios}\nSALÁRIO BRUTO: R$ {salario_bruto:.2f}\nPERCENTUAL DE IMPOSTO: {aliquota}%\nIMPOSTO RETIDO: R$ {imposto:.2f}\nSALÁRIO LÍQUIDO: R$ {salario_liquido:.2f}')
