# ● Modificação 2 – Paulo tem o hábito de guardar 10% de tudo que fatura
# numa caderneta de poupança, para eventuais necessidades no futuro.
# Sabendo disso, modifique o algoritmo que você criou para que ele
# informe quanto do total faturado deve ser poupado.

pao_frc = int(input('Digite a quantidade vendida de pão francês: '))
pao_dc = int(input('Digite a quantidade vendida de pão doce: '))
qnd = int(input('Digite a quantidade vendida de quindim: '))
pao_frances = 0.75
pao_doce = 0.85
quindim = 1.50

total = (pao_frances * pao_frc) + (pao_doce * pao_dc) + (quindim * qnd)

poupar = (total * 10 / 100)

print('Total da venda foi R$ {} você deve guardar R$ {}'.format(total, poupar))
