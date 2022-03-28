"""
    Generators
Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não foi visto Tuple, porque elas se chamam Generators

"""
# Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof 
# Usando Generators
nomes = ['Carla','Camila','Cassio', 'Carlos']
print(any(nome[0] == 'C' for nome in nomes)) # Se foi feita algum tipo de conversão, o resultado é apagado da memória

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res) # Mostra a lista de True/False
# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res) # Não mostra, só faz a checagem

print(getsizeof(True))

print(' ---- Tamanho de cada Comprehension ----')

list_comp = getsizeof([x*10 for x in range(1000)])
set_comp = getsizeof({x*10 for x in range(1000)})
dic_comp = getsizeof({x: x*10 for x in range(1000)})
gen = getsizeof((x*10 for x in range(1000)))
print('Para realizar a mesma tarefa gastamos:')
print(f'List Comprehension: {list_comp}') # Aceita tudo
print(f'Set Comprehension: {set_comp}') # Não aceita dados repetidos
print(f'Dictionary Comprehension: {dic_comp}') # Não aceita chaves repetidas
print(f'Generator Expression: {gen}')

# Iterando
gen = (x*10 for x in range(1000))

for num in gen:
    print(num)

print(type(num))