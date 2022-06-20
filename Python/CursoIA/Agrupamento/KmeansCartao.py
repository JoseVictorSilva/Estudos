import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

base_cartao=pd.read_csv('ArquivosBase/credit_card_clients.csv', header=1)
print(base_cartao)

base_cartao['BILL_TOTAL'] = base_cartao['BILL_AMT1'] + base_cartao['BILL_AMT2'] + base_cartao['BILL_AMT3'] + base_cartao['BILL_AMT4'] + base_cartao['BILL_AMT5'] + base_cartao['BILL_AMT6']
print(base_cartao)

X_cartao = base_cartao.iloc[:,[1,25]].values
print(X_cartao)

scaler_cartao = StandardScaler()
X_cartao = scaler_cartao.fit_transform(X_cartao)
print(X_cartao)

'''
wcss = []
for i in range(1,11):
    kmeans_cartao = KMeans(n_clusters=i, random_state=0)
    kmeans_cartao.fit(X_cartao)
    wcss.append(kmeans_cartao.inertia_)

print(wcss)

grafico = px.line(x=range(1,11), y=wcss)
grafico.show()'''

kmeans_cartao = KMeans(n_clusters=4, random_state=0)
rotulos=kmeans_cartao.fit_predict(X_cartao)

grafico1 = px.scatter(x=X_cartao[:,0], y=X_cartao[:,1], color=rotulos)
#grafico2 = px.scatter(x=centroides[:,0], y=centroides[:,1],size =[12,12,12])
#grafico3 = go.Figure(data = grafico1.data + grafico2.data)
grafico1.show()

lista_clientes = np.column_stack((base_cartao,rotulos))
print('LISTA CLIENTES')
print(lista_clientes,'\n')

lista_clientes=lista_clientes[lista_clientes[:,26].argsort()]
print('LISTA CLIENTES')
print(lista_clientes,'\n')

X_cartao_mais = base_cartao.iloc[:,[1,2,3,4,5,25]].values
print(X_cartao_mais,'\n')
scaler_cartao_mais = StandardScaler()
X_cartao_mais = scaler_cartao_mais.fit_transform(X_cartao_mais)
print(X_cartao_mais,'\n')

'''
wcss = []
for i in range(1,11):
    kmeans_cartao_mais = KMeans(n_clusters=i, random_state=0)
    kmeans_cartao_mais.fit(X_cartao_mais)
    wcss.append(kmeans_cartao_mais.inertia_)

print(wcss)

grafico = px.line(x=range(1,11), y=wcss)
grafico.show()'''
from sklearn.decomposition import PCA
kmeans_cartao_mais = KMeans(n_clusters=4, random_state=0)
rotulos = kmeans_cartao_mais.fit_predict(X_cartao_mais)

pca = PCA(n_components=2)
X_cartao_mais_pca = pca.fit_transform(X_cartao_mais)
