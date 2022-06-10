from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle
import numpy as np


with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape}')

logistc_credit = LogisticRegression(random_state=1)
logistc_credit.fit(X_credit_treinamento, y_credit_treinamento)
print(f'B0: {logistc_credit.intercept_}') 
print(f"B's{logistc_credit.coef_}")
previsao = logistc_credit.predict(X_credit_teste)
print(f'Previsão: {previsao}')

print(f'Acurracy: {accuracy_score(y_credit_teste, previsao)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsao)}') 
# Linha[0] -> Não pagam empréstimo  [Acertos, Erros]
# Linha[1] -> Pagam empréstimo      [Erros, Acertos]

print(f'Report:\n {classification_report(y_credit_teste, previsao)}') 

# Matriz de confusão com yellowBrick
cm = ConfusionMatrix(logistc_credit)
cm.fit(X_credit_treinamento,y_credit_treinamento)
cm.score(X_credit_teste,y_credit_teste)
cm.show()