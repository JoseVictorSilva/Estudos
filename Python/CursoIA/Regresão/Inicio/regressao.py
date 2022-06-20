import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base_plano_saude = pd.read_csv('../ArquivosBase/plano_saude.csv')
print(base_plano_saude)

X_plano_saude = base_plano_saude.iloc[:,0].values
print(X_plano_saude)
y_plano_saude = base_plano_saude.iloc[:,1].values
print(y_plano_saude)
print(f'CORRELAÇÃO\n{np.corrcoef(X_plano_saude, y_plano_saude)}')
print(X_plano_saude.shape) # É só um array mas tem que transformar em matriz
X_plano_saude = X_plano_saude.reshape(-1,1) # Transforma em matriz

regressor_plano_saude = LinearRegression()
regressor_plano_saude.fit(X_plano_saude, y_plano_saude)
print(f"b0: {regressor_plano_saude.intercept_}")
print(f"b1: {regressor_plano_saude.coef_}")

previsoes = regressor_plano_saude.predict(X_plano_saude)
print(previsoes)

print(f'Accuracy: {regressor_plano_saude.score(X_plano_saude,y_plano_saude)*100}')

visualizador = ResidualsPlot(regressor_plano_saude)
visualizador.fit(X_plano_saude,y_plano_saude)
visualizador.poof()

grafico = px.scatter(x = X_plano_saude.ravel(), y = y_plano_saude )
grafico.add_scatter(x = X_plano_saude.ravel(), y = previsoes, name = 'Regressão')
grafico.show()