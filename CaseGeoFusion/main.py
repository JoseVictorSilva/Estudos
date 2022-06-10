from sklearn.metrics import accuracy_score, confusion_matrix
from yellowbrick.classifier import ConfusionMatrix
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder, StandardScaler

base= pd.read_excel('./ArquivosBase/DadosDesafioCientista.xlsx')
base['popDe20a24'] = base['popDe20a24']+base['popDe25a34']+base['popDe35a49']
base = base.rename(columns={'popDe20a24': 'popDe20a49'})
base.fillna(base['população'].mean(), inplace=True)
X_lista_rio = base.loc[base['estado']=="RJ", ["população","popDe20a49","domiciliosA1","domiciliosA2","domiciliosB1","domiciliosB2","rendaMedia"]].values
y_lista_rio = base.loc[base['estado']=="RJ", "potencial"].values

scaler = StandardScaler()
X_lista_rio = scaler.fit_transform(X_lista_rio)

X_lista_treinamento, X_lista_teste, y_lista_treinamento, y_lista_teste = train_test_split(X_lista_rio, y_lista_rio, test_size=0.15, random_state=6)

# -----------------------------
naive_lista = GaussianNB()

naive_lista.fit(X_lista_treinamento,y_lista_treinamento)
predicao = naive_lista.predict(X_lista_teste)
print(f'Acurracy: {accuracy_score(y_lista_teste, predicao)*100}%')

cm = ConfusionMatrix(naive_lista)
cm.fit(X_lista_treinamento,y_lista_treinamento)
cm.score(X_lista_teste,y_lista_teste)
cm.show()
