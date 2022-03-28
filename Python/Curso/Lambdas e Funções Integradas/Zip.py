"""
    Zip
zip() -> Cria um iterável Zip Object que agrega elemento de cada um dos iteráveis passados como entrada em pares. 
"""

lista1 = [1,2,3]
lista2 = [4,5,6]
zip1 = zip(lista1,lista2,'abc',(1,2,3,4))
print(zip1)
print(list(zip1)) # Depois dessa execução, ele para de existir
print(tuple(zip(lista1,lista2,'abc')))
print(set(zip(lista1,lista2,'abc'))) 
print(dict(zip(lista1,lista2))) #Dicionario não da pra passar 3

prova1 = [8,7,6]
prova2 = [4,6,9]
alunos = ['José','Eduardo','Thiago']
# Para cada dado no zip de (aluno,prova1,prova2) você vai jogar em dado, o dado[0] é aluno e ai mostra a maior nota dele
final = {dado[0]:max(dado[1],dado[2]) for dado in zip(alunos,prova1,prova2)}
print(dict(final))

# Zipa a prova1 e prova2, tira a maxima de cada uma e joga em nota, depois ele só atribui aos alunos suas maiores notas
final = zip(alunos, map(lambda nota: max(nota),zip(prova1,prova2)))
print(dict(final))
