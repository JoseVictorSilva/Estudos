import pandas as pd
from pyECLAT import ECLAT


base_mercado1 = pd.read_csv('ArquivosBase/mercado.csv',header=None)
print(base_mercado1)

eclat = ECLAT(data=base_mercado1)

print(eclat.df_bin)
print(eclat.uniq_, '\n')

indices, suporte = eclat.fit(min_support=0.3, min_combination=1, max_combination=3)
print(indices,'\n')
print(suporte)