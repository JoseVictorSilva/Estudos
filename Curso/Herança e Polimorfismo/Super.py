"""
    POO - Super()


"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
    
    def som(self,som):
        print(f'O/A {self.__nome} faz {som}')
    
class Gato(Animal):
    def __init__(self,nome,especie,raca):
        super().__init__(nome,especie)
        super().som('aaaaaaaaaaa')
        self.__raca = raca

nala = Gato('Nala','Felina','Branca')
nala.som('miau')