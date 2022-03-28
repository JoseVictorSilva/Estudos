"""
    Dictionary Comprehension

    {chave:valor for valor in iteravel}
"""

numeros = {'a':(1,2),'b':(2,3),'c':(3,4),'d':(4,5)}
numeroLista = (1,2,3,4,5) # se tivesse repetissão de chave, iria pular na hora de converter
quadrado = {chave: valor **2 for chave, valor in numeros.items()}
print(quadrado)
quadrado = {valor: valor ** 2 for valor in numeroLista} # tranformando em dic, funciona com qualquer outro tipo de lista
print(quadrado)

# Criando dic

chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]: valores[i] for i in range(0,len(chaves))}
print(mistura)