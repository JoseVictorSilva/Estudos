"""
    POO - Herança Múltipla

- Multiderivação Direta;
- Multiderivação Indireta;

"""
# Exemplo - Multiderivação Direta

class Base1:
    pass
class Base2:
    pass
class MultiDerivada(Base1,Base2):
    pass

# Exemplo - Multiderivação Indireta

class BaseIndireta2(Base1):
    pass
class BaseIndireta3(Base2):
    pass
class MultiDerivadaIndireta(BaseIndireta3):
    pass

class Animal:
    def __init__(self,nome):
        self.__nome = nome
    def cumprimenta(self):
        return f'Eu sou o {self.__nome}'
class Aquatico(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def nadar(self):
        return f'{self._Animal__nome} está nadando'
    def cumprimenta(self):
        return f'Eu sou o {self._Animal__nome} do mar'

class Terrestre(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def andar(self):
        return f'{self._Animal__nome} está nadando'
    def cumprimenta(self):
        return f'Eu sou o {self._Animal__nome} da terra'

class Pinguim(Aquatico,Terrestre):
    def __init__(self,nome):
        super().__init__(nome)

baleia = Aquatico('Baleia')
print(baleia.nadar())
print(baleia.cumprimenta())

tatu = Terrestre('Tatu')
print(tatu.andar())
print(tatu.cumprimenta())

pinguim = Pinguim('Pinguim')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimenta()) # Ele vai cumprimentar de acordo com a ordem da herança em Pinguim(Aquatico,terrestre)
# Pra saber quem vai executar, pode usar com Pinguim.__mro__, Pinguim.mro(), help(Pinguim)

print(f'Tux é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Tux é instância de Pinguim? {isinstance(pinguim, Aquatico)}')
print(f'Tux é instância de Pinguim? {isinstance(pinguim, Terrestre)}')
print(f'Tux é instância de Pinguim? {isinstance(pinguim, Animal)}')
print(f'Tux é instância de Pinguim? {isinstance(pinguim, object)}')