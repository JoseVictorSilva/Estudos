from email.mime import base
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credits = pd.read_csv('./Arquivos Base/credit_data.csv')
base_credits.loc[base_credits['age'] < 0, 'age'] = 40.92
base_credits['age'].fillna(base_credits['age'].mean(), inplace = True)

X_credit = base_credits.iloc[:,1:4 ].values
print('============== Todas as Linhas da Primeira Coluna: ============== ')
print(X_credit[:,0],'\n')
print('================ Maior Renda: ================ ')
print(X_credit[:,0].max(),'\n')
print('================ Menor Renda: ================ ')
print(X_credit[:,0].min(),'\n')

print('============ Maior Renda e Idade: ============ ')
print(f'Renda: {X_credit[:,0].max()} \nIdade: {X_credit[:,1].max()} \n')
print('============ Menor Renda e Idade: ============ ')
print(f'Renda: {X_credit[:,0].min()} \nIdade: {X_credit[:,1].min()}\n')

print('============ Maior Renda, Idade e Dívida: ============ ')
print(f'Renda: {X_credit[:,0].max()} \nIdade: {X_credit[:,1].max()} \nDívida: {X_credit[:,2].max()} \n')
print('============ Menor Renda, Idade e Dívida: ============ ')
print(f'Renda: {X_credit[:,0].min()} \nIdade: {X_credit[:,1].min()} \nDívida: {X_credit[:,2].min()} \n')

Y_credit = base_credits.iloc[:,4].values
print('===================== Y: ===================== ')
print(Y_credit,'\n')

# HORA DO SHOW
# O problema de ter atributos distoantes (por exemplo renda que chega a 63 mil), é que o algoritmo pode entender um valor de importância maior
# Inicia um objeto 'scaler_credit' e passa como parametro em fit_transform o X_credit, para que os valores não possuam um desvio alto
scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)
print('============ Maior Renda, Idade e Dívida: ============ ')
print(f'Renda: {X_credit[:,0].max()} \nIdade: {X_credit[:,1].max()} \nDívida: {X_credit[:,2].max()} \n')
print('============ Menor Renda, Idade e Dívida com transformação: ============ ')
print(f'Renda: {X_credit[:,0].min()} \nIdade: {X_credit[:,1].min()} \nDívida: {X_credit[:,2].min()} \n')
