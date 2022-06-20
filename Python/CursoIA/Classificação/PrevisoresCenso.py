from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./Arquivos Base/census.csv')
X_census = base_census.iloc[:,0:14].values
print(X_census)
Y_census = base_census.iloc[:,14].values
