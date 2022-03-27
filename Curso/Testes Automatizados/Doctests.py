"""
    Doctests

- Criar documentações para as funções que funcionam como testes

- Para usar: python -m doctest -v nome_do_modulo.py 

OBS: Não reconhece aspas duplas, só simples
OBS: Espaços e tabs prejudicam a execução
"""

import doctest

# Se eu colocar um teste e colocar que espero um erro, ele passa também ja que retorna um erro

def soma(a,b):
    """soma os número a e b
    >>>soma(1,2)
    3
    """
    return a+b

print(soma(3,4))