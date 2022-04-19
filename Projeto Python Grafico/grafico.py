import matplotlib.pyplot as plt
from cadastraBanco import *
from pymongo import MongoClient, errors
from bson.objectid import ObjectId

def pega_dados():
    conn = conectar()
    db = conn.ProjetoGrafico
    try:
        if db.Pessoa.count_documents({}) > 0:
            pessoas = db.Pessoa.find(
                {"Nome":"José"},
                {"_id":0, "Fazendo":1}
            )
            print('Listando Momentos...')
            print('--------------------')
            i = 0
            for pessoa in pessoas:
                for i in range(len(pessoa['Fazendo'])):
                    a = list(pessoa['Fazendo'][i].values())
                    print(f"Fazendo: {a[1].values()}")
                    print('----------------------')
        else:
            print('Não existem pessoas cadastrados')
    except errors.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')
    desconectar(conn)

if __name__ == '__main__':
    pega_dados()
