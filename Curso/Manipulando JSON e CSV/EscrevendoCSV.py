"""
    Escrevendo em Arquivos CSV
- reader() -> Leitor
- writer() -> Escritor
- writerow() -> Escreve em uma linha
- DictWritter() -> Trabalha com dicionários
"""
from csv import writer, DictWriter

"""with open('filmes.csv','w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título','Gênero','Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do Filme: ')
        if filme != 'sair': 
            genero = input('Informe o Genêro: ')
            duracao = input('Informe a Duração: ')
            escritor_csv.writerow([filme, genero, duracao])
"""

with open('filmes.csv','w') as arquivo:
    cabecalho = ['Título','Gênero','Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do Filme: ')
        if filme != 'sair': 
            genero = input('Informe o Genêro: ')
            duracao = input('Informe a Duração: ')
            escritor_csv.writerow({'Título': filme, 'Gênero':genero, 'Duração': duracao})
