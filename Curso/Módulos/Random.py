"""
    Módulos e o que são
- Em Python, módulos são nada mais nada menos que outros arquivos de Python
- Módulo Random -> Possui várias funções para geração de números pseudo-aleatório

OBS: Existem duas formas de usar um módulo/função deste
"""

# Forma 1 - Importando todo o módulo
import random as r
for i in range(10):
    print(round(r.random(),2))

print(round(r.uniform(3,7),2)) # entre 3 e 7