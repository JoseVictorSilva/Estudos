from sklearn.neighbors import KNeighborsClassifier
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix


with open('../Arquivos Base/censu.pkl','rb') as f:
    X_census_treinamento, y_census_treinamento, X_census_teste, y_census_teste = pickle.load(f)

print(f'Previsores de treinamento: {X_census_treinamento.shape}')
print(f'Classes de treinamento: {y_census_treinamento.shape}\n')

print(f'Previsores de teste: {X_census_teste.shape}')
print(f'Classes de teste: {y_census_teste.shape}')

KNNCenso = KNeighborsClassifier(n_neighbors=5)
KNNCenso.fit(X_census_treinamento, y_census_treinamento)
previsoes = KNNCenso.predict(X_census_teste)
print(previsoes)
print(f'Acurracy: {accuracy_score(y_census_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_census_teste, previsoes)}') 


print(f'Report:\n {classification_report(y_census_teste, previsoes)}') 

cm = ConfusionMatrix(KNNCenso)
cm.fit(X_census_treinamento,y_census_treinamento)
cm.score(X_census_teste,y_census_teste)
cm.show()
