'''
    Docstrings é a documentação
'''
def diz_oi():
    '''Uma função simples que retorna a string 'Oi!' '''
    return 'Oi!'

def exponencial(numero,potencia = 2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou/e a 'potencia';
    :param numero: Número que queremos gerar o exponencial;
    :param potencia: Número que é a potencia do numero;
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(diz_oi())
print(diz_oi.__doc__) # retorna a documentação de uma função
print(exponencial.__doc__)
