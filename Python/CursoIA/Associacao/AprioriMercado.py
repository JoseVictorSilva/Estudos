import pandas as pd
from apyori import apriori

base_mercado1 = pd.read_csv('ArquivosBase/mercado.csv', header=None)
print(base_mercado1)

transacoes = []
for i in range(len(base_mercado1)):
    #print(base_mercado1.values[i,0])
    transacoes.append([str(base_mercado1.values[i,j]) for j in range(base_mercado1.shape[1])])

#item_base -> se compra café e manteiga
#item_add -> compra pão

# min_lift, regra que fala: se voce compra pão, voce compra pão
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.3, min_lift = 2)
resultados = list(regras)
print(resultados)

A = []
B = []
suporte = []
confianca = []
lift = []

for resultado in resultados:
    print(resultado)
    s = resultado[1]
    #suporte
    print(s)
    # regras
    result_rules = resultado[2]
    for result_rule in result_rules:
        print(result_rule)
        a = list(result_rule[0])
        b = list(result_rule[1])
        c = result_rule[2]
        l = result_rule[3]
        print(a,' - ',b,' - ',c,' - ',l)
        A.append(a)
        B.append(b)
        suporte.append(s)
        confianca.append(c)
        lift.append(l)

rules_df = pd.DataFrame({'A':A,'B':B,'suporte':suporte,'confianca':confianca,'lift':lift})
print(rules_df.sort_values(by='lift', ascending=False))

