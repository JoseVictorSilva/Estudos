from datetime import datetime
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
    Função para listar os usuários
    """
    conn = conectar()
    db = conn.ProjetoGrafico
    try:
        if db.Pessoa.count_documents({}) > 0:
            pessoas = db.Pessoa.find()
            print('Listando as Pessoas...')
            print('----------------------')
            for pessoa in pessoas:
                print(f"ID: {pessoa['_id']}")
                print(f"Nome: {pessoa['Nome']}")
                print(f"Trabalho: {pessoa['Trabalho']}")
                print(f"Estudos: {pessoa['Estudos']}")
                print(f"Fazendo: {pessoa['Fazendo']}")
                print('-------------------')
        else:
            print('Não existem pessoas cadastrados')
    except erros.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')
    desconectar(conn)

def inserir():
    """
    Função para inserir um usuário
    conn -> Usa a função conectar para iniciar a conecxão com o banco de dados
    db -> Inicia a conexão com o banco, e mostra com qual banco vamos trabalhar
    """  
    conn = conectar()
    db = conn.ProjetoGrafico

# Inicializa um objeto pessoa para podermos trabalhar e enviar ao banco de dados
    # Usar um dicionário para fazer isto
    nome = input('Informe o nome do usuário: ')
    trabalhoFuncao = input('Informe sua função que exerce no trabalho: ')
    trabalhoHorarioInicial = int(input('Informe a hora que ele entra no trabalho: '))
    trabalhoHorarioFinal = int(input('Informe a hora que ele sai do trabalho: '))
    
    estudos = input(f'Informe a área de estudos de {nome}: ')
    estudosHorarioInicial = input('Informe a hora que ele começa os estudos: ')
    estudosHorarioFinal = input('Informe a hora que ele para os estudos: ')
    
  
    # Rever momento, talvez fazer só a inserção do trabalho e dos estudos
    try:
        db.Pessoa.insert_one(
            {
                "Nome": nome,
                "Trabalho":{
                    "Funcao": trabalhoFuncao,
                    "Horario":{
                        "Inicial":trabalhoHorarioInicial,
                        "Final":trabalhoHorarioFinal
                    }
                },
                "Estudos":{
                    "Curso": estudos,
                    "Horario":{
                        "Inicial":estudosHorarioInicial,
                        "Final":estudosHorarioFinal
                    }
                },
            }
        )
        print(f'A pessoa foi adicionada!')
    except erros.PyMongoError as e:
        print(f'Não foi possível adicionar a pessoa! Algo aconteceu :( ->  {e}')
    desconectar(conn)

def atualizar():
    """
    Função para atualizar uma Pessoa
    """
    conn = conectar()
    db = conn.ProjetoGrafico

# Inicializa um objeto pessoa para podermos trabalhar e enviar ao banco de dados
    # Usar um dicionário para fazer isto
    _id = input('Informe o ID da pessoa: ')
    nome = input('Informe o nome do usuário: ')
    trabalhoFuncao = input('Informe sua função que exerce no trabalho: ')
    trabalhoHorarioInicial = int(input('Informe a hora que ele entra no trabalho: '))
    trabalhoHorarioFinal = int(input('Informe a hora que ele sai do trabalho: '))
    
    estudos = input(f'Informe a área de estudos de {nome}: ')
    estudosHorarioInicial = input('Informe a hora que ele começa os estudos: ')
    estudosHorarioFinal = input('Informe a hora que ele para os estudos: ')

    try:
        if db.Pessoa.count_documents({}) > 0:
            res = db.Pessoa.update_one(
                {"_id": ObjectId(_id)},
                {
                    "$set":{
                        "Nome": nome,
                        "Trabalho":{
                            "Funcao": trabalhoFuncao,
                            "Horario":{
                                "Inicial":trabalhoHorarioInicial,
                                "Final":trabalhoHorarioFinal
                            }
                        },
                        "Estudos":{
                            "Curso": estudos,
                            "Horario":{
                                "Inicial":estudosHorarioInicial,
                                "Final":estudosHorarioFinal
                            }
                        }
                    }
                }
            )
            if res.modified_count == 1:
                print(f'A pessoa {nome} foi atualizada com sucesso.')
            else:
                print(f'Não foi possível atualizar os dados de {nome}')
        else:
            print(f'Não existem pessoas para serem atualizados')
    except erros.PyMongoError as e:
        print(f'Não foi possível se conectar com a pessoa: {e}')
    except berros.InvalidId as f:
        print(f'Object ID inválido: {f}')
    desconectar(conn)

def nova_atividade():
    conn = conectar()
    db = conn.ProjetoGrafico

    nome = input('Informe o nome do usuário: ')

    momento = input(f"O que o {nome} está fazendo agora? ")
    data = datetime.today().strftime('%d/%m/%Y')
    momentoHorarioInicial = int(input(f"Desde que horas ele está executando esta ação? "))
    momentoHorarioFinal = int(input(f"Em que horas ele vai terminar esta ação? "))

    try:
        db.Pessoa.update_one(
            {"Nome": "José"},
            {"$push":
                {
                    "Fazendo":{
                    "Momento":momento,
                    "Horario":{
                        "Data": data,
                        "Inicial":momentoHorarioInicial,
                        "Final":momentoHorarioFinal
                        }
                    }
                }
            }
        )
        print(f'A pessoa foi adicionada!')
    except erros.PyMongoError as e:
        print(f'Não foi possível adicionar a pessoa! Algo aconteceu :( ->  {e}')
    desconectar(conn)

def deletar():
    """
    Função para deletar uma Pessoa
    """  
    conn = conectar()
    db = conn.ProjetoGrafico
    _id = input('Informe o ID da pessoa: ')
    try:
        if db.Pessoa.count_documents({}) > 0:
            res = db.Pessoa.delete_one(
                {
                    "_id": ObjectId(_id)
                }
            )
            if res.deleted_count > 0:
                print('Pessoa deletada com sucesso')
            else:
                print('Não foi possível deletar a pessoa')
        else:
            print('Não possuem pessoas para serem deletadas')
    except erros.PyMongoError as e:
        print(f'Não foi possível indentificar a pessoa: {e}')
    except berros.InvalidId as f:
        print(f'Object ID inválido: {f}')
    desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Criação de Gráfico de Pessoas pelo horário==============')
    print('Selecione uma opção: ')
    print('1 - Listar as Pessoas.')
    print('2 - Inserir novas Pessoas.')
    print('3 - Inserir nova atividade.')
    print('4 - Atualizar informações de alguém.')
    print('5 - Deletar alguém.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4, 5]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            nova_atividade()
        elif opcao == 4:
            atualizar()
        elif opcao == 5:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
