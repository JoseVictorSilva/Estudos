"""
    Manipulando Data e Hora

- Python tem o modo built-in pra trabalhar com data e hora chamado datetime
"""
import datetime

print(f'Data máxima: {datetime.MAXYEAR}')
print(f'Data mínima: {datetime.MINYEAR}')
print(f'Hora atual: {datetime.datetime.now()}') # datetime(módulo).datetime(classe).now(método)
print(f'Hora atual: {repr(datetime.datetime.now())}') # Alterando o formato que essa classe retorna

inicio = datetime.datetime.now()
print(inicio)

inicio = inicio.replace(hour = 16, minute = 0, second = 0, microsecond = 0) # Colocando novos valores
print(inicio)

# Criando
evento = datetime.datetime(2019,1,1,0)
print(f'Evento: {evento}')
nascimento = input('Informe sua data de nascimento: (dd/mm/yyyy) ')
nascimento = nascimento.split('/')
print(nascimento)

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]),int(nascimento[0]) )
print(nascimento)
