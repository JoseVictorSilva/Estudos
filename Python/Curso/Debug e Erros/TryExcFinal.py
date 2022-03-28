"""
    Juntando com inputs
Sempre tratar quando tiver entrada de dados
"""
num = 0
try:
    num = 6 #int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else: #Entra caso não va no except
    print(f'Você digitou: {num}')
finally: # Normalmente utilizado para fechar ou desalocar recursos
    print('Finalizado')

# Forma correta de tratar erros
# Forma Errada -> Colocar um try pra cada variavel/print

def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError: # pode fazer except (Value Error, ZeroDivisionError) as err
        print('Não pode dividir por 0') 
    except:
        print('Algo deu errado')

num1 = input("Informe o 1 número: ")
num2 = input("Informe o 2 número: ")
print(dividir(num1,num2))

