# 11) Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
# programa que calcule e escreva o número de anos necessários para que a
# população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

pais_a = 80000
pais_b = 200000
anos = 0
while (pais_b > pais_a):
    pais_b += 2400
    pais_a += 3000
    anos += 1
print(f'São necessários {anos} anos para que o país A iguale a população do país B')