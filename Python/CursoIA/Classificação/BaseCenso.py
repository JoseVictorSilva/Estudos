from email.mime import base
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./Arquivos Base/census.csv')
#print(base_census)
print(base_census.describe())
print(base_census.isnull().sum())