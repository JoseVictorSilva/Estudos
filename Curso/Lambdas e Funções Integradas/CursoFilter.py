"""
    Filter
filter() -> Filtrar dados de uma determinada coleção
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

valores = 1.3,2.7,0.8,4.1,4.3,-0.1

media = sum(valores)/len(valores)
print(media)

# Dados coletados de algum sensor
dados = [1.3,2.7,0.8,4.1,4.3,-0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)
# OBS: Assim como a função map(), a filter() recebe dois parâmentros, sendo uma função e um iterável. 

res = filter((lambda valor: valor > media), dados)
print(res)
print(list(res))
print('Tipo: ',type(res))
print('Tipo: ',type(list(res)))
print(list(res),'\n') # O valor some assim como o Map
# Ele vai pegar cada um dos dados e passar como entrada da função em lambda valor:
# Então esse valor unico verá se é maior que a média, e passar como true ou false
# Sendo true vai pra res

# Remoção de Dados Faltantes

paises = ['', 'Brasil', '', 'Venezuela', '', '', 'Colombia', 'Equador']
print(paises)
res = filter(None ,paises) # Faz com que elimine os dados vazios, poderia ser filter(lambda pais : pais != '',paises)
print(list(res),'\n')

# Diferença entre map() e filter():
# Map() ->  Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável. 
# Filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um obejto filtrando apenas os elementos de acordo com a função
# Map() Retorna valor, Filter() Retorna Boolean que vai selecionar o valor

# Exemplos mais complexo
print('------ Exemplo Twitter -----')
usuarios = [
    {"username": "Samuel","tweets": ["Eu adoro bolos","Eu adoro pizza"]},
    {"username": "Carla","tweets": ["Eu amo meus gatos"]},
    {"username": "bob123","tweets": []},
    {"username": "doggo","tweets": ["Eu gosto de cachorros","Vou sair hoje"]},
    {"username": "dualdo","tweets": []}
]
print(usuarios)

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios ))
print('Usuários inativos: ',inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios ))
print('Usuários inativos usando not: ',inativos)
# Listas vazias, são dadas como falsas, então usuário que possui o valor tweet, ta vazio

# Combinando filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'Giulia']
# Devemos criar uma lista contendo 'Sua instrutora é:' + nome, desde que tenha menos de 5 caracteres

instrutora = list(map(lambda nomeInst: f'Sua instrutora é: {nomeInst}', filter(lambda nome: len(nome) < 5, nomes) ))
print(instrutora)
# Primeiro a lista NOMES entra em filter um por um, então Vanessa vai pra função lambda entrando na variavel NOME, e então é checado
# se seu tamanho é menor que 5, que no caso é falso
# Depois disso, o valor FALSO dado no filter vai para o map que pode receber qualquer tipo de dado, sendo assim, ele não fará nada
# No próximo valor de NOMES que seria ANA, ela vai passar por ter menos de 5 letras dando True, e então vai pro map em que ela será
# atribuida à nomeInst, então escrevendo o que ela é sua instrutora
# lembrando, o map() funciona da seguinte forma -> map(função, iterável), nesse caso map(funcaoLambda, booleanDoFilter)