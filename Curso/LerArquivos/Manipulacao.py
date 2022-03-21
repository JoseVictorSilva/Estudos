"""
    Sistema de Manipulação
"""

from genericpath import exists
import os
# Descobrindo se existe um arquivo ou diretório

print(os.path.exists('Dentro')) # Passar arquivos ou diretórios, depende da extensão ou também caminhos relativos ou absolutos

print(os.path.exists('C:\\Users\\vitao\\OneDrive\\Documentos'))

# Criando arquivos
    # Formas erras:
    # Forma 1 para escrita
open('Dentro/arquivo-teste.txt','w').close()
    # Forma 2 para escrita e leitura caso ja exista, se não cria
open('Dentro/arquivo-teste2.txt','a').close()
    # Forma 3
with open('Dentro/arquivo-teste3.txt','w') as arquivo:
    pass

    #Forma Correta:
# Com o mknod mas ele não funciona

# Criar diretórios 
#os.mkdir('Outro-Diretorio') # Da pra criar dentro de um caminho
#os.makedirs('Agora-Existe/Vamo-pra-outro/O-ultimo')

# Renomear (funciona pra diretorio e arquivo)
#os.rename('Outro-diretorio','diretorio-diferente')

# Remover arquivos e diretórios (não vai pra lixeira
# )
#os.remove('novo.txt')
#os.rmdir('Agora-Existe/Vamo-pra-outro/O-ultimo')

# Removendo uma arvore
print(list(os.scandir('Agora-existe')))
print(os.path)
'''for arquivo in os.scandir('Agora-existe/Vamo-pra-outro'):
    print(f'- {arquivo.name}')
    if(arquivo.is_file()):
        os.remove(arquivo.path)'''
# Criando diretório temporário 
import tempfile 

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporario em {tmp}')
    with open(os.path.join(tmp,'arquivo_temporario.txt'),'w') as arquivo:
        arquivo.write('José Victor Temporário\n')
    input()

with tempfile.TemporaryFile() as tmp:
    tmp.write('José Victor\n','wb')
    tmp.seek(0)
    print(tmp.read())