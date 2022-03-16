"""
    Bloco With
- O bloco with é utilizado para criar um contexto de trabalho onde os recursos
são fechados após o bloco with
"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.close())

print(arquivo.closed())