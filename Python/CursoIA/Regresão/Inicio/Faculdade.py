import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

base_insurance = pd.read_csv('../ArquivosBase/insuranceCorrigido.csv')

X_insurance = base_insurance.iloc[:,0:5].values
print(f'X: {X_insurance}')
y_insurance = base_insurance.iloc[:,6].values
print(f'Y: {y_insurance}')

# 30% para testar, 70% para treinar
X_insurance_treinamento, X_insurance_teste, y_insurance_treinamento, y_insurance_teste = train_test_split(X_insurance, y_insurance,test_size=0.3, random_state=0)
print(f'Treinamento X: {X_insurance_treinamento.shape}')
print(f'Treinamento Y: {y_insurance_treinamento.shape}')
print(f'Teste X: {X_insurance_teste.shape}')
print(f'Teste Y: {y_insurance_teste.shape}\n')

regressor_simples_insurance = LinearRegression()
regressor_simples_insurance.fit(X_insurance_treinamento, y_insurance_treinamento)
print(f'B0: {regressor_simples_insurance.intercept_}')
print(f'B1: {regressor_simples_insurance.coef_}')
print(f'Accuracy: {regressor_simples_insurance.score(X_insurance_treinamento,y_insurance_treinamento)}')

previsoes = regressor_simples_insurance.predict(X_insurance_treinamento)
# grafico = px.scatter(x = X_insurance_treinamento.ravel(), y = previsoes)
# grafico1 = px.scatter(x = X_insurance_treinamento.ravel(), y = y_insurance_treinamento)
# grafico2 = px.line(x = X_insurance_treinamento.ravel(), y=previsoes)
# grafico2.data[0].line.color = 'red'
# grafico3 = go.Figure(data= grafico1.data + grafico2.data)
# grafico3.show()

# REGRESSÃO 2
previsoes_teste = regressor_simples_insurance.predict(X_insurance_teste)
print(previsoes_teste,'\n')
subtracao = abs(y_insurance_teste - previsoes_teste).mean()
print(f'Subtração: {subtracao}')
print(f'Mean Absolute: {mean_absolute_error(y_insurance_teste, previsoes_teste)}')
print(f'Mean Squared: {mean_squared_error(y_insurance_teste, previsoes_teste)}')

grafico1 = px.scatter(x = X_insurance_teste.ravel(), y = y_insurance_teste)
grafico2 = px.line(x = X_insurance_teste.ravel(), y=previsoes_teste)
grafico2.data[0].line.color = 'red'
grafico3 = go.Figure(data= grafico1.data + grafico2.data)
grafico3.show()

# print(base_insurance)
# print(base_insurance.describe())
# print(base_insurance.isnull().sum())
# print(base_insurance.corr())
# figura = plt.figure(figsize=(20,20)) # na figura podemos que alguns atributos impactam mais que outros, banheiro por exemplo impacta mais que quarto no preço
# sns.heatmap(base_insurance.corr(), annot= True)
# plt.show()