# 31) Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se que
# existe um desconto acumulado de 0,5% do valor total da compra a cada
# centena comprada deste produto. Escreva um algoritmo que receba a
# quantidade comprada desse produto e informe.
# a) O valor total da compra (sem o desconto)
# b) A quantidade de centenas compradas desse produto
# c) O desconto em R$.
# d) O valor total da compra (com desconto)

produto_valor = 5.4

print("Informe a quantidade comprada: ")
produto_quantidade = int(input())

total_sem_desconto = produto_quantidade * produto_valor

centenas_compradas = produto_quantidade / 100
centenas_compradas -= centenas_compradas % 1

valor_centena = produto_valor * 100

desconto_centena = valor_centena * 0.5 / 100

desconto_total = centenas_compradas * desconto_centena

total_com_desconto = total_sem_desconto - desconto_total

print("Total sem desconto: {}".format(total_sem_desconto))

print("Centenas compradas: {}".format(centenas_compradas))

print("Desconto: {}".format(desconto_total))

print("Total com desconto: {}".format(total_com_desconto))