# ● Modificação 3 – Modifique o algoritmo para que, antes de calcular
# quanto deve ser guardado na poupança, ele desconte o valor do
# imposto devido, que é de 5%.pao_frc = int(input('Digite a quantidade vendida de pão francês: '))

pao_dc = int(input('Digite a quantidade vendida de pão doce: '))
qnd = int(input('Digite a quantidade vendida de quindim: '))
pao_frances = 0.75
pao_doce = 0.85
quindim = 1.50

total = (pao_frances * pao_frances) + (pao_doce * pao_dc) + (quindim * qnd)

imposto = (total * 5 / 100)
total = total - imposto
poupar = (total * 10 / 100)
total_g = (total - poupar)
print(f'Imposto à pagar R$ {imposto:.2f}')
print(f'Total da venda R$ {total:.2f}') 
print(f'Você deve guardar R$ {poupar:.2f}')
print(f'Total após descontos: R$ {total_g:.2f}')

