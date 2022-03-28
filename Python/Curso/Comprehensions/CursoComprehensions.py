'''
    List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável. 

# Sintaxe da List Comprehension

[dado for dado in iteravel]
'''

# Exemplos

lista = [1,2,3,4,5]
res = [numero * 10 for numero in lista]
print(res)
res = [numero /2 for numero in res]
print(res)

# List Comprehensio versos Loop

lista_dobrada = []
for numero in lista:
    lista_dobrada.append(numero*2)
print(lista_dobrada)

print([lista_dobrada *2 for lista_dobrada in lista],'\n')

# Letras

nome = 'José Victor'

print([letra.upper() for letra in nome])

# Amigos

amigos = ['maria','julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos]) # pega a primeira letra

# Pares

numeros = [1,2,3,4,5,6,7,8]
pares = [numeroCalc for numeroCalc in numeros if numeroCalc % 2 == 0]
impares = [numeroCalc for numeroCalc in numeros if numeroCalc % 2 != 0]
print(pares)
print(impares)

# Refatorando
pares = [numeroCalc for numeroCalc in numeros if not numeroCalc % 2]
impares = [numeroCalc for numeroCalc in numeros if numeroCalc % 2]
print(pares)
print(impares)