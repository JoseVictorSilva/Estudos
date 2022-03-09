'''
    **kwargs

Este é só mais um parametro, mas diferente do *args, que coloca os valores extras em uma tupla,
o **kwargs exige que utilizaemos paramtros nomeados, e transforma esses parametros extras em um dicionário. 

def soma_multiplos_numeros(a,b,c):
    print(a+b+c)
lista = [1,2,3]
tupla = (1,2,3)
set = {1,2,3}
dicionario = dict(a=1,b=2,c=3)
soma_multiplos_numeros(*lista) -> desempacota
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set) 
soma_multiplos_numeros(**dicionario)

OBS: O nome das chaves do dicionario pra desempacotar deve ser o mesmo da função
'''

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


def verificando(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Meus cumprimentos'
    elif 'geek' in kwargs:
        return f"Salve {kwargs['geek']} Geek!"
    return 'Quem é você'

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

cores_favoritas(marcos = 'Verde', Fernanda = 'Azul', Jose = 'Preto')
print(verificando(geek = 'Python'))
print(verificando(geek = 'José'))
print(verificando(briga = 'treta'),'\n')

# Desempacotar **kwargs
nomes = {'nome': 'José', 'sobrenome': 'Nogueira'}
#print(mostra_nomes(nomes)) -> erro
print(mostra_nomes(**nomes)) # Desempacota