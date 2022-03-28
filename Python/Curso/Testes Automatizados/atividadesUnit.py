def comer(comida,saudavel):
    if saudavel == True:
        vida = 'quero manter a forma'
    else: 
        vida = 'só vivemos uma vez'
    return f'Estou comendo {comida} porque {vida}'
def dormir(num_horas):
    if num_horas > 8:
        return 'Estou atrasado pro trabalho'
    return 'Estou cansado pro trabalho :('
