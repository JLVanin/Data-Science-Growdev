# 9) Escreva um programa que peça ao usuário para fornecer um dia, mês e o
# ano arbitrários e determine se esses dados correspondem a uma data válida.
# Não deixe de considerar que existem meses com 30 e 31 dias, e que
# fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
# Considere que um ano é bissexto quando for divisível por 4.

dia = int(input('Informe o Dia: '))
mes = int(input('Informe o Mês: '))
ano = int(input('Informe o Ano: '))

data = False
if( mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if(dia <= 31):
        data = True
elif( mes ==4 or mes == 6 or mes == 9 or mes == 11):
     if(dia <= 30):
        data= True
elif mes == 2:
     if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        if(dia <= 29):
         data = True
     elif(dia <= 28):
          data = True

if(data):
     print('Data válida')
else:
    print('Data inválida')

