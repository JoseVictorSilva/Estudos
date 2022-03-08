"""
    Set Comprehension
Mesma coisa que lista
"""

from locale import LC_MONETARY


numeros = {num for num in range(1,7)}
print(numeros)

numeros = {x ** 2 for x in range(1,7)}
print(numeros)

numeros = {x:x ** 2 for x in range(10)}
print(numeros)

# Final

letra = {letra for letra in 'José Victor Nogueira Alves da Silva'}
print(letra)