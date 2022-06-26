# 3) Crie uma classe para implementar uma conta corrente. A classe
# deve possuir os seguintes atributos:
#    a) número da conta
#    b) nome do correntista
#    c) saldo
# Os métodos são os seguintes:
#   a) alterar_nome
#   b) deposito
#   c) saque
# No construtor, o saldo é opcional, com valor padrão zero e os
# demais atributos são obrigatórios.
from Classes import Conta

conta = Conta('', '')


conta.deposito()
conta.mostra_saldo()
conta.saque()
conta.mostra_saldo()
