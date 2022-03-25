"""
    Conhecendo o Pickle

- Objeto Python -> Binarização
- Binarização -> Objeto Python

Este processo se chama de serialização/ descerialização

"""

import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self): 
        return self.__nome
    
    def comer(self):
        print(f'{self.__nome} está comendo')
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo')

"""nala = Gato('Nala')
lucky = Cachorro('Lucky')

# Escrita
with open('animais.pickle','wb') as arquivo: # Dado serializado
    pickle.dump((nala,lucky), arquivo)"""

# Leitura
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo) # Descompacta nos nossos objetos
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')