# 2) Exiba um gráfico que mostre a quantidade total de compras
# agrupadas por anos.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('compras.csv')

df.groupby('ano').size().plot(kind = 'bar')

plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.title('Quantidade de compras por ano.')
plt.xticks(rotation=45)

plt.show()