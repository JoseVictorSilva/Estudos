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
print(numeros)