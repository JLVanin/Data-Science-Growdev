# 17) Receba 3 notas de um aluno e peça o peso (em porcentagem)
# respectivamente de cada nota, ao final exiba a nota final do mesmo.

n_1 = float(input('Digite a primeira nota: '))
n_2 = float(input('Digite a segunda nota: '))
n_3 = float(input('Digite a terceira nota: '))

total = n_1 + n_2 + n_3
pn_1 = n_1 / total * 100
pn_2 = n_2 / total * 100
pn_3 = n_3 / total * 100

print(f'A nota {n_1} ({pn_1:.2f} %)')
print(f'A nota {n_2} ({pn_2:.2f} %)')
print(f'A nota {n_3} ({pn_3:.2f} %)')

print(f'Total das notas {total:.2f} ({(pn_1+pn_2+pn_3):.2f} %)')