"""
    Iterador Customizado

"""

from tracemalloc import start


for n in range(11):
    print(n,' ',end='')

class Contador:
    # Método Construtor
    def __init__(self,menor,maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
con = Contador(1,6)
print('\n')
it = iter(con)

print(next(con))
print(next(it))
print(next(con)) # Estou mexendo com o mesmo objeto

"""for n in Contador(1,61):
    print(n)"""