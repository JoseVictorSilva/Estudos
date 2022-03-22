"""
    Decoradores (Decorators)

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamento;
- Decorators são HOF
- Decorators tem sintaxe própria, usando "@"(Syntatic Sugar) 

"""
# Decoradores como funções

def seja_educado(funcao): # Funcao decorator por ter uma função
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia\n')
    return sendo

def raiva():
    print('EU TE ODEIO-')

def saudacao():
    print('Seja bem vindo')

teste = seja_educado(saudacao)
teste()

raiva_educada = seja_educado(raiva)
raiva_educada()

def sejda_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@sejda_educado_mesmo
def apresentando(): # Ela vai ser enviada automaticamente pra seja educada mesmo como parametro por conta do @
    print('Meu nome é Pedro')

apresentando()

#__________________________________
#| HOME | Produtos | Sexo | Admin |
#  
jose ='admin'
def login(funcao): # Função decorada
    def checa(usuarioJose): #Ele pega da passagem da funcao
        if funcao(usuarioJose): 
            print('Bem vindo adm')
        else: 
            print('Vaza escoria')
    return checa

@login # Decorator
def admin(usuario):
    if usuario == 'admin':
        return True
    else:
        return False
admin(jose)
"""def home(usuario):
    print('Pode acessar')

def produtos(usuario):
    print('Pode acessar')

def sexo(usuario):
    print('Pode acessar')
"""
