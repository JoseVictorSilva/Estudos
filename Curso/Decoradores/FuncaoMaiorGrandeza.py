"""
    Funções de Maior Grandeza - Higher Order Functions = HOF

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

0BS: Na pasta de funções ja foi utilizado
"""

def somar(a,b):
    return a+b

def diminuir(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def calcular(num1,num2,funcao):
    return funcao(num1,num2)

print('Soma: ',calcular(4,2,somar))
print('Subtração: ',calcular(4,2,diminuir))
print('Multiplicação: ',calcular(4,2,multiplicar))
print('Divisão: ',calcular(4,2,dividir))

# Podemos ter funções dentro de funções que seriam Nested Functions/Inner Functions
from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ','Suma daqui ','Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Thiago'))