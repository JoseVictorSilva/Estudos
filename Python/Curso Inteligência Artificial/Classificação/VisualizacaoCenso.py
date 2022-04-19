from email.mime import base
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./Arquivos Base/census.csv')

print(np.unique(base_census['income'], return_counts=True))
#sns.countplot(x=base_census['income'])
#plt.hist(x=base_census['age'])
#plt.show()

grafico = px.treemap(base_census, path=['workclass'])
grafico = px.treemap(base_census, path=['workclass','age'])
grafico = px.treemap(base_census, path=['occupation','relationship'])
grafico = px.parallel_categories(base_census, dimensions=['occupation','relationship'])
grafico.show()