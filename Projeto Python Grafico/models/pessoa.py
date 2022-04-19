class Pessoa:
    contador: int = 1

    def __init__(self: object, nome: str, 
    trabalhoFuncao: str, trabalhoHorarioInicial: int, trabalhoHorarioFinal: int,
    estudos: str, estudosHorarioInicial: int, estudosHorarioFinal: int) -> None:
        self.__codigo: int = Pessoa.contador
        self.__nome: str = nome
        self.__trabalhoFuncao: str = trabalhoFuncao
        self.__trabalhoHorarioInicial: int = trabalhoHorarioInicial
        self.__trabalhoHorarioFinal: int = trabalhoHorarioFinal
        self.__estudos: str = estudos
        self.__estudosHorarioInicial: int = estudosHorarioInicial
        self.__estudosHorarioFinal: int = estudosHorarioFinal
        Pessoa.contador += 1

    @property
    def codigo(self: object)->int:
        return self.__codigo
    @property
    def nome(self: object)->str:
        return self.__nome 

    @property
    def trabalhoFuncao(self: object)->str:
        return self.__trabalhoFuncao
    @trabalhoFuncao.setter
    def trabalhoFuncao(self,novo_trabalho):
        self.__trabalhoFuncao = novo_trabalho 

    @property
    def trabalhoHorarioInicial(self: object)->int:
        return self.__trabalhoHorarioInicial
    @trabalhoHorarioInicial.setter
    def trabalhoHorarioInicial(self,novo_horario_inicial):
        self.__trabalhoHorarioInicial = novo_horario_inicial 

    @property
    def trabalhoHorarioFinal(self: object)->int:
        return self.__trabalhoHorarioFinal
    @trabalhoHorarioFinal.setter
    def trabalhoHorarioFinal(self,novo_horario_final):
        self.__trabalhoHorarioFinal = novo_horario_final

    @property
    def estudos(self: object)->str:
        return self.__estudos
    @estudos.setter
    def estudos(self,novo_estudo):
        self.__estudos = novo_estudo

    @property
    def estudosHorarioInicial(self: object)->int:
        return self.__estudosHorarioInicial
    @estudosHorarioInicial.setter
    def estudosHorarioInicial(self,novo_horario_inicial):
        self.__estudosHorarioInicial = novo_horario_inicial

    @property
    def estudosHorarioFinal(self: object)->int:
        return self.__estudosHorarioFinal
    @estudosHorarioInicial.setter
    def estudosHorarioInicial(self,novo_horario_inicial):
        self.__estudosHorarioInicial = novo_horario_inicial
    
    def __str__(self)->str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nTrabalho: {self.trabalhoFuncao} -> {self.trabalhoHorarioInicial}:{self.trabalhoHorarioFinal}'





