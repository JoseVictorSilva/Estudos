import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_absolute_error, mean_squared_error

base_casas = pd.read_csv('ArquivosBase/house_prices.csv')

X_casas = base_casas.iloc[:,3:19].values
print(f'X: {X_casas}')
y_casas = base_casas.iloc[:,2].values
print(f'Y: {y_casas}\n')

X_casas_treinamento, X_casas_teste, y_casas_treinamento, y_casas_teste = train_test_split(X_casas, y_casas,test_size=0.3, random_state=0)
print(f'Treinamento X: {X_casas_treinamento.shape}')
print(f'Treinamento Y: {y_casas_treinamento.shape}')
print(f'Teste X: {X_casas_teste.shape}')
print(f'Teste Y: {y_casas_teste.shape}\n')

regressor_multiplo_casas = LinearRegression()
regressor_multiplo_casas.fit(X_casas_treinamento, y_casas_treinamento)
print(f'B0: {regressor_multiplo_casas.intercept_}')
print(f'B1: {regressor_multiplo_casas.coef_}')
print(f'Accuracy: {regressor_multiplo_casas.score(X_casas_treinamento,y_casas_treinamento)*100}')
print(f'Accuracy Teste: {regressor_multiplo_casas.score(X_casas_teste,y_casas_teste)*100}\n')

previsao = regressor_multiplo_casas.predict(X_casas_teste)
print(f'Mean Absolute: {mean_absolute_error(y_casas_teste, previsao)}')
print(f'Mean Squared: {mean_squared_error(y_casas_teste, previsao)}')

print(f'Treinamento X: {X_casas_treinamento.shape}')
print(f'Treinamento Y: {y_casas_treinamento.shape}')
print(f'Teste X: {X_casas_teste.shape}')
print(f'Teste Y: {y_casas_teste.shape}')
print(f'Previsão: {previsao.shape}\n')

grafico1 = px.scatter(x = X_casas_teste, y = y_casas_teste.ravel())
grafico2 = px.scatter(x = y_casas_teste, y=previsao)
grafico2.data[0].line.color = 'red'
grafico3 = go.Figure(data=  grafico2.data)
grafico3.show()
