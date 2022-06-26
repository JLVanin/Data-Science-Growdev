import csv

def data_frame(arquivo):
    f = open(arquivo, encoding= 'utf_8')
    dados = csv.reader(f, delimiter= ',')               #Abre o arquivo 'csv'
    dados = list(dados)
    info = dicionario(dados)
    return info

def dicionario(dados):
    registros = len(dados)
    info = []
    for i in range(1, registros):                       
        info.append(
            {                                           #Transforma o arquivo em dicionário    
                'nome': dados[i][0],
                'ano': int(dados[i][1]),
                'escola': dados[i][2],                      
                'nota_semestre_1': float(dados[i][3]),
                'nota_semestre_2': float(dados[i][4]),
                'faltas': int(dados[i][5]),
                'nota_exame': float(dados[i][6]),
                'monitoria': (dados[i][7]),    
                'media': (float(dados[i][3]) + float(dados[i][4])) / 2             
            }
        )
    return info

def reprovacoes(dados, ano, lista, alunos):              #Função calculo de reprovações
    for i in dados:
        if i['ano'] == ano:
            if i['faltas'] > 15 or i['faltas'] <= 15 and i['nota_exame'] >0 and i['nota_exame'] <=5:
                lista[alunos] +=1

def monitoria(dados, ano, lista, alunos):
    for i in dados:                                       #Função calculo monitoria 
        if i['ano'] == ano and i['monitoria'] == 'True':
            lista[alunos] += 1
