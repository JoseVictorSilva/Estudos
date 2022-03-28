def cumprimenta(nome,/, mensagem = '1'): # Fala que o valor pode ser posicional, tudo que tiver antes da barrinha
    # Se colocar * todos depois tem que informar o parametro do tipo print(cumprimenta(parametro = x))
    return f'Olá {nome} {mensagem}'

print(cumprimenta('José','10'))
print(cumprimenta('José', '3')) 