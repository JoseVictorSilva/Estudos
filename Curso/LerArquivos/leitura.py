"""
    Leitura de Arquivos
- Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que é o nome do arquivo
que vai retornar um _io.TextIOWrapper, que é o que trabalhamos

Erro: FileNotFoundError

mode: 'r' -> reading
"""

arquivo = open('teste.txt')
print(arquivo)
print(type(arquivo))
# Para ler o arquivo
print(arquivo.read()) # Lê todo o conteudo

# O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor
# funciona como o cursor de quando escrevemos