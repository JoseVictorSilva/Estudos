import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

base_casas = pd.read_csv('ArquivosBase/house_prices.csv')

X_casas = base_casas.iloc[:,5:6].values
print(f'X: {X_casas}')
y_casas = base_casas.iloc[:,2].values
print(f'Y: {y_casas}')

# 30% para testar, 70% para treinar
X_casas_treinamento, X_casas_teste, y_casas_treinamento, y_casas_teste = train_test_split(X_casas, y_casas,test_size=0.3, random_state=0)
print(f'Treinamento X: {X_casas_treinamento.shape}')
print(f'Treinamento Y: {y_casas_treinamento.shape}')
print(f'Teste X: {X_casas_teste.shape}')
print(f'Teste Y: {y_casas_teste.shape}\n')

regressor_simples_casas = LinearRegression()
regressor_simples_casas.fit(X_casas_treinamento, y_casas_treinamento)
print(f'B0: {regressor_simples_casas.intercept_}')
print(f'B1: {regressor_simples_casas.coef_}')
print(f'Accuracy: {regressor_simples_casas.score(X_casas_treinamento,y_casas_treinamento)}')

previsoes = regressor_simples_casas.predict(X_casas_treinamento)
# grafico = px.scatter(x = X_casas_treinamento.ravel(), y = previsoes)
# grafico1 = px.scatter(x = X_casas_treinamento.ravel(), y = y_casas_treinamento)
# grafico2 = px.line(x = X_casas_treinamento.ravel(), y=previsoes)
# grafico2.data[0].line.color = 'red'
# grafico3 = go.Figure(data= grafico1.data + grafico2.data)
# grafico3.show()

# REGRESSÃO 2
previsoes_teste = regressor_simples_casas.predict(X_casas_teste)
print(previsoes_teste,'\n')
subtracao = abs(y_casas_teste - previsoes_teste).mean()
print(f'Subtração: {subtracao}')
print(f'Mean Absolute: {mean_absolute_error(y_casas_teste, previsoes_teste)}')
print(f'Mean Squared: {mean_squared_error(y_casas_teste, previsoes_teste)}')

grafico1 = px.scatter(x = X_casas_teste.ravel(), y = y_casas_teste)
grafico2 = px.line(x = X_casas_teste.ravel(), y=previsoes_teste)
grafico2.data[0].line.color = 'red'
grafico3 = go.Figure(data= grafico1.data + grafico2.data)
grafico3.show()

# print(base_casas)
# print(base_casas.describe())
# print(base_casas.isnull().sum())
# print(base_casas.corr())
# figura = plt.figure(figsize=(20,20)) # na figura podemos que alguns atributos impactam mais que outros, banheiro por exemplo impacta mais que quarto no preço
# sns.heatmap(base_casas.corr(), annot= True)
# plt.show()