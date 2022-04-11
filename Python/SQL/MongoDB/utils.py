from ast import Try
from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from bson import errors as berros
def conectar():
    """
    Função para conectar ao servidor
    """
    conn = MongoClient('localhost',27017)
    return conn

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()

def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    db = conn.pMongo
    try:
        if db.produtos.count_documents({}) > 0:
            produtos = db.produtos.find()
            print('Listando produtos...')
            print('--------------------')
            for produto in produtos:
                print(f"ID: {produto['_id']}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Estoque: {produto['estoque']}")
                print('-------------------')
        else:
            print('Não existem produtos cadastrados')
    except erros.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')
    desconectar(conn)

def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    db = conn.pMongo
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o estoque do produto: '))
    try:
        db.produtos.insert_one(
            {
                "nome":nome,
                "preco":preco,
                "estoque":estoque
            }
        )
        print(f'O produto {nome} foi inserido com sucesso')
    except erros.PyMongoError as e:
        print(f'Não foi possível inserir o produto: {e}')
    desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    db = conn.pMongo
    _id = input('Informe o ID do produto: ')
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o estoque do produto: '))

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.update_one(
                {"_id": ObjectId(_id)},
                {
                    "$set":{
                        "nome":nome,
                        "preco":preco,
                        "estoque":estoque
                    }
                }
            )
            if res.modified_count == 1:
                print(f'O produto {nome} foi atualizada com sucesso.')
            else:
                print('Não foi possível atualizar o produto')
        else:
            print(f'Não existem produtos para serem atualizados')
    except erros.PyMongoError as e:
        print(f'Não foi possível inserir o produto: {e}')
    except berros.InvalidId as f:
        print(f'Object ID inválido: {f}')
    desconectar(conn)

def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    db = conn.pMongo
    _id = input('Informe o ID do produto: ')
    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.delete_one(
                {
                    "_id": ObjectId(_id)
                }
            )
            if res.deleted_count > 0:
                print('Produto deletado com suceso')
            else:
                print('Não foi possível deletar o produto')
        else:
            print('Não possuem produtos para serem deletados')
    except erros.PyMongoError as e:
        print(f'Não foi possível inserir o produto: {e}')
    except berros.InvalidId as f:
        print(f'Object ID inválido: {f}')
    desconectar(conn)

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
