"""
    Criando Loops

"""

for num in [1,2,3,4,5]:
    print(num,' ',end='')
print('\n')
for letra in 'José Victor':
    print(letra,' ',end='')
print('\n')

# O loop for ta fazendo por de baixo dos panos um iter()
# Fazendo um loop
def meu_for(interavel):
    it=iter(interavel)
    while True:
        try:
            print(next(it),' ',end='')
        except StopIteration:
            break

meu_for([1,2,3,4])