# A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 e
# quindim a R$1.50. Crie um algoritmo que pergunte quantas unidades de cada
# produto foram vendidas pelo Paulo num dia e calcule o total faturado.

pao_frc = int(input('Digite a quantidade vendida de pão francês: '))
pao_dc = int(input('Digite a quantidade vendida de pão doce: '))
qnd = int(input('Digite a quantidade vendida de quindim: '))
pao_frances = 0.75
pao_doce = 0.85
quindim = 1.50
total = (pao_frances * pao_frc) + (pao_doce * pao_dc) + (quindim * qnd)
print('Total da venda foi R$ {}'.format(total))
