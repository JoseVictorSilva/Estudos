import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

base_cartao=pd.read_csv('ArquivosBase/credit_card_clients.csv', header=1)
print(base_cartao,'\n')

base_cartao['BILL_TOTAL'] = base_cartao['BILL_AMT1'] + base_cartao['BILL_AMT2'] + base_cartao['BILL_AMT3'] + base_cartao['BILL_AMT4'] + base_cartao['BILL_AMT5'] + base_cartao['BILL_AMT6']
print(base_cartao,'\n')

X_cartao = base_cartao.iloc[:,[1,25]].values
print(X_cartao,'\n')

scaler_cartao = StandardScaler()
X_cartao = scaler_cartao.fit_transform(X_cartao)
print(X_cartao,'\n')

dbscan_cartao = DBSCAN(eps=0.37, min_samples=5)
rotulos = dbscan_cartao.fit_predict(X_cartao)
print("RÓTULOS")
print(rotulos)

print(np.unique(rotulos, return_counts=True))

grafico1 = px.scatter(x=X_cartao[:,0], y=X_cartao[:,1], color=rotulos)

grafico1.show()