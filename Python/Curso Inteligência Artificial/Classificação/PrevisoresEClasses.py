from email.mime import base
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credits = pd.read_csv('./Arquivos Base/credit_data.csv')

# Previsores -> Aquilo que vamos prever: income, age, loan X
# Classe --> O que vai resultar da previsão: default Y

# Váriavel previsora X que recebe o base_credits, e selecionamos as linhas e colunas do arquivo de dados (iloc[])
#   em seguida selecionamos as linhas que no caso são todas .iloc[->:,1:4], e então as colunas que devem selecionar que
#   serão income(1), age(2) e loan(3) .iloc[:,->1:4].
# Por último convertemos isso tudo para um valor que o numpy entenda com o values
X_credit = base_credits.iloc[:,1:4 ].values
print('===================== X: ===================== ')
print(X_credit,'\n')

# É uma classe e vai servir como resultado de X
Y_credit = base_credits.iloc[:,4].values
print('===================== Y: ===================== ')
print(Y_credit)