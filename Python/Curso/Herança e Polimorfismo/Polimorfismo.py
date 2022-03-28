"""
    POO - Polimorfismo

Cada animal abaixo vai falar de um jeito, eles herdam a mesma classe mas fazem coisas diferentes
"""

class Animal(object): # Tanto faz ter o object
    def __init__(self,nome):
        self.__nome = nome
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
    def comer(self):
        return f'{self.__nome} está comendo'

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
        return f'{self._Animal__nome} fala auauaau'
class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
        return f'{self._Animal__nome} fala miaaaaau'
class Rato(Animal):
    def __init__(self,nome):
        super().__init__(nome)


Nala = Gato('Nala')
print(Nala.comer())
print(Nala.falar(),'\n')
Lucky = Cachorro('Lucky')
print(Lucky.comer())
print(Lucky.falar(),'\n')
Ratoberto = Rato('Ratoberto')
print(Ratoberto.comer())
print(Ratoberto.falar())
