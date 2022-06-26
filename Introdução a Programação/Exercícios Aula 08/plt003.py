# 3) Mostre a quantidade de homens e mulheres na base de dados.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('compras.csv')

df.groupby('sexo').size().plot(kind = 'bar')

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.title('Quantidade de Homens e Mulheres.')
plt.xticks(rotation=0)

plt.show()