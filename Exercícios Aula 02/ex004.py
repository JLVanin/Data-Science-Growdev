#4) Escreva um programa que receba 3 números, faça a soma dos dois primeiros e depois divida o 
#resultado pelo 3o número. Após, exiba o resultado na tela.

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: ')) 
div = float(input('Número para realizar a divisão: '))
res = (num1 + num2) / div
print('O resultado é {:.2f}' .format(res))
