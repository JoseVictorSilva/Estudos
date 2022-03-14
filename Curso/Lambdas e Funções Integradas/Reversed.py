"""
    Reversed

OBS: Não confunda com o reverse() em listas
Retorna um iteravel chamado List Reverse Iterator
"""

from tracemalloc import start


tupla = (1,2,4,5,9)
reve = reversed(tupla)
print(reve)

# Podemos converter o elemento para uma Lista, Tupla, Conjunto... 
print(list(reversed(tupla)))
print(tuple(reversed(tupla)))
print(set(reversed(tupla))) # Não se define ordem em conjuntos

# Pode se iterar
for letra in reversed('José Victor'):
    print(letra, end = '')

# Da pra fazer o mesmo sem for
print('\n',''.join(list(reversed('José Victor'))))
# OU
print('José Victor'[::-1])

for n in reversed(range(0,10)):
    print(n)