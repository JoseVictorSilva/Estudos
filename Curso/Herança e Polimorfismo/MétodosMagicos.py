"""
    Métodos Mágicos

- Todos os que utilizam dunder (__)

"""
from numpy import isin


class Livro:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self): #Existe o __str__ que faz o mesmo mas transforma o retorno em string
        return self.titulo
    def __repr__(self):
        return f'O livro {self.titulo} será escrito por {self.autor}'
    def __len__(self):
        return self.paginas
    def __add__(self,outro):
        return f'{self} - {outro}'
    def __mul__(self,outro):
        if isinstance(outro,int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'
    def __del__(self):
        print('Um objeto do tipo livro foi deletador da memória')
l1 = Livro('Teste1', 'Autor1', 100)
l2 = Livro('Teste2', 'Autor2', 200)

print(f'__repr__/__str__: {l1}') # Agora imprime o título colocado por cauda do repr
print(f'__len__: {len(l1)}')
print(f'__add__: {l1 + l2}')
print(f'__mul__: {l1 * 4}') 
del(l1)
print(l1)

