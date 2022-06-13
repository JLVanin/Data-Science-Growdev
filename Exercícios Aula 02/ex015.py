# 15) Um cliente de uma loja está comprando cinco produtos. Crie um programa
# que solicite o preço de cada um desses produtos e, em seguida, exiba o
# subtotal da venda, o valor do imposto e o valor total (subtotal da venda mais
# o valor do imposto). Suponha que a alíquota do imposto seja de 6% sobre o
# subtotal da venda.

p_1 = float(input('Valor produto 1: '))
p_2 = float(input('Valor produto 2: '))
p_3 = float(input('Valor produto 3: '))
p_4 = float(input('Valor produto 4: '))
p_5 = float(input('Valor produto 5: '))

s_total = p_1 + p_2 + p_3 + p_4 + p_5
print(f'Subtotal da venda R$: {s_total:.2f}')
imposto = (s_total * 6 / 100)
print(f'Valor do imposto R$: {imposto:.2f}')
total = s_total + imposto
print(f'Total R$: {total:.2f}')
