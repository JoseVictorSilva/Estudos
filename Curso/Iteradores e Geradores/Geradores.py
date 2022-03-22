"""
    Geradores

- Geradores (Generators) são Iteradores
    Exemplo
    - Generatos podem ser criados com funções geradoras;
    - Funções geradoreas utilizam a plavra reservada yield;
    - Generators podem ser criados com expressões Geradoras;

Diferença entre Funções e Generator Functions:
___________________________________________________________________________
|             Funções               |         Generator Functions          |
| Utilizam Return                   | Utilizam yield                       |
| Retorna uma vez                   | Podem utilizar yield múltiplas vezes |
| Quando executada retorna um valor | Retorna um generator                 |
"""

# Generator Function não é um generator, ela gera um generator
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(5)
print(list(gen)) # poderia printar nex(gen) em vez de list/tuple e afins
"""for num in gen:
    print(num)"""