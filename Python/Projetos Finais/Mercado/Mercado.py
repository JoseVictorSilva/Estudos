from typing import * # Importa as tipações List, Dict e afins
from time import sleep 
from models.Produto import Produto # Importa a classe Produto dentro da pasta models
from utils.Helper import formata_float_str_moeda # Importa a classe formata_float_str_moeda dentro da pasta utils

produtos: List[Produto] = [] # Cria uma lista que só aceita dados de Produto
carrinho: List[Dict[Produto,int]] = [] # Cria uma LISTA de DICIONÁRIO, em que as chaves deste serão {'Produto': Quantidade}

def main() -> None:
    menu()

def menu() -> None:
    # Menu
    print('==================================')
    print('========== BEM-VINDO(a) ==========')
    print('==========   Zé Shop    ==========')
    print('==================================\n')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input(''))

    if opcao == 1:
        cadasatrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre...')
        exit(42)
    else:
        print('Não entendi a opção')
        menu()

def cadasatrar_produto() -> None:
    # Inicia o cadastro de produtos
    print('Cadastro de Produto')
    print('===================')
    # Informe o produto e seu preço
    nome: str = input('Informe o nome do Produto: ')
    preco: float = float(input('Informe o preço do Produto: '))
    # Inicializa um objeto produto do tipo Produto passando o nome e o preço anteriores e adiciona na Lista de PRODUTOS
    produto: Produto = Produto(nome,preco)
    produtos.append(produto)

    print('===================')
    print(f'O produto: {nome} foi adicionado com sucesso!')
    sleep(1)
    menu()

def listar_produto() -> None:
    # Lista os produtos existentes se tiver algum produto
    if len(produtos) > 0:
        for produto in produtos: # Para cada produto na Lista de PRODUTOS imprima 1 por 1
            print(produto)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados!')
    sleep(2)
    menu()

def comprar_produto() -> None:
    # Compra um produto caso existão
    if len(produtos)> 0:
        print('Informe o código do Produto que deseja adicionar ao carrinho: ')
        print('------------------------------------------------------------')
        print('=================== Produtos Disponíveis ===================')

        for produto in produtos: # Lista os produtos assim como na função listar_produto()
            print(produto)
            print('------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('')) # Adicione o código do produto que deseja obter

        produto: Produto = pega_produto_por_codigo(codigo) # Pega o produto pelo seu código
        # Se produto não for None e nem o carrinho for 0
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False # Inicia essa variavel se baseando que não possui o produto no carrinho para adiciona-lo
                # Para cada item no dicionário Carrinho
                for item in carrinho: 
                    quant: int = item.get(produto) # Pega pela chave(nome), a quantidade do produto
                    if quant: # Se a quantidade não for None
                        item[produto] = quant + 1 # Novamente pega pela chave a quantidade do produto e a adiciona
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True # Agora existe no carrinho
                        sleep(2)
                        menu()
                if not tem_no_carrinho: # Produto escolhido ainda não esta no carrinho
                    prod = {produto:1} # Adiciona a item o Produto com a quantidade 1
                    carrinho.append(prod) # Adiciona o carrinho
                    print(f'O produto {produto.nome} foi adicionado ao carrinho ')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1} 
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu() 
        else:
            print(f'O produto com o código {codigo} não foi encontrado')
        sleep(2)
    else: 
        print('Ainda não tem nenhum produto para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    # Mostra carrinho se tiver produto nele
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho: # Para cada item em carrinho
            for dados in item.items(): # Veja a chave do carrinho e jogue em dados
                print(dados[0]) # Mostre o Produto
                print(f'Quantidade: {dados[1]}')
                print('----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho!')
    sleep(2)
    menu()    

def fechar_pedido() -> None:
    # Fecha o pedido se tiver algo no carrinho
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos no carrinho: ')
        print('---------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * int(dados[1]) # Acessa o atributo preco do objeto e multiplica por sua quantidade
                print('---------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho!')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> None:
    # Pega o objeto produto pelo seu código
    p: Produto = None # Inicia um produto vazio
    for produto in produtos:
        if produto.codigo == codigo: # Se o código do produto for igual ao código passado, p será igual ao produto
            p = produto
    return p # Retorna o produto

if __name__ == '__main__':
    main()