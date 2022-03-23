"""
    POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. 

- Método de Instância
- Métodos de Classe

- Método dunder init (__init__) é um método que chamado de construtor
"""

import email
from passlib.hash import pbkdf2_sha256 as crypt


class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 4999
    def __init__(self,limite,saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0

    def __init__(self,nome,descricao,valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor     
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto"""
        return (int(self.__valor) * (100-porcentagem))/100

class Usuario:
    contador = 0

    @classmethod # usar quando não vou usar nenhum atributo de instancia tipo self
    def conta_usuario(cls):
        print(f'Temos: {cls.contador} usuários cadastrados') #cls é classe, então traduzindo, esta escrito Temos: Usuario.contador
   
    @staticmethod
    def definicao():
        return 'Faz nada'
   
    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000,salt_size=16)   
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
   
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
   
    def checa_senha(self,senha):
        if crypt.verify(senha,self.__senha):
            return True
        return False    
   
    def __gera_usuario(self):
        return self.__email.split('@')[0]
   
    def __correr__(self,metros): # Nunca criar um método com __metodo__
        print(f'{self.__nome} está correndo {metros}m')

def usuario(): 
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    email = input('Informe o email: ')
    senha = input('Informe a senha: ')
    confirma_senha = input('Confirme a senha: ')

    if senha == confirma_senha:
        user = Usuario(nome,sobrenome,email,senha)
    else: 
        print('Senha não confere...')
        exit(42)

    print('Usuário criado com sucesso!')
    senha = input('Informe a senha para acessar: ')

    if user.checa_senha(senha):
        print('Acesso Garantido!')
    else: 
        print('Acesso Negado!')

    print(f'Senha do usuário criptografada é: {user._Usuario__senha}')

p1 = Produto('Xbox','VideoGame', '2500')
print(p1.desconto(50))
print(Produto.desconto(p1,50))
user1 = Usuario('José Victor','Nogueira Alves da Silva', 'josevictorcomrc@gmail.com', '123456')
user2 = Usuario('Anna Caroline','Fidélis Conte Pereira', 'anninhaunderground@gmail.com', 'teste123')
print(user1.nome_completo())
print(user2.nome_completo())

print(f'Senha: {user1._Usuario__senha}') # forma errada
print(f'Senha: {user2._Usuario__senha}') # forma errada

Usuario.conta_usuario() # Forma correta
user1.conta_usuario() # Forma incorreta
print(user1._Usuario__gera_usuario()) # Forma errada
print(user1.definicao())