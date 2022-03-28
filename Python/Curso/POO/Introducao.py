"""
    Programação Orientada a Objetos - POO
     
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributo -> Caracteristicas do Objeto;
- Método -> Comportamento do objeto (funções);
- Construtor -> Método pra criar objetos com caracteristicas obrigatórias;
- Objeto -> Instância da classe;
"""

numero = 10
nome = 'José'

class Produto: # Classe Produto
    pass # Sem métodos ou atributos na classe produto

ps4 = Produto() #Produto() é o Construtor (padrão), e ps4 o Objeto

print(ps4)
print(type(ps4))