'''
Mapas -> Conhecidos como Dicionários
Dicionários são representados por {}
'''

receita = {'jan':100,'fev':250,'mar':400}

# Interar
print('Interando:')
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Imprime as chaves
print('\nChaves:')
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Imprime os valores
print('\nValores:')
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento
print('\nDesempacotamento:')
print(receita.items())
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

print('\nSoma: ',sum(receita.values()))
print('Maior Valor: ',max(receita.values()))
print('Menor Valor: ',min(receita.values()))
print('Tamanho: ',len(receita))