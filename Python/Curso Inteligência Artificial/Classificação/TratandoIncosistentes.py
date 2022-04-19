from email.mime import base
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Testes com pandas
base_credits = pd.read_csv('./Arquivos Base/credit_data.csv')
#print(base_credits.head(10)) # Mostra os 10 primeiros
#print(base_credits.describe()) # Mostra todos os dados, maiores menos, % e afins
#print(base_credits[base_credits['income']>=69995.685578]) # Mostra o que tiver maior que o número em income
#print(base_credits[base_credits['loan']<= 1.377630 ]) 

print(np.unique(base_credits['default'], return_counts=True)) # Sem o return_counts, ele retorna a variação dos dados (0 e 1)
plt.xlabel("Situação")
plt.ylabel("Pessoas")

#sns.countplot(x = base_credits['default']) # Mostra o gráfico de pessoas em default
#plt.hist(x = base_credits['age'])
#plt.hist(x = base_credits['income'])
#plt.hist(x = base_credits['loan'])
#plt.show()

# Vai gerar gráficos cruzando age income e loan, a cor será a variação de default
grafico = px.scatter_matrix(base_credits,dimensions=['age','income', 'loan'], color = 'default') 
grafico.show()

#print(base_credits[base_credits['age']<0]) # Mostra idades menores que 0
print(base_credits.loc[base_credits['age']<0]) # Mostra idades menores que 0

# Apagar a coluna inteira
#base_credits.drop('age',axis = 1)

# Apagar os registros com valores inconsistentes
base_credits3 = base_credits.drop(base_credits[base_credits['age'] < 0].index) # Dropa o index que são menores que 0
print(base_credits3.loc[base_credits['age']<0]) # Mostra idades menores que 0

print(base_credits['age'].mean()) # Média de idade
print(base_credits['age'][base_credits['age'] > 0].mean()) # Média com números maiores que 0

base_credits.loc[base_credits['age'] < 0, 'age'] = 40.92 # Coloca o valor 40.92 nas idades menores que 0
print(base_credits.loc[base_credits['age']<0])
print(base_credits.head(27))

