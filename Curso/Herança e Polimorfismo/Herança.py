"""
    POO - Herança

- A ideia de herança é a de reaproveitar código. Também extender nossas classes. 


"""
class Pessoa:
    def __init__(self, nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa): # Esta herdando Pessoa
    def __init__(self,nome,sobrenome,cpf,renda):
        super().__init__(nome,sobrenome,cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    def __init__(self,nome,sobrenome,cpf,matricula):
        super().__init__(nome,sobrenome,cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'{self._Pessoa__nome} {self._Pessoa__sobrenome} matricula: {self.__matricula}' # Sobrescrever

cliente1 = Cliente('José','Nogueira',12345678910,2000)
funcionario1 = Funcionario('Thiago','Lima',12345678910,555)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
    