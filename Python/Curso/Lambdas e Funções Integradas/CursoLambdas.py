"""
    Lambdas são conhecidas por expressões sem nome, ou seja, funções anonimas
    São expressões
# Funções em Python
"""

# Funções em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressões Lambda

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter com multiplas entradas

nomeCompleto = lambda nome,sobrenome: nome.strip().title() + ' '+sobrenome.strip().title() # strip() tira o espaço
print(nomeCompleto(' josé ', ' nogueira '))

# Lambdas não precisam ter entrada

rosh = lambda : 'Hora do rosh'
print(rosh(),'\n')

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur Conan Doyle']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # forma mais usual de usar lambdas
print(autores)

# Função Quadratica
# f(x): a*x**2 + b*x + c

def funcao_quadratica(a,b,c):
    """Retorna a função quadrática:f(x): a*x**2 + b*x + c """
    return lambda x: a*x**2 + b*x + c

teste = funcao_quadratica(2,3,-5)

print(teste(0))
print(teste(1))
print(teste(2))
print(funcao_quadratica(2,3,-5)(0))

