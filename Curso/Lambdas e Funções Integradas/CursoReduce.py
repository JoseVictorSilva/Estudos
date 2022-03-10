"""
    Reduce
OBS: A partir do Python versão 3 e acima a função reduce() não é mais uma função integrada (built-in), 
ou seja, precisamos importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso 99% das vezes
um loop for é mais legível. 

Para entender o reduce():

Imagine que você tem uma coleção de dados:
dados = [a1,a2,a3,...,an]

E você tem uma função que recebe dois parâmetros:
def funcao(a,b):
    return a*b

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iteravel. 
A função reduce(), funciona da seguinte forma:
    Passo1: res1 = f(a1,a2) -> Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo2: res2 = f(res1,a3) -> Aplica a função no resultado do passo 1 + o 3 elemento, repetindo até 'an'
    Ele aplica a função passando como primeiro argumento o resultado da aplicação anterior. Reduce irá retornar o valor final
"""

# Na pratica -> Multiplicar todos os números da Lista

from functools import reduce
dados = [2,5,7,8,9,6,4,1,2,3,6,5,8]
# Para usar o reduce, precisamos de uma função que receba dois parametros

multi = lambda x,y: x*y
res = reduce(multi,dados)
print(res)

# Com for
res = 1
for n in dados:
    res = res * n
print(res)
