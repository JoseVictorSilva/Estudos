from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import pickle

with open('../Arquivos Base/censu.pkl','rb') as f:
    X_census_treinamento, y_census_treinamento, X_census_teste, y_census_teste = pickle.load(f)

print(f'Previsores de treinamento: {X_census_treinamento.shape}')
print(f'Classes de treinamento: {y_census_treinamento.shape}\n')

print(f'Previsores de teste: {X_census_teste.shape}')
print(f'Classes de teste: {y_census_teste.shape}\n')

random_census = RandomForestClassifier(n_estimators = 40,criterion='entropy', random_state=0)
random_census.fit(X_census_treinamento, y_census_treinamento)

previsoes = random_census.predict(X_census_teste)
print(previsoes)

print(f'Acurracy: {accuracy_score(y_census_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_census_teste, previsoes)}')
cm = ConfusionMatrix(random_census)
cm.fit(X_census_treinamento,y_census_treinamento)
cm.score(X_census_teste,y_census_teste)
cm.show()