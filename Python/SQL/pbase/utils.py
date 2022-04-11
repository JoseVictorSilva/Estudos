

def conectar():
    """
    Função para conectar ao servidor
    """
    print('Conectando ao servidor...')

def desconectar():
    """ 
    Função para desconectar do servidor.
    """
    print('Desconectando do servidor...')


def listar():
    """
    Função para listar os produtos
    """
    print('Listando produtos...')

def inserir():
    """
    Função para inserir um produto
    """  
    print('Inserindo produto...')

def atualizar():
    """
    Função para atualizar um produto
    """
    print('Atualizando produto...')

def deletar():
    """
    Função para deletar um produto
    """  
    print('Deletando produto...')

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
