"""
    Map

Com Map, fazemos mapeamento de valores para função. 
"""
import math

def area(r):
    """Calcula a area de um circulo com raio 'r' """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3),'\n')

raios = [2,5,7.1,0.3,10,44]

# Forma Comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas,'\n')

# Forma do Map

print('----- Usando Map -----')
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object
areas = map(area,raios) # Usa-se lambdas
print(areas)
print('Lista de mapas: ',list(areas))
print('Tipo: ',type(areas))
print('Tipo: ',type(list(areas)),'\n')

# Usando Lambdas e Maps
print('Usando Lambdas: ',list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera

# Para fixar - Map
"""
    Temos dados iteráveis: 
    dados -> a1, a2, ..., an
    Temos uma função:
    Função -> f(x)
    Utilizamos a função map(f,dados) onde irá 'mapear' cada elemento dos dados e aplicar a função.
    O Map Object é algo tipo: f(a1), f(a2), f(a3)
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo',36), ('Barueri',32), ('Carapicuiba',30), ('Jandira',100), ('Osasco',-100)]
print(cidades)
# Lambda
c_para_f = lambda dado: (dado[0], (9/5)*dado[1]+32)
print(list(map(c_para_f, cidades))) # Ele passa um por um, e não cidades inteiro, então o tratamento é unico
