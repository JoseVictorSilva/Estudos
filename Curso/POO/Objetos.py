"""
    POO - Objetos

- Objetos -> Instâncias da classe
"""


class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False
    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class ContaCorrente:
    contador = 4999
    def __init__(self,limite,saldo,cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero
    
    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


class Cliente:
    def __init__(self, nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')

lamp1 = Lampada('branca',110,60)
print(f'A lampada esta ligada? {lamp1.checa_lampada()}')
lamp1.liga_desliga()
print(f'A lampada esta ligada? {lamp1.checa_lampada()}')

user1 = Usuario('José','Nogueira','ze@gmail.com','123145')

cli1 = Cliente('José Victor', '12345678910')
cc1 = ContaCorrente(2000,6000,cli1)
cc1.mostra_cliente() # Acessando atributos de fora da classe
cc1._ContaCorrente__cliente.diz() # Acessando métodos de fora da classe