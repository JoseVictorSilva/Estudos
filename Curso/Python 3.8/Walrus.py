"""
    Walrus
- Ele permite fazer a atribuição e retorno de valor em uma única expressão
"""
# Antes
nome = 'José'
print(nome)

# Walrus
print(nome:= 'Victor')

# Antes
cesta = []
fruta = input('Informe a fruta: ')
while fruta!='sair':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

print(cesta)

# Agora
cesta = []
while (fruta:=input('Informe a fruta: ')) != 'sair':
    cesta.append(fruta)

print(cesta)