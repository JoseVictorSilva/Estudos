"""
    Trabalhando com deltas de data e hora

    delta = data final - data inicial
"""

import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2023,3,3,0)
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
print(f'Faltam: {tempo_para_evento.days} dias, {tempo_para_evento.seconds//60//60} horas')