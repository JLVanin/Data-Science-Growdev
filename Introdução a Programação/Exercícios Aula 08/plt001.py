# Plotagem de Gráficos
# 1) Exiba um gráfico que mostre a quantidade total de gastos com
# compras agrupadas por anos.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('compras.csv')

coluna_ano = df.groupby('ano')

plt.figure()
coluna_ano.sum()['compra'].plot(kind='bar')

plt.title('Quantidade de gasto em compras por ano')
plt.show()