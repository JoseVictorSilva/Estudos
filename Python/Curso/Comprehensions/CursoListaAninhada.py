'''
    - Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
        - Unidimensionais (Arrays/Vetores)
        - Multidimensionais (Matrizes)
    Em python só existem, LISTAS

'''

listas = [[1,2,3],[4,5,6],[7,8,9]] # Matriz 3x3

print(listas)
print(type(listas))
print(listas[0][1])

# Iterando
[[print(valor) for valor in valorLista] for valorLista in listas]

# Jogo da Velha
velha = [['X' if numero%2==0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1,4)]for j in range(1,4)])

