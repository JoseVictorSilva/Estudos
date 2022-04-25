from sklearn.tree import DecisionTreeClassifier
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

arvore_census = DecisionTreeClassifier(criterion='entropy', random_state=0)
arvore_census.fit(X_census_treinamento, y_census_treinamento)

previsoes = arvore_census.predict(X_census_teste)
print(previsoes)

print(f'Acurracy: {accuracy_score(y_census_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_census_teste, previsoes)}')
print(arvore_census.classes_)
fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(20,20))
print(tree.plot_tree(arvore_census,feature_names=previsoes, class_names=arvore_census.classes_, filled = True))
fig.savefig('Censo_Arvore.png')
