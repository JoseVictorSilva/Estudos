"""
    Leitura de Arquivos
- Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que é o nome do arquivo
que vai retornar um _io.TextIOWrapper, que é o que trabalhamos

Erro: FileNotFoundError
"""

arquivo = open('texto.txt', 'r')
print(arquivo)
print(type(arquivo))
