"""
    JSON e Pickle

- JSON -> JavaScript Object Notation
- API -> São meios de comunicação entre os serviçõs oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (Nós desenvolvedores)

ret = json.dumps(['Produto', {'Playstation 4':('2TB','Novo','220V',2340)}])
print(type(ret))
print(ret)

class Gato():
    def __init__(self, nome,raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__nome

nala = Gato('Nala', 'Vira lata')
#print(nala.__dict__)
#ret = json.dumps(nala.__dict__)
#print(ret)

ret = jsonpickle.encode(nala)
print(ret)
# Integrando JSON com Picle

"""

import json,jsonpickle



class Gato():
    def __init__(self, nome,raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

nala = Gato('Nala', 'Vira lata')
with open('nala.json','w') as arquivo:
    ret = jsonpickle.encode(nala)
    arquivo.write(ret)
with open('nala.json','r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)