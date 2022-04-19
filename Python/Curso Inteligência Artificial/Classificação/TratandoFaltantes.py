from email.mime import base
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credits = pd.read_csv('./Arquivos Base/credit_data.csv')
# Mostra a somatória dos valores nulos
#print(base_credits.isnull().sum())

# Mostra os valores nulos
print(base_credits.loc[pd.isnull(base_credits['age'])],'\n\n')

# .fillna = filtra os valores nulos | com a média da coluna, e substitui com o inplace 
base_credits['age'].fillna(base_credits['age'].mean(), inplace = True)
print('================== Valores entre 29 e 32 ==================')
print('Or: \n',base_credits.loc[(base_credits['clientid'] == 29) | (base_credits['clientid'] == 31) | (base_credits['clientid'] == 32)])
print('Isin(): \n',base_credits.loc[(base_credits['clientid'].isin([29,31,32]))])