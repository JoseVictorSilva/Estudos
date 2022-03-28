"""
    Min e Max
max() - > Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
"""
print('----- LISTA -----')
lista =[1,5,9,32,4,7,2]
print(max(lista))
print(min(lista))
print('----- TUPLA -----')

tupla =(1,5,9,32,4,7,2)
print(max(tupla))
print(min(tupla))
print('----- SET -----')

set ={1,5,9,32,4,7,2}
print(max(set))
print(min(set))

print('----- DICIONÁRIO -----')
dicionario ={'a':1, 'b':5, 'c':9, 'd':32, 'e':4, 'f':7, 'g':2}
print(max(dicionario)) #para pegar o valor da chave .values()
print(min(dicionario))

# Veja qual valor é o maior

a = 10
b = 1
print(max(a,b)) # Posso passar quantos valores eu quiser, seja max(a,b,c,d,e,g,h)

# Exemplos
nomes = ["Samuel", "Carla", "Jeff", "Eduardo", "José", "Anna", "Thiago"]
print('Último nome: ',max(nomes))
print('Primeiro nome: ',min(nomes))
print('Maior nome: ',max(nomes, key = lambda nome:len(nome)))
print('Menor nome: ',min(nomes, key = lambda nome:len(nome)),'\n')


musicas = [
    {'titulo': "Caneta Azul", "Tocou": 4},
    {'titulo': "Kanye West", "Tocou": 5},
    {'titulo': "Mina de Vermelho", "Tocou": 3},
    {'titulo': "Skrillex", "Tocou": 1}
]
print('Musica alfabética maior: ',max(musicas, key = lambda musica: musica['Tocou'])['titulo'])
print('Musica alfabética menor: ',min(musicas, key = lambda musica: musica['Tocou'])['titulo'],'\n')
teste =[]
print('Musicas ',[teste.get('titulo') for teste in musicas])
for musica in musicas:
    print('Nome: ',musica.get('titulo'))