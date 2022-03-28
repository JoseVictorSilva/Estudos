"""
    Raise
raise -> Lança exceções
"""
def colore(texto,cor):
    cores = ('Amarelo', 'Verde', 'Azul', 'Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser um String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')
    if cor not in cores:
        raise ValueError('A cor precisa ser uma entre: ',cores)

colore(" 'José' ",'vermelho')