from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import pandas as pd


base_census = pd.read_csv('./Arquivos Base/census.csv')
X_census = base_census.iloc[:,0:14].values
Y_census = base_census.iloc[:,14].values
#print(X_census[2,1])

one_hot_encoder_census = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder = 'passthrough')
X_census = one_hot_encoder_census.fit_transform(X_census).toarray()
print('=================== ONE HOT ENCODER ===================')
print(one_hot_encoder_census)
print(X_census)
print(X_census[2,1],'\n')
scaler_census = StandardScaler()
X_census = scaler_census.fit_transform(X_census)

print('=================== ESCALONADO ===================')
print(X_census)
print('Censo [2,1]: ',X_census[2,1])