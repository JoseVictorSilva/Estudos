from sklearn.neighbors import KNeighborsClassifier
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix


with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape}')

KNNCredit = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2) # valores padrões
KNNCredit.fit(X_credit_treinamento, y_credit_treinamento)
previsoes = KNNCredit.predict(X_credit_teste)
print(previsoes)
print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}') 


print(f'Report:\n {classification_report(y_credit_teste, previsoes)}') 

cm = ConfusionMatrix(KNNCredit)
cm.fit(X_credit_treinamento,y_credit_treinamento)
cm.score(X_credit_teste,y_credit_teste)
cm.show()
