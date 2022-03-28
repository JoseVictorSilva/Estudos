from models.Calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado: (1, 2, 3, 4) '))
    calc: Calcular = Calcular(dificuldade)
    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pts')
    continuar: int = int(input('Deseja continuar no jogo? (1 - Sim / 2 - Não) '))
    if continuar == 1:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pts')
        print('Até a próxima')

if __name__ == '__main__':
    main()