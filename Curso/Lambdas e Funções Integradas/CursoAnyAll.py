"""
    Any & All
all() -> retorna true se todos os elementos do iteravel são verdadeiros ou se o iterável esta vazio
any() -> retorna true se qualquer elemento for verdadeiro, se estiver vazio, da falso
"""

# Exemplo all()

print(all([0,1,2,3,4]))

nomes = ['Carla','Camila','Cassio', 'Carlos']
print(all([nome[0] == 'C' for nome in nomes])) # Se todos as primeiras letras dos nomes tem a letra J

print(all([letra for letra in 'b' if letra in 'a'])) # Vai dar true independente do que colocar, porque se o iteravel estiver vazio ele volta True
print(any([letra for letra in 'b' if letra in 'a']))
