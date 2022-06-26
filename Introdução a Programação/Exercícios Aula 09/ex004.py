# 4) Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
#   a) Atributos
#   i) Nome
#   ii) Fome
#   iii) Saúde
#   iv) Idade.
# b) Métodos
#   i) alterar_nome,
#   ii) alterar_fome
#   iii) alterar_saude
#   iv) alterar_idade
#   v) retornar_nome
#   vi) retornar_fome
#   vii) retornar_saude

from Classes import Tamagoshi

tamagoshi = Tamagoshi()

tamagoshi.alterar_nome('')
tamagoshi.alterar_fome()
tamagoshi.alterar_saude()
tamagoshi.alterar_idade()

print(tamagoshi.retornar_fome())
print(tamagoshi.retornar_saude())
print(tamagoshi.retornar_nome())
