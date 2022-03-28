"""
    Sorted
OBS: Não confunda com a função sort() que só funciona em listas. 
Pode-se usar o sorted() com qualquer iteravel
O sorted() serve pra ordenar os elementos
"""

# Exemplos

numeros = [6,5,8,1,3,4]
print(numeros)
print(sorted(numeros)) # Sempre retorna uma LISTA
print(sorted(numeros, reverse = True))
print(numeros,'\n')

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"Username": "Samuel", "Tweets":["Eu adoro bolo", "Eu adoro pizza"]},
    {"Username": "Carla", "Tweets":["Eu adoro cães", "Eu gosto de você"]},
    {"Username": "Jeff", "Tweets":["Eu adoro gatos", "Eu adoro programar"], "Cor": "amarelo"},
    {"Username": "Eduardo", "Tweets":[]},
    {"Username": "José", "Tweets":["Eu adoro brincar", "Eu amo meu cachorro"]},
    {"Username": "Anna", "Tweets":["Eu adoro jogar", "Eu odeio pizza"], "Cor": "preto", "Musica": "Rock"}
]
#print(usuarios)
lista = sorted(usuarios, key = lambda usuario: usuario["Username"]) # Pode pegar os tweets se colocar ai
nomes = sorted(usuarios, key = lambda usuario: usuario.get('Username'))
for usuario in usuarios:
    print(usuario.get('Username'))

print('\n',lista[0],'\n')
print('Usuários: ',nomes)