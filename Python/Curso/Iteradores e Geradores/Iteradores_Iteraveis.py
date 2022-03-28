"""
    Iteradores e Iteraveis (Iterator/Iterable)

- Iterador -> Um Objeto que pode ser iterador
    Ex: Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada
    Retorna um dado que seria no caso 'Geek' ou 1,2,3,4,5

- Iteravel -> Um objeto que irá retornar um iterator quando a função iter() for chamada (Tudo que possa repetir com loop for)
    Retorna um iterator
"""

nome = 'José' # Iterable mas não é iterator
lista = [1,2,3,4] # Iterable mas não é iterator

it1 = iter(nome)
it2 = iter(lista)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1)) # Se desse mais um daria StopIteration

for n in nome:
    print(nome)

