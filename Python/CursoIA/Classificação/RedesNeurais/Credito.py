from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
import pickle

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')
print(y_credit_teste)
# Aumento a quantidade de diminuições de ocorrencia de erros para 1000 (era 200) e mostra a quantidade de vezes que é executado em verbose
# Diminui o erro mínimo para 0.0000100
# Para saber a quantidade de camadas ocultas: (3+1)/2 -> (Entradas+Saídas)/2
rede_neural_credit = MLPClassifier(max_iter=1500, tol=0.000010, solver = "adam", activation="relu", hidden_layer_sizes=(2,2))
rede_neural_credit.fit(X_credit_treinamento,y_credit_treinamento)

previsoes = rede_neural_credit.predict(X_credit_teste)
print(previsoes)

print(previsoes)
print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}')
print(rede_neural_credit.classes_)