from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import pickle

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')

arvore_credit = DecisionTreeClassifier(criterion='entropy', random_state=0) # random = gera os mesmos resultados
arvore_credit.fit(X_credit_treinamento,y_credit_treinamento)
previsoes = arvore_credit.predict(X_credit_teste)
print(previsoes)
print(f'Acurracy: {accuracy_score(y_credit_teste, previsoes)*100}%')
print(f'Matriz: {confusion_matrix(y_credit_teste, previsoes)}')
print(arvore_credit.classes_)
fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(20,20))
tree.plot_tree(arvore_credit,feature_names=previsoes, class_names=['0','1'], filled = True)
fig.savefig('arvore_credit.png')

