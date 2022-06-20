import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

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

dendograma = dendrogram(linkage(base_salario, method='ward'))
plt.title('Dendograma')
plt.xlabel('Pessoas')
plt.ylabel('Distância');
plt.show()

hc_salario = AgglomerativeClustering(n_clusters=3,linkage='ward',affinity='euclidean')
rotulos = hc_salario.fit_predict(base_salario)
print("RÓTULOS")
print(rotulos)

grafico1 = px.scatter(x=base_salario[:,0], y=base_salario[:,1], color=rotulos)
grafico1.show()

'''
grafico1 = px.scatter(x=base_salario[:,0], y=base_salario[:,1], color=rotulos)
grafico2 = px.scatter(x=centroides[:,0], y=centroides[:,1],size =[12,12,12])
grafico3 = go.Figure(data = grafico1.data + grafico2.data)
grafico3.show()'''
