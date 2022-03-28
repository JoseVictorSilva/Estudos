"""
    Dunder Name e Dunder Main
- Dunder -> Double Under
- Name -> __name__
- Main -> __main__

 É utilizado para a criação de funções/atributos/propriedades para não gerar conflitos
"""
# Basicamente só executa o código se ele estiver sendo executado, isso garante que quando for importado, não execute código a mais
if __name__ == '__main__':
    print('oi')