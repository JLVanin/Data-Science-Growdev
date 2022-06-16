# 8) Crie um algoritmo para uma empresa de transportes que, a partir do peso de
# uma encomenda fornecida pelo usuário, calcule o preço da remessa
# conforme a seguinte tabela:

# 500 gramas ou menos R$ 1,10
# Mais de 500 gramas, mas não mais que 2 quilos R$ 2,20
# Mais de 2 quilos, mas não mais de 10 quilos R$ 3,70
# Mais de 10 quilos R$ 5,00 mais R$ 3,80/kg pelo peso que ultrapassar 10 Kg

peso = float(input('Digite o peso da encomenda: '))
if peso <= 500/1000:
    preço = ('1.10')
    print(f'O preço da remessa é R$ {preço}')
elif peso > 500/1000 and peso <= 2:
    preço = ('2.20')
    print(f'O preço da remessa é RS {preço}')
elif peso > 2 and peso <= 10:
    preço = ('3.70')
    print(f'O preço da remessa é RS {preço}')
elif peso > 10:
    preço = ((peso - 10) * 3.80) + 5
    print(f'O preço da remessa é RS {preço:.2f}')