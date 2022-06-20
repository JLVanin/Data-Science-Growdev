
from Classes import Carro


meu_carro = Carro(15)

meu_carro.adicionar_gasolina(20)

meu_carro.andar(100)

print(f'{meu_carro.obter_gasolina():.2f} litros')