"""
    Forçando tipos de dados com decoradores

a = (1,2,3)
b = (4,5,6)
c = zip(a,b)
c = (1,2),(3,4),(5,6)
"""
def forca_tipo(*tipos): # args, Em tipos vai entrar o tipo str e int
    def decorador(funcao): # Aqui a funcao repete_msg
        def converte(*args,**kwargs): # Mensagem e Quantidade(4)
            novo_args =[]
            for(valor,tipo) in zip(args,tipos): # Pra cada Valores: mensagem('oi') e quantidade(4) e tipos(str,int)
                novo_args.append(tipo(valor)) # Adicione em novo_args o valor convertido, forçando ele a ser o str primeiro depois int
            return funcao(*novo_args,**kwargs) # Retorna a execução da função com mensagem('oi') e quantidade(4)
        return converte
    return decorador

@forca_tipo(str,int)
def repete_msg(msg,vezes):
    for vez in range(vezes):
        print(msg, end=' ')

@forca_tipo(float,float)
def dividir(a,b):
    print(a/b)

repete_msg("oi",'4')
print()
dividir(6,3)