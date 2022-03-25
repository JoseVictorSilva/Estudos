"""
    Lendo CSV

- CSV -> Comma Separeted Values - Valores Separados por Vírgula

1, 2, 3, 4, 5


"""

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split()
    print(dados)