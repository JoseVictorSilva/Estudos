from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
base_risco_credito = pd.read_csv('../Arquivos Base/risco_credito.csv')

X_risco_credito = base_risco_credito.iloc[:,0:4].values
print('======= X RISCO CRÉDITO =======')
print(X_risco_credito,'\n') # Valores dos risco
Y_risco_credito = base_risco_credito.iloc[:,4].values
print('======= Y RISCO CRÉDITO =======')
print(Y_risco_credito,'\n') # O risco dos valores

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantias = LabelEncoder()
label_encoder_renda = LabelEncoder()

# Como a base de dados é pequena, não precisa do OneHotEncoder
X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantias.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print('======= X RISCO CRÉDITO NUMÉRICO =======')
print(X_risco_credito)

with open('../Arquivos Base/risco_credito.pkl','wb') as f:
    pickle.dump([X_risco_credito,Y_risco_credito], f)

naive_risco_credito = GaussianNB() # Criando Naive Bayes
naive_risco_credito.fit(X_risco_credito, Y_risco_credito) # Transforma o X e o Y para se ENCAIXAR na tabela de naive bayes
print(f'Classes: {naive_risco_credito.classes_}')
print(f'Classes qtd: {naive_risco_credito.class_count_}')
print(f'Classes a Priori: {naive_risco_credito.class_prior_},\n')
# História boa = 0; desconhecia = 1; ruim = 2
# Dívida alta = 0; baixa = 1;
# Garantia adequada = 0; nenhuma = 1
# Renda 0_15 = 0; 15_35 = 1; acima_35 = 2

# História boa(0), dívida alta(0), garantia nenhuma(1), renda > 35(2) -> resultado é baixo
# História ruim(2), dívida alta(0), garantia adequada(0), renda < 15(0) -> resultado moderado
previsao = naive_risco_credito.predict([[0,0,1,2],[2,0,0,0]]) # Faz os calculos com Navie Bayes e retorna a classe
print(f'Previsão: {previsao}')