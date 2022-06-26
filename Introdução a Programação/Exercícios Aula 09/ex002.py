# 2) Crie uma classe que modele um retângulo:
# a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
# Altura, a escolher)
# b) Métodos:
#   i) Mudar valor dos lados
#   ii) Retornar valor dos lados
#   iii) Calcular Área
#   iv) Calcular Perímetro;
# c) Crie um programa que utilize esta classe. Ele deve pedir
# ao usuário que informe as medidas de um local. Depois,
# deve-se criar um objeto com as medidas e calcular a
# quantidade (em m²) de pisos (1 x 1 m²) e de rodapés
# necessários para o local.
from Classes import Retangulo

base = int(input('Informe o valor da base do retângulo: '))
altura = int(input('Informe o valor da altura do retângulo: '))

retangulo = Retangulo(base, altura)

pisos = retangulo.area()
rodapes = retangulo.perimetro()

print(f'Pisos (1 x 1 m²): {pisos}')
print(f'Rodapés (1 m): {rodapes}')
