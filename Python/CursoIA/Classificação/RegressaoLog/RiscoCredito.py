import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

with open('../Arquivos Base/risco_credito.pkl','rb') as f:
    X_risco_credito, y_risco_credito = pickle.load(f)
print(f'Previsores:\n{X_risco_credito}\n')
print(f'Classes:\n{y_risco_credito}\n') # Vamos excluir os registros de classe moderado

X_risco_credito = np.delete(X_risco_credito, [2,7,11], axis = 0) # Axis -> apaga linha(0) ou coluna(1)
y_risco_credito = np.delete(y_risco_credito, [2,7,11], axis = 0)

logistic_risco_credito = LogisticRegression(random_state=1)
logistic_risco_credito.fit(X_risco_credito,y_risco_credito)
print(logistic_risco_credito.intercept_) # B0 parametro da conta
print(logistic_risco_credito.coef_) # Valores previsores, B1, B2, B3

# História boa(0), dívida alta(0), garantia nenhuma(1), renda > 35(2) -> resultado é baixo
# História ruim(2), dívida alta(0), garantia adequada(0), renda < 15(0) -> resultado moderado
previsao = logistic_risco_credito.predict([[0,0,1,2],[2,0,0,0]]) # Faz os calculos com Navie Bayes e retorna a classe
print(f'Previsão: {previsao}')