"""
    StringIO
- Para ler arquivos do sistema o programa precisa ter permissão
- StrinIO -> Utilizado para ler e criar arquivos em memória, ele não grava. 
"""

from io import StringIO

mensagem = 'Este é apenas um teste \n'

# Podemos criar um arquivo em memória ja com uma string inserida ou mesmo vazio

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt','w') -> mesma coisa da linha de cima

print(arquivo.read()) # Não é criado nennhum arquivo
arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())