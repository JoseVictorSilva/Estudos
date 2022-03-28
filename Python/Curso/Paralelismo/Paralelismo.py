from datetime import datetime
import threading
from time import time

from numpy import number

class nossaThread(threading.Thread):
    def __init__(self,idt,nome):
        threading.Thread.__init__(self)
        self.idt = idt
        self.nome = nome
    
    def run(self):
        print(f'Iniciando a Thread {self.nome}')
        procThread(self.nome)
        print(f'Finalizando a Thread {self.nome}')
    
def procThread(nome):
    cont = 0
    while cont < 1000:
        #print(f'Processo {cont} da Thread {nome}') 
        cont+=1

thread1 = nossaThread(1,'t1')
thread2 = nossaThread(2,'t2')

arrThread = []
arrThread.append(thread1)
arrThread.append(thread2)

tempo = time()
thread1.run()
thread2.run()
tempo2 = time()

"""for t in arrThread:
    t.join()
    print('A: ', t)"""

print(f'Fim do programa {tempo2 - tempo} ')
