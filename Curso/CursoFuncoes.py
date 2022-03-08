'''
    Funções
    
- Funções são pequenos trechos de código que realizam tarefas específicas
- Nome das funções sempre em minusculo e com _
- Parametros opcionais
- Não precisa de return necessariamente pra retornar algo
- Variavel Local se sobrepõe a globais
- Pode-se ter funções dentro de funções

def fora():
    contador = 0
    def dentro():
        nonLocal contador
        contador += 1
        return contador
    return dentro()'''

cores = ['verde','azul']
cores.append('roxo')
#cores.append('Mais dados...') erro
print(cores)
cores.clear()
print(cores)

def diz_oi():
    print('oi')

def retorno():
    return 7*7

def quadrado(num):
    return num**2

def nome_completo(nome, sobrenome):
    return f'Oi {nome} {sobrenome}'

def exponencial(num, param=2): # Cria um parametro padrão, esse valor padrão sempre tem que ficar no final
    return num ** param

def soma(num1, num2):
    return num1 + num2 

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def sub(num1, num2):
    return num1 - num2

diz_oi()
copiaFuncao = diz_oi
copiaFuncao()

print(retorno(),)

print(quadrado(6),'\n')

print(nome_completo('José', 'Victor'))
print(nome_completo('Victor', 'José'))
print(nome_completo(sobrenome = 'Victor', nome = 'José'),'\n')

print(exponencial(2))
print(exponencial(2,3)) #substitui o 2 parametro
print(exponencial(2,4),'\n')

print('Teste Funções: ',mat(2,3))
print('Teste Funções: ',mat(2,2,sub))