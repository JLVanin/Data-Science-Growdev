# 6) Faça um programa completo utilizando classes e métodos que:
# a) Possua uma classe chamada BombaCombustivel, com no
# mínimo esses atributos:
#    i) tipo_combustivel.
#    ii) valor_litro
#    iii) quantidade_combustivel
# b) Possua no mínimo esses métodos:
#    i) abastecer_por_valor() – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#    ii) abastecer_por_litro() – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#    iii) alterar_valor() – altera o valor do litro do combustível.
#    iv) alterar_combustivel() – altera o tipo do combustível.
#    v) alterar_quantidade_combustivel() – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

from Classes import BombaCombustivel

bomba_combustivel = BombaCombustivel('gasolina', 7.59, 1000)

bomba_combustivel.abastecer_por_litro(15)

print(f'{bomba_combustivel.quantidade_combustivel:.2f}')

bomba_combustivel.abastecer_por_valor(150)

print(f'{bomba_combustivel.quantidade_combustivel:.2f}')