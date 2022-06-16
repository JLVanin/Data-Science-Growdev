# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercício.
# 8) A opção de débito é mais utilizada entre homens ou mulheres?

from dados import abr_dados, dicionario

dados = abr_dados('compras.csv')
info = dicionario(dados)

mulheres = 0
homens = 0

for i in info:
    if i['sexo'] == 'F' and i['pagamento'] == 'debito':
        mulheres += 1
    elif i['sexo'] == 'M' and i['pagamento'] == 'debito':
        homens += 1
if mulheres > homens:
    print('A opção débito é mais utiliada entre as MULHERES.')
else:
    print('A opção débito é mais utilizada entre os HOMENS')
