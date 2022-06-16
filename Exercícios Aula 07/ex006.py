# 6) Escreva um programa para solicitar ao usuário o raio r de uma esfera, e
# calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
# a seguinte fórmula para determinar o volume:

# v = (4.0 / 3.0) * π * r3

#Sendo π = 3.141592

def volume(r):
    
    return(4.0/3.0)*3.141592*(r**3)

r = float(input("Digite o raio:"))

print(volume(r))