"""
    POO - Atributos

- Atributos -> Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionlamente os estados de um obejto.add()

- Em Python, dividimos os atributos em 3 grupos:
        - Atributo de Instância
        - Atributo de Classe
        - Atributo de Dinâmico

- Atributo de Instância: São atributos dentro do método construtor
- Atributo de Classe: São atributos declarados diretamente na classe
- Atributo Dinâmico: Atributo de Instância que pode ser criado em tempo de execução (exclusivo da instância que o criou)

- Por convenção, todo atributo de uma classe é público, se quiser mudar pra privado
que só pode ser utilizado na própria classe, deve-se declarar com __
"""

from mimetypes import init


class Lampada:
    # Construtor/Método
    def __init__(self,voltagem,cor):
        self.voltagem = voltagem # __ significa que é private, então só na classe eu tenho acesso
        self.cor = cor
        self.ligada = False
        # O atributo voltagem do objeto Lampada vai receber voltagem

class Produto:
    contador = 0
    imposto = 1.05

    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)      
        Produto.contador = self.id

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha      

class Cervejaria:
    def __init__(cerveja, nome, gosto):
        cerveja.nome = nome
        cerveja.gosto = gosto

# Acesso privado
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha
    
    def mostra_email(self):
        print(self.__email)
    def mostra_senha(self):
        print(self.__senha)

user1 = Acesso('user@gmail.com','12345')
user2 = Acesso('user2@gmail.com','4325')
# print(user.email)  Não da pra acessar, AtributteError porque são privados 
print(user1._Acesso__email) # Não deveria mas da
user1.mostra_email()
user1.mostra_senha()
user2.mostra_email()
user2.mostra_senha()
print()

# Atributo de Classe
p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('VR', 'Video Game', 2100)
print('ID: ',p1.id,' Valor: ',p1.valor, 'Imposto: ',p2.imposto) # Pode-se fazer o acesso por Produto.imposto mas é incorreto
print('ID: ',p2.id,' Valor: ',p2.valor, ' Imposto: ',p2.imposto)

# Atributo Dinâmico
pd = Produto('Playstation 4', 'Video Game', 2300)
pd2 = Produto('VR', 'Video Game', 2100)
print('--- Atributo Dinâmico ---')
pd.peso = '1Kg'
print(f'Id: {pd.id}, Produto: {pd.nome}, Descrição: {pd.descricao}, Preço: {pd.valor}, Peso: {pd.peso}')
print(f'Id: {pd2.id}, Produto: {pd2.nome}, Descrição: {pd2.descricao}, Preço: {pd2.valor}, Peso: não tem peso, da erro :(\n')

del pd.peso
print(f'Id: {pd.id}, Produto: {pd.nome}, Descrição: {pd.descricao}, Preço: {pd.valor}, Peso: excluido')

#print(Produto.__dict__) mostra os atributos