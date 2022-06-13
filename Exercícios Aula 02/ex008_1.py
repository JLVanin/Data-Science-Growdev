# ● Modificação 1 – Modifique o algoritmo para que, ao invés de
# considerar o preço dos produtos como fixos, o usuário possa informar
# o preço deles.

pao_frances = float(input('Digite o valor do pão francês: '))
pao_doce = float(input('Digite o valor do pão doce: '))
quindim = float(input('Digite o valor do quindim: '))

pao_frc = int(input('Digite a quantidade vendida de pão francês: '))
pao_dc = int(input('Digite a quantidade vendida de pão doce: '))
qnd = int(input('Digite a quantidade vendida de quindim: '))

total = (pao_frances * pao_frc) + (pao_doce * pao_dc) + (quindim * qnd)
print('Total da venda foi R$ {:.2f}'.format(total))