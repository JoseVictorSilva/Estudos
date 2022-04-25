from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape}')

naive_credits_data = GaussianNB()
naive_credits_data.fit(X_credit_treinamento,y_credit_treinamento)
previsoes = naive_credits_data.predict(X_credit_teste)
# as respostas de previsões estão em y_credit_teste
print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}') 
# Linha[0] -> Não pagam empréstimo  [Acertos, Erros]
# Linha[1] -> Pagam empréstimo      [Erros, Acertos]

print(f'Report:\n {classification_report(y_credit_teste, previsoes)}') 

# Matriz de confusão com yellowBrick
cm = ConfusionMatrix(naive_credits_data)
cm.fit(X_credit_treinamento,y_credit_treinamento)
cm.score(X_credit_teste,y_credit_teste)
#cm.show()