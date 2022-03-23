"""
    POO - Abstração e Encapsulamento

- Encapsular -> Cápsula, a classe se torna a capsula de atributos e métodos
- Abstração em POO -> Ato de expor apenas dados relevantes de uma classe, 
escondendo atributos e métodos privados de usuários
"""

class Conta:
    contador = 400

    def __init__(self, titular,saldo,limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        self.__saldo -= valor  

conta1 = Conta('José',8000,2000)
print(conta1.numero)  
print(conta1.titular)  
print(conta1.saldo)  
print(conta1.limite)  

conta1.numero = 42
conta1.titular = 'dadsa'
conta1.saldo = 1
conta1.limite = 1

print(conta1.__dict__)