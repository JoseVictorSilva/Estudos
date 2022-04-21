from email.mime import base
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./Arquivos Base/census.csv')
X_census = base_census.iloc[:,0:14].values
Y_census = base_census.iloc[:,14].values


# Problemas do labelEncoder: problema de peso, um item tem valor 15 e aparece 3x ele ficam com peso 
# diferente de um com valor 4 que aparece também 3x
# One Hot Encoder resolve isso
# Gol = 1, Pálio = 2, Uno = 3
# Gol   1 0 0
# Pálio 0 1 0
# Uno   0 0 1

print(X_census[2,1])


one_hot_encoder_census = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder = 'passthrough')
X_census = one_hot_encoder_census.fit_transform(X_census).toarray()
print(one_hot_encoder_census)
print(X_census)
print(X_census[2,1])
