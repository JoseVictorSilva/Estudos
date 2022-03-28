"""
    Métodos de Data e Hora
"""

import datetime
import functools
import timeit
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

agora = datetime.datetime.now() # agora em uma região, da pra especificar
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today() # aqui não da pra especificar
print(agora)
print(type(agora))
print(repr(agora))

manutencao = datetime.datetime.combine((datetime.datetime.now()+datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
print(manutencao.weekday()) # Que dia da semana estamos

aniversario = '09/06/2001'#input(' Qual sua data de nascimento? dd/mm/yyy ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]),month=int(aniversario[1]),day=int(aniversario[0]))
diaSemana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo']
print(f'Você nasceu em: {aniversario} em uma {diaSemana[aniversario.weekday()]}')

hoje_formatado = hoje.strftime('%d/%m/%Y') # B - mês inteiro, %b - mês primeiras letras, %y - dois digitos do ano
print(hoje_formatado)
print(formata_data(hoje))

nascimento = datetime.datetime.strptime('1/04/1998', '%d/%m/%Y')
print(nascimento)

almoco = datetime.time(12,30,0)
print(almoco)

# Tempo de execução

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) # 0.1191924000158906
print(tempo)

# List
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000) # 0.09955469996202737
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000) # 0.09890540002379566
print(tempo)

def teste(n):
    soma = 0
    for num in range(n*200):
        soma += num ** 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number = 10000)) # 0.7824034000514075 partial -> executa a funcao com x parametro

