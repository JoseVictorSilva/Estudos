"""
    Try/ Except

"""
try:
  printf('teste')
except:
  print('Deu erro')
finally:
  print('Tentativa finalizada \n')

try:
  geek()
except NameError as err: # Só pega NameError
  print('Função inexistente: ', err,'\n')

try:
  printf('x')
except NameError as err:
  print('Erro de nome: ', err,'\n')
except TypeError as err:
  print('Erro do Tipo: ', err,'\n')
except:
  print('Outro tipo de erro','\n')

def pega_valor(dicionario,chave):
    try:
      return dicionario[chave]
    except KeyError:
      return None
    except TypeError:
        return None

dic = {"nome":"Geek"}
print(pega_valor(dic,"nome"))