import pywhatkit
import datetime
import random
from sometimes import sometimes

@sometimes
def lembrete():
    data = datetime.datetime.now()
    print(data.minute)
