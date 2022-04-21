from email.mime import base
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./Arquivos Base/census.csv')
X_census = base_census.iloc[:,0:14].values
Y_census = base_census.iloc[:,14].values

label_encoder_teste = LabelEncoder()
teste = label_encoder_teste.fit_transform(X_census[:,1])
print('===== Valor Inteiro =====')
print(X_census[:,1],'\n')
# Codificamos valores para trabalhar matemáticamente com eles
print('===== Codificando Valores =====')
print(teste)

label_encoder_workclass = LabelEncoder()
label_encoder_educational = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])
X_census[:,3] = label_encoder_educational.fit_transform(X_census[:,3])
X_census[:,5] = label_encoder_marital.fit_transform(X_census[:,5])
X_census[:,6] = label_encoder_occupation.fit_transform(X_census[:,6])
X_census[:,7] = label_encoder_relationship.fit_transform(X_census[:,7])
X_census[:,8] = label_encoder_race.fit_transform(X_census[:,8])
X_census[:,9] = label_encoder_sex.fit_transform(X_census[:,9])
X_census[:,13] = label_encoder_country.fit_transform(X_census[:,13])

print(X_census[0,0])

