import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,3,6,1,0]

x2 = [2,4,6,8,10]
y2 = [4,1,9,5,2]

plt.title("Titulo das barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()

plt.show()