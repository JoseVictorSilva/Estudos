from cv2 import kmeans
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X_random, y_random = make_blobs(n_samples=200, centers=5, random_state=1)
print('X RANDOM')
print(X_random,'\n')
print('Y RANDOM')
print(y_random,'\n')

#grafico = px.scatter(X_random[:,0],X_random[:,1])
#grafico.show()

kmeans_blobs = KMeans(n_clusters=5)
kmeans_blobs.fit(X_random)

rotulos = kmeans_blobs.predict(X_random)
centroides = kmeans_blobs.cluster_centers_
grafico1 = px.scatter(x=X_random[:,0],y=X_random[:,1], color= rotulos)
grafico2 = px.scatter(x=centroides[:,0], y=centroides[:,1], size =[5,5,5,5,5])
grafico3 = go.Figure(data=grafico1.data+grafico2.data)
grafico3.show()

