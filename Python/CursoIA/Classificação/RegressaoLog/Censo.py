from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle

with open('../Arquivos Base/censu.pkl','rb') as f:
    X_census_treinamento, y_census_treinamento, X_census_teste, y_census_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_census_treinamento.shape}')
print(f'Classes de treinamento: {y_census_treinamento.shape}\n')

print(f'Previsores de teste: {X_census_teste.shape}')
print(f'Classes de teste: {y_census_teste.shape}\n')

logistic_census = LogisticRegression(random_state=1)
logistic_census.fit(X_census_treinamento,y_census_treinamento)
print(f'B0: {logistic_census.intercept_}') 
print(f"B's{logistic_census.coef_}")
previsoes = logistic_census.predict(X_census_teste)
print(previsoes)
print(f'Acurracy: {accuracy_score(y_census_teste, previsoes)*100}%')

cm = ConfusionMatrix(logistic_census)
cm.fit(X_census_treinamento,y_census_treinamento)
cm.score(X_census_teste,y_census_teste)
cm.show()