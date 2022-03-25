# Possível mas muito trabalhoso: 

"""with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)"""

# Opções: 
# reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
# DictRead -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

from csv import reader,DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pula o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)s {linha[1]} e mede {linha[2]}cm')

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    print(list(leitor_csv))
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)s {linha['Pais']} e mede {linha['Altura (em cm) ']}cm")

# Se não fosse virgula o separador seria assim: 
#     leitor_csv = DictReader(arquivo, delimiter = ';')
