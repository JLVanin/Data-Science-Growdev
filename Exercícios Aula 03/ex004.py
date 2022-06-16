# 4) O programa de fidelidade de uma determinada livraria premia seus clientes
# de acordo com o número de livros comprados a cada mês. Os pontos são
# atribuídos da seguinte forma:
# a) Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# b) Se um cliente comprar um livro, ele ganhará 5 pontos.
# c) Se um cliente comprar dois livros, ele ganhará 15 pontos.
# d) Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# e) Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
# Crie um algoritmo que leia o número de livros comprados por um cliente e
# exiba o número de pontos correspondentes.

livros_cmpr = int(input('Informe a quantidade de livros comprados: '))

if livros_cmpr == 0:
    print('0 pontos!')
elif livros_cmpr == 1:
    print('Você ganhou 5 pontos no programa de fidelidade!')
elif livros_cmpr == 2:
    print('Você ganhou 15 pontos no programa de fidelidade!')
elif livros_cmpr == 3:
    print('Você ganhou 30 pontos no programa de fidelidade!')
else:
    print('Você ganhou 60 pontos no programa de fidelidade!')
