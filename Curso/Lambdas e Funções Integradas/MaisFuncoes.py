"""
    Len, Abs, Sum, Round
# Len: Retorna o tamanho (número de itens) de um iterável
# Abs: Retorna o valor absoluto de um número. Ou seja, seu valor real sem o sinal
# Sum: Soma valores
# Round: Arredonda valores
"""
# Len faz isso:
print('José Victor'.__len__()) # Dunder len -> qualquer funcao que tenha .__nome__() 
print(abs(-5))
print(sum((1,2,3,4,5,9)))
print(sum((1,2,3,4,5,9),-5))
print(round(12.26785,3))