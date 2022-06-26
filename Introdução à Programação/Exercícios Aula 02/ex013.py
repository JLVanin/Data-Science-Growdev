#13) Escreva um programa que receba dois valores para as variáveis A e B e
# efetue a troca dos valores de forma que a variável A passe a possuir o valor
# da variável B e a variável B passe a possuir o valor da variável A. Apresentar
# os valores após a efetivação do processamento da troca.

var_a = (input('Digite um valor para a variável A: '))
var_b = (input('Digite um valor para a variável B: '))

var_a, var_b = var_b, var_a

print(f'A = {var_a}')
print(f'B = {var_b}')