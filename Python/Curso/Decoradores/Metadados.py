"""
    Preservando metadatas com wraps

- Metadados -> São dados intrísecos em arquivos. 

- wraps -> São funções que envolvem elementos com diversas finalidades

"""
from functools import wraps
def ver_log(funcao):
    @wraps(funcao) # Um decorator que vai fazer com que soma.__name__ e __doc__ apareça de soma em vez de logar
    def logar(*args,**kwargs):
        """ Eu sou uma função (logar) dentro de outra"""
        print(f'Você esta chamando: {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a+b

print(soma(10,20))

# Pro erro que esta acontecendo, é preciso importar o wraps
print(soma.__name__) # Aparece o nome de logar
print(soma.__doc__) # Aparece o doc de logar