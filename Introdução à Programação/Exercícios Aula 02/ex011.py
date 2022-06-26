#11) Sabendo que o lucro anual de uma empresa é, tipicamente, 23% do total de
#vendas, crie um programa que solicite ao usuário que entre com o valor
#projetado do total de vendas e, em seguida, calcule e exiba o lucro que deve
#ser obtido com esse valor.

valor_projetado = float(input('Digite o valor projetado do total das vendas: '))

lucro = (valor_projetado * 23 / 100)

print(f'Com o total de vendas de R$ {valor_projetado} \nO lucro estimado é de R$ {lucro}')


