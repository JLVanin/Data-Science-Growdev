# 3) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
# escrever o custo final ao consumidor.

custo_fbr = float(input('Digite o custo de fábrica do veículo: '))

lucro_dist = custo_fbr * 28 / 100

imposto = custo_fbr * 45 / 100

custo_cons = custo_fbr + lucro_dist + imposto

print(f'Custo do veículo incluindo impostos e distribuição \nR$ {custo_cons}')
