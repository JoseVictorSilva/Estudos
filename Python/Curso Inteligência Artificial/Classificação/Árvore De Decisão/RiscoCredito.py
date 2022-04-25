from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import pickle

with open('../Arquivos Base/risco_credito.pkl','rb') as f:
    X_risco_credito, y_risco_credito = pickle.load(f)
print('========== X ==========')
print(X_risco_credito,'\n')
print('========== Y ==========')
print(y_risco_credito,'\n')

arvore_risco_credito = DecisionTreeClassifier(criterion='entropy')
arvore_risco_credito.fit(X_risco_credito,y_risco_credito)
print('========== Importância dos Atributos ==========')
print(arvore_risco_credito.feature_importances_,'\n')

print('========== Árvore de Decisão ==========')
previsores = ['História', 'Dívida', 'Garantia', 'Renda']
figura, eixos = plt.subplots(nrows = 1, ncols= 1, figsize =(10,10))
print(arvore_risco_credito.classes_,'\n')
print(tree.plot_tree(arvore_risco_credito,feature_names=previsores, class_names=arvore_risco_credito.classes_, filled = True))

# História boa, dívida alta, garantias nenhuma, renda > 35
# História ruim, dívida alta, garantias adequada, renda < 35
print('========== Previsão ==========')
previsoes = arvore_risco_credito.predict([[0,0,1,2],[2,0,0,0]])
print(previsoes)
figura.savefig('Risco_credito_Arvore.png')