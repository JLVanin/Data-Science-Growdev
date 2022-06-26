# 3) Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string em um formato por extenso. Opcionalmente, valide a data
# e retorne NULL caso a data seja inválida.

data = str(input('Informe a data no formato DD/MM/AAAA: '))
def data_extenso(data):
    dia, mes, ano = data.split("/")
    import calendar
    mes = calendar.month_name[int(mes)]
    
    return "{} de {} de {}".format(dia, mes, ano)
print(data_extenso(data))