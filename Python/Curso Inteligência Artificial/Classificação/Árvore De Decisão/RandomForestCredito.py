from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')

random_forest_credit = RandomForestClassifier(n_estimators=40, criterion='entropy',random_state=0) # Quantas árvores vai gerar
random_forest_credit.fit(X_credit_treinamento,y_credit_treinamento)
print('======== RANDOM FOREST ========')
print(random_forest_credit,'\n')
previsoes = random_forest_credit.predict(X_credit_teste)
print(previsoes)

print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}')
cm = ConfusionMatrix(random_forest_credit)
cm.fit(X_credit_treinamento,y_credit_treinamento)
cm.score(X_credit_teste,y_credit_teste)
cm.show()