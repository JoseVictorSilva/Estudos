import numpy as np
import pickle
from matplotlib.pyplot import axis
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

with open('../Arquivos Base/credit.pkl','rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)
print(f'Previsores de treinamento: {X_credit_treinamento.shape}')
print(f'Classes de treinamento: {y_credit_treinamento.shape}\n')

print(f'Previsores de teste: {X_credit_teste.shape}')
print(f'Classes de teste: {y_credit_teste.shape} \n')

X_credit = np.concatenate((X_credit_treinamento, X_credit_teste), axis=0)
y_credit = np.concatenate((y_credit_treinamento, y_credit_teste), axis=0)
print(f'Previsores: {X_credit.shape}')
print(f'Classes: {y_credit.shape} \n')

# {'criterion': 'entropy', 'min_samples_leaf': 1, 'min_samples_split': 5, 'splitter': 'best'}
parametros ={'criterion':['gini', 'entropy'],
             'splitter': ['best', 'random'],
             'min_samples_split': [2,5,10],
             'min_samples_leaf': [1,5,10]}
grid_search = GridSearchCV(estimator = DecisionTreeClassifier(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')

# Testei com outros valores em n_estimator mas o melhor foram esses e demorou d++++
# {'criterion': 'entropy', 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 40}
parametros ={'criterion':['gini', 'entropy'],
             'n_estimators': [40],
             'min_samples_split': [2],
             'min_samples_leaf': [1]}
grid_search = GridSearchCV(estimator = RandomForestClassifier(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')

# {'n_neighbors': 20, 'p': 1}
parametros ={'n_neighbors':[3,5,10,20],
            'p':[1,2]}
grid_search = GridSearchCV(estimator = KNeighborsClassifier(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')

'''
# {'C': 1.0, 'solver': 'lbfgs', 'tol': 0.0001}
parametros ={'tol':[0.0001,0.00001,0.000001],
            'C':[1.0,1.5,2.0],
            'solver':['lbfgs','sag','saga']}
grid_search = GridSearchCV(estimator = LogisticRegression(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')

# {'C': 1.5, 'kernel': 'rbf', 'tol': 0.001}
parametros ={'tol':[0.001,0.0001,0.00001],
            'C':[1.0,1.5,2.0],
            'kernel':['rbf','linear','poly', 'sigmoid']}
grid_search = GridSearchCV(estimator = SVC(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')


# relu 10 adam
parametros ={'activation':['relu','logistic','tanh'],
            'solver':['adam','sgd'],
            'batch_size':[10,56,]}
grid_search = GridSearchCV(estimator = MLPClassifier(), param_grid=parametros)
grid_search.fit(X_credit,y_credit)
melhores_parametros = grid_search.best_params_
melhor_resultado = grid_search.best_score_
print(f'Melhores parametros: {melhores_parametros}')
print(f'Melhores resultados: {melhor_resultado*100}%\n')'''

