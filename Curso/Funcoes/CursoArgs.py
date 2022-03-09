'''
    Entendo o *args

- O *args é um parametro qualquer que pode-se chamar de qualquer coisa, desde que comece com asterisco

Ex: *xis

Convenção -> *args

O parametro * args utilizado em uma função, coloca os valores extras informados como
entradas em uma tupla. Então desde já lembre-se que tuplas são imutáveis. 
'''

def soma_todos_numeros(num1,num2,num3):
    return num1+num2+num3

def soma_args(*args):
    '''total = 0
    for numero in args:
        total += numero
    return total'''
    return sum(args)

def nome_soma_args(nome,email,*args):
    total = sum(args)
    return f'Oi {nome}, email: {email}, result: {total}'

def verifica (*args):
    if 'José' in args and 'josevictorcomrc' in args:
        return 'Bem vindo josé'
    return 'WTF'

def tupla (*args):
    return sum(args)
print(soma_todos_numeros(2,3,4))
#print(soma_todos_numeros(2,3)) -> Da erro
#print(soma_todos_numeros(2,3,4,5)) -> Da erro

# Entendendo o *args (sem o print e pedindo pra imprimir o args na funcao 'print(args)' aparece como uma tupla) 
print(soma_args(2,3,4))
print(soma_args(2,3))
print(soma_args(2,3,4,5))
print(nome_soma_args('José', 'josevictorcomrc', 2,5,8,9),'\n')

print(verifica(1,'José','josevictorcomrc',True,1.25))
print(verifica(1,'Carlitos','josevictorcomrc',True,1.25))
print(verifica(1,True,1.25),'\n')

numeros = [1,2,3,4,5,6,7]
# Desempacotar
print(tupla(*numeros)) # Avisa que ta passando uma lista e precisa ser desempacotada
