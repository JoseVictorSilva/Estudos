"""
    POO - Propriedades - Properties

"""
# Exemplo baseado em java: 
"""class Conta:
    contador = 0
    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero
    def set_numero(self,numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite

cc1 = Conta('José', 1000, 3000)
cc2 = Conta('Eduardo', 2000, 4122)

print(cc1.extrato())
print(cc2.extrato())

soma = cc1.get_saldo() + cc2.get_saldo()
print(soma)"""

class Conta:
    contador = 0
    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo = novo_saldo 
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

cc1 = Conta('José', 1000, 3000)
cc2 = Conta('Eduardo', 2000, 4122)

print(cc1.extrato())
print(cc2.extrato())

soma = cc1.saldo + cc2.saldo
print('Soma 1: ',soma)
cc1.saldo = 2000
soma = cc1.saldo + cc2.saldo
print('Soma 2: ',soma)

cc1.limite = 10000
print('Limite 1: ',cc1.limite)

print(f'Valor total 1: {cc1.valor_total}')
print(f'Valor total 2: {cc2.valor_total}')