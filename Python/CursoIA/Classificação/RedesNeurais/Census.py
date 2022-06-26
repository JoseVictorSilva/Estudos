from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle

with open('../Arquivos Base/censu.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')

# (108+1)/2 = 55
rede_neural_census = MLPClassifier(verbose = True,max_iter=1000, tol=0.000010, hidden_layer_sizes=(55,55))
rede_neural_census.fit(X_credit_treinamento,y_credit_treinamento)

previsoes = rede_neural_census.predict(X_credit_teste)
print(previsoes)

print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}')
print(rede_neural_census.classes_)