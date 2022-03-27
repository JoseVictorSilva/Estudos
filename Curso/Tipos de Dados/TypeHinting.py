from numpy import integer


def cumprimentar(nome: str) -> str: # Ele espera string e vai retornar -> string
    return {nome}
def inteito(esp: int) -> int:
    return esp

print(cumprimentar('José'))
esp = inteito(cumprimentar('a'))
print(esp)

def cabecalho(texto: str,alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')

print(cabecalho('José Victor'))
print(cabecalho('José Victor', alinhamento = False))
print(cabecalho('José Victor', alinhamento = 'zé')) # String é True