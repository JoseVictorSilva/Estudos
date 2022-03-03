''' 
Conjuntos em qualquer linguagem de programação, estamos fazendo referência 
à Teoria dos Conjuntos da Matemática

- Aqui no Python, os conjuntos são chamados de Sets. 

Dito isto, da mesma forma que na matemática: 
- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas 
não nos importamos com a ordenação deles. Quando não precisamos se preocupar 
com chaves, valores e itens duplicados. 

Os conjuntos são referenciados em Pyhton com chaves {}

Diferença entre Conjuntos e Mapas em Python:
- Um dicionário tem chave/valor;
- Um conjunto tem apenas valor;

Lembrando, não possui ordem
'''

s = set({1,2,3,4,5,5,6,7,2,3})
print(s)
print(type(s))

# Da para alterarmos listas/tuplas para se tornarem sets
lista = [1,2,3,4,5,5,6,7,2,3]
print("LISTA\n",type(lista))
print(set(lista))
print(type(set(lista)))
lista = (1,2,3,4,5,5,6,7,2,3)
print("\nTUPLA\n",type(lista))
print(set(lista))
print(type(set(lista)))

if 3 in s:
    print("Tem o 3")

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [52,2,8,39,4,85,2,45,27,27]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (52,2,8,39,4,85,2,45,27,27)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionário não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([52,2,8,39,4,85,2,45,27,27], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {52,2,8,39,4,85,2,45,27,27}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

conjunto = {1,'b',True,34,22}
print("Conjunto com valores variados:\n",type(conjunto))
print(conjunto,"\nIterando:")
for valor in conjunto:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formuçário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram. Mas queremos adicionar a cidade em uma lista python
# ja que em uma lista podemos adicionar novos elementos e ter repetição
print("\nExercício Cidades")
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'São Paulo', 'Campo Grande']
print("Cidades e Quantidade de pessoas que visitaram: ",cidades,",", len(cidades))
print("Cidades não repetidas:",set(cidades),len(set(cidades)))

# Adicionando e removendo elementos em um conjunto
s = {1,2,3}
s.add(4),s.add(5),s.add(4)
print("Adicionando .add()",s)
s.remove(4) #não é indice, é valor, mas se não encontrar o valor vai dar key error
print("Usando .remove()",s)
s.discard(5) #se não encontrar valor, não da erro
print("Usando .discard()",s)

# Copiando um conjunto pra outro
# Deep Copy - Não altera a memória
print("\nCopiando")
novo = s.copy()
print("Deep: ",novo)
novo.add(4)
print(novo)
print(s)

# Shallow copy - Altera a memória
novo = s
novo.add(4)
print("Shallow: ",novo)
print(s)

# Métodos matemáticos de Conjuntos
# Imagine que temos dois ocnjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.
print('Exercício Estudantes')
estudantes_python = {'Marcos','Patricia','Ellen','Pedro','Julia','Guilherme'}
estudantes_java = {'Fernando','Gustavo','Julia','Ana','Patricia'}
print("- Juntar os Estudantes -")
uniao1 = estudantes_python.union(estudantes_java)
print("Primeiro jeito: .union() -> ",uniao1)

uniao2 = estudantes_python | estudantes_java

print("Segundo jeito: | -> ",uniao2)

# Agora veremos quem esta em ambos os cursos
print("\n- Quem estuda em ambas as grades -")

ambos1 = estudantes_python.intersection(estudantes_java)
print("Primeiro jeito: .intersetion() -> ",ambos1)
ambos2 = estudantes_python & estudantes_java
print("Segundo jeito: & -> ",ambos2)

# Gerar dos estudantes que estão em um e não no outro
print("Usando .difference()")
so_python = estudantes_python.difference(estudantes_java)
print("Quem esta só em Python",so_python)

so_java = estudantes_java.difference(estudantes_python)
print("Quem esta só em Java",so_java)

# Soma, max, min, tamanho
print("\nPadrões")
s = {1,2,3,4,5,6}
print(max(s))
print(min(s))
print(len(s))
print(sum(s))