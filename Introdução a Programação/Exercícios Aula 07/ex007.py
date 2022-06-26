# 7) Faça uma função que recebe por parâmetro o tempo de duração da produção
# de uma peça em uma fábrica expressa em segundos e exibe esse tempo em
# horas, minutos e segundos.

t = int(input('Digite o tempo de produção em segundos: '))

def tempo_de_producao(t):
    h = t//3600
    m = (t - (h*3600))//60
    s = t - (h*3600) - (m*60)
    print(f'{h:02d}:{m:02d}:{s:02d}')

tempo_de_producao(t)