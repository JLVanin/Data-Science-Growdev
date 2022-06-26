''' 7) Qual dos anos (1º, 2º ou 3º) mais procura a monitoria?. Crie um gráfico para
mostrar esses dados.'''

import matplotlib.pyplot as plt
from funcoes import data_frame, monitoria

dados = data_frame('alunos.csv')

alunos_m = {
    'ano_1': 0,
    'ano_2': 0,
    'ano_3': 0
}
monitoria(dados, 1, alunos_m, 'ano_1')
monitoria(dados, 2, alunos_m, 'ano_2')
monitoria(dados, 3, alunos_m, 'ano_3')

anos = ['1° Ano', '2° Ano', '3° Ano']
alunos = [alunos_m['ano_1'], alunos_m['ano_2'], alunos_m['ano_3']]

fig, ax = plt.subplots()
grafico = ax.bar(anos, alunos)
ax.set_ylabel('Quantidade Alunos')
ax.set_title('Procura Monitoria.')
ax.bar_label(grafico, fmt="%.01f", size=11, label_type="edge")
plt.ylim(0, 1000)
plt.show()
