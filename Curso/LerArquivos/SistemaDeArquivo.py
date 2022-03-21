"""
    Sistema de Arquivos e Navegação

os -> Móduo importavel Operating System
"""

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
os.chdir('..') # Retorna o caminho
print(os.getcwd())
# Checar se o repositório é absoluto ou relativo (se começa ou não com uma /)
print(os.path.isabs("Users/vitao/OneDrive/Documentos"))
# Se eu quiser usar o \ tenho que usar \\ desse jeito C:\\Users\\vitao\\OneDrive\\Documentos

# Da pra identificar o sistema operaciona com o os
print(os.name) #posix - Linux Mac / nt - Windows


# Adicionar caminhos 
# O os.path.join recebe o diretório atua e o segundo que sera juntado ao atual
res = os.path.join(os.getcwd(),'Teste','Dentro')
os.chdir(res)
print(os.getcwd())
os.chdir('..')

# Podemos listar os diretórios com listdir()
print(len(os.listdir('C:\\Users\\vitao\\OneDrive\\Documentos\\José'))) # Vazio ou pode escolher o diretório

print(list(os.scandir('C:\\Users\\vitao\\OneDrive\\Documentos\\José'))) # Iterator
arquivos = list(os.scandir())
#print(arquivos)
#print('Diretórios: ',dir(arquivos[0]))
print('Númeração na arvore de diretórios: ',arquivos[0].inode()) # ??
print('Nome: ',arquivos[0].name) # nome do arquivo
print('É diretório? ',arquivos[0].is_dir())
print('É arquivo? ',arquivos[0].is_file())
print('É link?? ',arquivos[0].is_symlink())
print('É caminho? ',arquivos[0].path)
print('É ? ',arquivos[0].stat())

