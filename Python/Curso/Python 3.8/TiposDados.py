"""
- Literar type
- Union
- Final
- Typed dictionaries
- Protocols
"""

from re import A
from typing import Literal,Union,Final,TypedDict,Protocol

def pegar_status(usuario:str) -> Literal["conectado","desconectado"]:
    return 'conectado'

print(pegar_status(teste:=''))
#!r pra destacar algo

# Union
def soma(num1: int, num2:int) -> Union[str,int]:
    resultado: int = num1+num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else: 
        return f'{resultado}'

# Final
# Se tiver classe com o decorador @final, essa classe não podera ser herdada (MYPY)
NOME: Final = 10 # Não é possível alterar

#NOME += 1
print(NOME)

# Type Dict
class ClasseDicionario(TypedDict):
    a: str
    b: int

print(outro:=ClasseDicionario(algo='vai',teste=1))

# Protocol

class Titulo(Protocol):
    # Todo objeto TEM que instanciar os atributos das formas que foram feitas
    titulo: str

class Venda:
    titulo = 'oi'

def estudar(valor:Titulo):
    print(f'Estou tentando estudar {valor.titulo}')

c1 = Titulo()
c1.titulo = 'Python'
v1 = Venda()

estudar(c1)
estudar(v1)
