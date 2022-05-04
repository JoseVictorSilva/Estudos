from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


base_credits = pd.read_csv('./Arquivos Base/credit_data.csv')
X_credit = base_credits.iloc[:,1:4 ].values
Y_credit = base_credits.iloc[:,4].values

base_census = pd.read_csv('./Arquivos Base/census.csv')
X_census = base_census.iloc[:,0:14].values
Y_census = base_census.iloc[:,14].values

# Previsores e Classes
# Criamos previsores e classes para treinar e de teste, os testes serão de 25% do tamanho do treino e sem randomização
X_credit_treinamento, X_credit_teste, Y_credit_treinamento, Y_credit_teste = train_test_split(X_credit, Y_credit, test_size=0.25, random_state=0)
print('========== CRÉDITO ==========')
print(X_credit_treinamento.shape)
print(Y_credit_treinamento.shape)
# 25% definido em test_size
print(f'X Teste: {X_credit_teste.shape}\nY Teste: {Y_credit_teste.shape}\n')

print('========== CENSO ==========')
X_census_treinamento, X_census_teste, Y_census_treinamento, Y_census_teste = train_test_split(X_census, Y_census, test_size=0.15, random_state=0)
print(X_census_treinamento.shape)
print(Y_census_treinamento.shape)
# 25% definido em test_size
print(f'X Teste: {X_census_teste.shape}\nY Teste: {Y_census_teste.shape}')

# Pickle salva variáveis em disco
with open('./Arquivos Base/credits.pkl', mode = 'wb') as f:
    pickle.dump([X_credit_treinamento,Y_credit_treinamento, X_credit_teste, Y_credit_teste], f)

with open('./Arquivos Base/census.pkl', mode = 'wb') as f:
    pickle.dump([X_census_treinamento,Y_census_treinamento, X_census_teste, Y_census_teste], f)