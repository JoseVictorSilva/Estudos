"""
    Decorators com diferentes asssinaturas

Para resolver, utilizamos um padrão de projeto chamado Decorator Patterns (* args)
"""

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar
@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'
@gritar
def ordenar(principal,acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}'

print(saudacao('José'))

# print(ordenar('Picanha','Batata frita'))

# Refazendo
def gritar(funcao):
    def aumentar(*args,**kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar
@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'
@gritar
def ordenar(principal,acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}'

print(saudacao('José'))

print(ordenar('Picanha','Batata frita'))

# Verifica recebe um valor
def verifica_primeiro_argumento(valor): # Aqui entra a pizza e o 10
    # Interna é a decorada
    def interna(funcao):
        # Outra é validação
        def outra(*args,**kwargs):
            if args and args[0] != valor: # Aqui vai comparar se o primeiro valor é pizza ou 10
                return f'Valor incorreto'
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    for n in args:
        print(n, end=' ')

@verifica_primeiro_argumento(10)
def soma__dez(num1,num2): #Poderia ter colocado args sum(args)
    return num1+num2

print(soma__dez(10,12))
print(soma__dez(12,5))
print(comida_favorita('pizza','lanchao'))
print(comida_favorita('lanchao','churras'))
