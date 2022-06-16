# 5) Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um
# produto.
# a) Calcular e escrever o total
# total = quantidade adquirida * preço unitário
# b) Leia o desconto sobre a compra e calcule.
# total a pagar = total - desconto
# i) Sabendo-se que:
# (1) Se quantidade <= 5 o desconto será de 2%.
# (2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
# (3) Se quantidade > 10 o desconto será de 5%.

preco_unitario = float(input('Digite o preço unitário do produto R$: '))
qnt_adquirida = int(input('Quantidade: '))
total = qnt_adquirida * preco_unitario
print(f'Total R$ {total}')
if qnt_adquirida <= 5:
    print(f'Total com desconto de 2% \n Total R$ {total - total * 2 / 100}')
elif qnt_adquirida > 5 and qnt_adquirida <= 10:
    print(f'Total com desconto de 3% \n Total R$ {total - total * 3 / 100}')
elif qnt_adquirida > 10:
    print(f'Total com desconto de 5% \n Total R$ {total - total * 5 / 100}')



