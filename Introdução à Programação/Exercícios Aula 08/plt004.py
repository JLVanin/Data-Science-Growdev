# 4) Exiba o valor total de compras por modo de pagamento.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('compras.csv')

df.groupby('pagamento').size().plot(kind = 'bar')

plt.xlabel('Método de Pagamento')
plt.ylabel('Quantidade')
plt.title('Quantidade de compras por método de pagamento.')
plt.xticks(rotation=0)

plt.show()