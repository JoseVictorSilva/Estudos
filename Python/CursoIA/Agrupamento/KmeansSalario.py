import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

x = [20,27,21,37,46,53,55,47,52,32,39,41,39,48,48]
y = [1000,1200,2900,1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500]

#grafico = px.scatter(x,y)
#grafico.show()
a = zip(x,y)
base_salario = np.array(list(a))
print('BASE SALÁRIO')
print(base_salario,'\n')

scaler_salario = StandardScaler()
base_salario = scaler_salario.fit_transform(base_salario)
print('BASE SALÁRIO ESCALADA')
print(base_salario,'\n')

kmeans_salario = KMeans(n_clusters=3)
kmeans_salario.fit(base_salario)
centroides = kmeans_salario.cluster_centers_
print('CENTROIDES')
print(centroides,'\n') 
centroides_escalado = scaler_salario.inverse_transform(kmeans_salario.cluster_centers_)
print('CENTROIDES NORMALIZADOS')
print(centroides_escalado,'\n') 

rotulos = kmeans_salario.labels_
print('RÓTULOS')
print(rotulos,'\n')

grafico1 = px.scatter(x=base_salario[:,0], y=base_salario[:,1], color=rotulos)
grafico2 = px.scatter(x=centroides[:,0], y=centroides[:,1],size =[12,12,12])
grafico3 = go.Figure(data = grafico1.data + grafico2.data)
grafico3.show()
