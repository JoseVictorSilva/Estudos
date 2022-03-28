"""
    Assertions (Afirmações / Checagens / Questionamentos)

- Em pyton utilizamos o 'assert' para realizar simples afirmações utilizadas nos testes.

- Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não. 
- Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError. 

OBS:Nós podemos epecificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

"""
# Cuidado ao usar o assert -> se o programa python for usado com o parâmetro -o nenhum assertion será validado
def soma_numeros_positivos(a,b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a+b

ret = soma_numeros_positivos(2,4)
print(ret)
#ret = soma_numeros_positivos(-2,4)
print(ret)

def comer_fast_food(comida):
    assert comida in ['pizza', 'sorvete', 'doces', 'batata frita', 'cachorro quente'], 'A comida precisa ser um fast food'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))