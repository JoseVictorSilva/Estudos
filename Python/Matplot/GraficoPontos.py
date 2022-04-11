from turtle import color
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,6,1,0]
tamanho = [100,200,300,400,500]
plt.title("Titulo das barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Pontos
plt.scatter(x,y, label = "Meus Pontos", color = "k", marker = '.', s = tamanho) # s = size

# Linha
plt.plot(x,y, linestyle='-.')
plt.legend()

plt.show()
#plt.savefig(",dpi=tamanhoDaImagem") -> salva a imagem