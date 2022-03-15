'''
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipode de dados;
'''

# Criação de dicionários
# Mais comum
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))

# Segunda forma
paises = dict(br = 'Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando Elementos
print(paises['br']) # Se não existir a chave, dará keyError

# Forma 2 via Get (recomendado)
print(paises.get('br'))
print(paises.get('ru')) # se não existir da none

pais = paises.get('ru')

if pais:
    print(f"Encontrei o pais {pais}")
else:
    print(f"Não encontrei o pais")

# Valor padrão caso não encontre
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o pais {pais}')

print('\n')
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Qualquer tipo de dado é aceito (int, float, string, boolean), incluindo listas, tuplas, dicionário 

# Tuplas são interessantes por serem imutáveis
print('\nDados')
localidades = {(35.6895,15.5863):'Casa Thigaslol',
               (58.1358,58.6544):'Casa Duzera',
               (22.1234,47.6481):'Casa Giulinha'}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
print('\nAdicionando Elementos')
receita = {'jan':100, 'fev':50, 'mar':120}
print(receita)
print(type(receita))

# Forma 1
receita['abr'] = 200
print('Forma 1 a força: ',receita)

# Forma 2 
novo_dado = {'mai':250}
receita.update(novo_dado)
print('Forma 2 usando .update(): ',receita)

# Atualizando dados em um dicionário 
print('\nAtualizando Elementos')

# Forma 1
receita['fev'] = 15

# Forma 2
receita.update({'mai':20})
print(receita)

# A forma de atualizar é a mesma de adicionar MAS NÃO PODEMOS TER CHAVES REPETIDAS

# Remover elementos em um dicionário
print('\nRemovendo Elementos')
# Forma 1 (comum)
ret = receita.pop('mar') # Sem definir a chave, retira o ultimo elemento
print("Valor retirado: ",ret)
print(receita)

# Forma 2
del receita['fev']
print('Valor retirado por del: ',receita) 

print('\nExercício Carrinho')

# Utilizando listas
carrinho = []
produto1 = ['Playstation 4', 1, 2300.000 ]
produto2 = ['God Of War 4', 1, 150.000]

carrinho.append(produto1)
carrinho.append(produto2)
print(f'{type(carrinho)}: {carrinho}')

# Utilizando tuplas
produto1 = ('Playstation 4', 1, 2300.000)
produto2 = ('God Of War 4', 1, 150.000)
carrinho = (produto1, produto2)
print(f'{type(carrinho)}: {carrinho}')

# Utilizando Dicionários
carrinho = []
produto1 = {'nome':'Playstation 4', 'Quantidade':1, 'Preço':2300.000}
produto2 = {'nome':'God Of War', 'Quantidade':1, 'Preço':150.000} 
carrinho.append(produto1)
carrinho.append(produto2)
print(f'{type(carrinho)}: {carrinho}')

# Métodos
print('\nMétodos')

d = dict(a=1, b=2, c=3)
print(f'{type(d)}: {d}')

print('\nLimpar')
d.clear()
print(d)

print('\nCopiar')

d = dict(a=1, b=2, c=3)
novo = d.copy()
print('---Deep Copy---')
novo['d'] = 4
print('Antigo: ',d)
print('Novo: ',novo)

print('---Shallow Copy---')
novo = d
novo['d'] = 4
print('Antigo: ',d)
print('Novo: ',novo)

# Usando {}.fromkeys()
print('\nNovo Tipo de Criação')
outro = {}.fromkeys('a', 'b')
print(f'{type(outro)}: {outro}')

usuario = {}.fromkeys(['nome','pontos','email','profile'], 'desconhecido')
print(f'{type(usuario)}: {usuario}')

veja = {}.fromkeys('teste', 'valor')
print(veja)
veja = {}.fromkeys(range(1,11),'novo')
print(veja)

