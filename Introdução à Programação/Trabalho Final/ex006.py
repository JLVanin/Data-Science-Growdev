'''6) As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um
gráfico para mostrar isso.'''

import matplotlib.pyplot as plt
from funcoes import data_frame, reprovacoes

dados = data_frame('alunos.csv')

alunos_r = {
    'ano_1': 0,
    'ano_2': 0,
    'ano_3': 0
}
reprovacoes(dados, 1, alunos_r, 'ano_1')
reprovacoes(dados, 2, alunos_r, 'ano_2')
reprovacoes(dados, 3, alunos_r, 'ano_3')

anos = ['1° Ano', '2° Ano', '3° Ano']
alunos = [alunos_r['ano_1'], alunos_r['ano_2'], alunos_r['ano_3']]
    
fig, ax = plt.subplots()
grafico = ax.bar(anos, alunos)
ax.set_ylabel('Quantidade Alunos')
ax.set_title('Gráfico de Reprovações / Ano.')
ax.bar_label(grafico, fmt="%.01f", size=11, label_type="edge")
plt.ylim(0, 1400)
plt.show()
