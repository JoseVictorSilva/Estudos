import pandas as pd
from apyori import apriori

base_mercado2 = pd.read_csv('ArquivosBase/mercado2.csv', header=None)
print(base_mercado2)

transacoes = []
for i in range(base_mercado2.shape[0]):
    transacoes.append([str(base_mercado2.values[i,j]) for j in range(base_mercado2.shape[1])])

#print(transacoes)
# Produtos que são vendidos 4x por dia
# 4 * 7 = 28 -> 28/7501 = 0.003
regras = apriori(transacoes, min_support = 0.003, min_confidence = 0.2, min_lift = 3)
resultados = list(regras)
print(len(resultados))

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
print(rules_df.sort_values(by='lift', ascending=False).head(50))
