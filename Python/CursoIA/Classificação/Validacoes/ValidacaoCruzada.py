import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')

X_credit = np.concatenate((X_credit_treinamento, X_credit_teste), axis=0)
y_credit = np.concatenate((y_credit_treinamento, y_credit_teste), axis=0)

resultados_arvore = []
resultado_random_forest = []
resultado_knn = []
resultado_logistica = []
resultado_svm = []
resultado_rede_neural = []
for i in range(30):
    kfold = KFold(n_splits=10,shuffle=True,random_state=i)
    arvore = DecisionTreeClassifier(criterion= 'entropy', min_samples_leaf= 1, min_samples_split= 5, splitter= 'best')
    scores = cross_val_score(arvore, X_credit,y_credit, cv = kfold)
    # print(scores)
    # print(scores.mean())
    resultados_arvore.append(scores.mean())
    
    random_forest = RandomForestClassifier(criterion= 'entropy', min_samples_leaf= 1, min_samples_split= 2, n_estimators= 40)
    scores = cross_val_score(random_forest, X_credit,y_credit, cv = kfold)
    resultado_random_forest.append(scores.mean())

print('ÁRVORE')
print(resultados_arvore)
print('FLORESTA')
print(resultado_random_forest)
