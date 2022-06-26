# 2) Escreva um algoritmo que leia 3 valores e exiba qual o maior valor entre eles.

valor_1 = int(input('Informe o primeiro valor: '))
valor_2 = int(input('Informe o segundo valor: '))
valor_3 = int(input('informe o terceiro valor: '))

lista = [valor_1, valor_2, valor_3]

valor_maior = max(lista)
print(f'O maior valor é {valor_maior}')
