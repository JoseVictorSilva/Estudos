def cabecalho(texto: str,alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')

print(cabecalho('José Victor'))
print(cabecalho('José Victor', alinhamento = False))
print(cabecalho('José Victor', alinhamento = 'zé')) # mypy falaria que isso da erro, pra isso executar no terminar mypy nome_arquivo

# __annotations__ pra saber o que chega e o que sai de uma função
nome: str = 'José' # self.__nome: str = nome

def teste(nome,alinhamento):
    #type (str,bool) -> str
    return 2
from typing import *

nomes: List[str] = {'José', 'Victor'}
nomes: Dict[str,bool] = {'ar':True,'teste':False }

