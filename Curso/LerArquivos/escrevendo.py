"""
    Escrevendo
    
        arquivo.write('Um dia me perguntaram por que engordei tanto')
        arquivo.write('Mano, eu tô comendo dinheiro')
        arquivo.write('O capitão do meu time, não capitão do mato')
        arquivo.write('O capetão tá na curva com a caneta e o contrato, não assinei')
"""
# Caso alterar o texto, ele vai sobrescrever
with open('novo.txt','w') as arquivo:
    test = True
    while test == True:
        frase = input('Escreva algo: ')
        if frase == 'sair':
            test = False
        arquivo.write(frase + '\n')