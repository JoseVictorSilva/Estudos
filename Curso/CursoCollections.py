''' Módulos Collections
Colletions -> High-performance Container Datetypes
Counter -> Recebe um interável como parâmetro e cria um objeto do tipo 
            Collections Counter que é parecido com um dicionário, contendo como 
            chave o elemento da lista passada como parâmetro e como valor a quantidade 
            de ocorrências desse elemento'''

# Utilizando Counter

from ast import Lambda
from collections import Counter, defaultdict, namedtuple, deque
from typing import OrderedDict

lista = [1,1,2,1,3,5,1,2,1,4,2,1,84,65,88,84,65] #poderia ser qualquer outro tipo de container
res = Counter(lista)

print(f'{type(res)}: {res}')
print(Counter('José Victor Nogueira Alves da Silva'))

wiki = """A Wikipédia é um projeto de enciclopédia multilíngue de licença livre,[5][6] 
baseado na web e escrito de maneira colaborativa.[6] O projeto encontra-se sob administração 
da Fundação Wikimedia,[7] uma organização sem fins lucrativos cuja missão é "empoderar e engajar 
pessoas pelo mundo para coletar e desenvolver conteúdo educacional sob uma licença livre ou no 
domínio público, e para disseminá-lo efetivamente e globalmente"."""

palavras = wiki.split()
res = Counter(palavras)
print("Mais Comuns: ",res.most_common(5))

# Utilizando Default Dict
# Não apresenta o keyError pois tem um valor default podendo ser um lambda 
# Este valor será utilizado sempre que não houver um valor definido. Caso 
# tentemos acessar uma chave que não exista, essa chave será criada com default
# OBS: Lambdas são funções sem nome que podem ou não receber parametros de entrada ou retornar valores
print('\nDefault Dict')

dicionario = defaultdict(lambda: 0) # 0 é o valor default
dicionario['curso'] = 'Python'
print(dicionario)
print(dicionario['Outro'])
print(dicionario)

# Utilizando Ordered Dict

print('\nOrdered Dict')
dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4})
print(type(dicionario))
for chave, valor in dicionario.items():
    print(f'Chave = {chave} e Valor = {valor}')

dict = {'a':1,'b':2}
dict2 = {'b':2, 'a':1}
print(dict == dict2) # Não importa a ordem

odict = OrderedDict({'a':1,'b':2})
odict2 = OrderedDict({'b':2, 'a':1})
print(odict == odict2)

# Utilizando Named Tuple
# São tuples diferenciadas em que especificamos nomes e parametros

print('\nNamed Tuple')

# Forma 1
cachorro = namedtuple('cachorro','idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro','idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade','raca','nome'])
# Usando
Lucky = cachorro(idade = 3, raca = 'Maltês', nome = 'Lucky')

# Acessando Dados
print(Lucky)
print('Usando [valor]: ',Lucky[0])
print(Lucky[1])
print(Lucky[2],'\n')

# Forma 2
print('Utilizando .nome/.idade/.raca -> ',Lucky.nome)

# Utilizando Deque
# É uma lista

print('\nNamed Tuple')

deq = deque('geek')
print(deq)

# Adicionando valores
deq.append('y')
print(deq)
deq.pop()
print(deq)