from turtle import color
import matplotlib.pyplot as plt
dados = open("populacao_brasileira.csv").readlines()
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y, color="grey")
plt.plot(x,y, linestyle="--", color="k")
plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.xlabel("População x100.000.000")
plt.show()