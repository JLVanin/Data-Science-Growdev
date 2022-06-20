from msilib.schema import Class
from tkinter.messagebox import NO


class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mosta_cor(self):
        print(self.cor)

class Conta:
    def __init__(self, numero_conta, nome, saldo = 0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
    
    def alterar_nome(self, nome):
        self.nome = nome
    
    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
        else:
            print('Impossível depósito de valores negativos')
    
    def saque(self, valor):       
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo Insuficiente!')
            
    def mostra_saldo(self):
        print(f'R$ {self.saldo}')

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def mudar_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura
    def lados(self):
        return self.base , self.altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base * 2 + self.altura * 2

class Tamagoshi:
    def __init__(self):
        self.nome = None
        self.fome = None
        self.saude = None
        self.idade = None
    
    def alterar_nome(self, nome):
        self.nome = nome
    def alterar_fome(self, fome):
        self.fome = fome
    def alterar_saude(self, saude):
        self.saude = saude
    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_nome(self):
        return self.nome
    def retornar_fome(self):
        return self.fome
    def retornar_saude(self):
        return self.saude

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y     

    def exibe(self):
        print(f'{self.x}, {self.y}')  

class Ret:
    def __init__(self):
        self.ponto1 = None
        self.ponto2 = None
    
    def centro(self):
        ponto_central = Ponto()
        ponto_central.x = (self.ponto1.x + self.ponto2.x) / 2
        ponto_central.y = (self.ponto1.y + self.ponto2.y) / 2
        return ponto_central


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_combustivel, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_combustivel
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        print(f'Você abasteceu {litros:.2f} litros com total de R$ {valor}')
        self.alterar_quantidade_combustivel(litros)

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        print(f'Você abasteceu {litros:.2f} litros com total de R$ {valor}')
        self.alterar_quantidade_combustivel(litros)

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro
    
    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
    
    def alterar_quantidade_combustivel(self, litros):
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
        else:
            print('Quantidade de combustivel insuficiente')

class Carro:
    def __init__(self, consumo, tanque = 0):
        self.consumo = consumo
        self.tanque = tanque

    def andar(self, km):
        self.tanque -= km / self.consumo

    def obter_gasolina(self):
        return self.tanque

    def adicionar_gasolina(self, litros):
        self.tanque += litros

