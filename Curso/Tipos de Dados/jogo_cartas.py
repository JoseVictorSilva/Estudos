import random
from typing import  *

NAIPES = 'copas ouros paus espadas'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
CARTA = Tuple[str,str]
BARALHO = List[CARTA]

def cria_baralho(aleatorio: bool = False) -> BARALHO:
    baralho: BARALHO = [(c,n) for n in NAIPES for c in CARTAS ]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO,BARALHO,BARALHO,BARALHO]:
    return (baralho[0::4],baralho[1::4],baralho[2::4],baralho[3::4])

def jogar():
    cartas: BARALHO = cria_baralho(aleatorio = True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores,distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}-{c}" for (j,c) in cartas)
        print(f'{jogador} : {carta}')

if __name__ == '__main__':
    jogar()