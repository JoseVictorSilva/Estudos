"""
    SEEK E CURSOR
- seek() -> É utilizada para movimentar o cursor pelo arquivo. 
    """
arquivo = open('texto.txt')
print(arquivo.read(),'\n')

# Movimentando o cursor pelo arquibo com a função seek()
arquivo.seek(0)
print(arquivo.read(12),'\n')

# Lendo linha por linha
arquivo.seek(0)
ret = arquivo.readline()
print(ret.split(' '))
print(type(ret))

# readLines() -> quantidade de linhas
# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador 
# e o programa chamada de streaming e precisa-se fechar essa conexão com close()
linhas = arquivo.readlines() 
print(len(linhas))

arquivo.close()