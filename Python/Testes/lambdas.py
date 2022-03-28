'''
funcao = lambda x,y: x * y
print(funcao(4,2))  

imprime = lambda texto: print(f'{texto} é muito bom')
imprime('testar')

# Exercicio 1
def resultadoMedia(media):
    if(media < 5): print('D')
    if(media < 7 and media >= 5): print('C')
    if(media < 9 and media >= 7): print('B')
    if(media == 10): print('A')
notas = lambda nota1,nota2: (nota1*0.4)+(nota2*0.6)

for n in range(2):
    nome = input('Entre com o Nome: ')
    nota1 = float(input('Entre com a primeira nota: '))
    nota2 = float(input('Entre com a segunda nota: '))
    print(f'O aluno {nome} ficou com a seguinte média: {(notas(nota1,nota2))}, sua situação foi de {resultadoMedia(notas(nota1,nota2))}')'''

a, b, c = "a", "b", "c"
data1 = {(1, a): 28, (1, c): 57, (2, b): 125}
total = list()

spot = 0 
for d in data1:
    print(d[1])
    total.append(list(d[1])) # Add new Lists to list "total" containing the Key values
    total[spot].append(data1[d]) # Add Values to Keys judging from their spot in the list
    spot += 1 # to keep the spot in correct place in lists

print(total)
total = dict(total) # convert it to dictionary
print(total)