# 5) Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
# metro e cresce 3 centímetros por ano. Construa um programa que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que Chico.

alt_chico = 1.50
alt_ze = 1.10
anos = 0
print('Chico tem 1,50 metros e cresce 2 centímetros por ano')
print('Zé tem 1,10 metros e cresce 3 centímetros por ano')

while(alt_chico > alt_ze):
    alt_chico += 0.02
    alt_ze += 0.03
    anos += 1 
print(f'Serão necessários {anos} anos para que Zé seja maior que Chico')

