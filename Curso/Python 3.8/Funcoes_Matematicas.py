import math

# math.prod - retorna o produto de um container numérico

nun_v1 = [2,3,6,8]
nun_v2 = (2,3,6,8)
nun_v3 = {2,3,6,8}

print(math.prod(nun_v1))
print(math.prod(nun_v2))
print(math.prod(nun_v3))

# math.isqrt
print(f'Raiz: {math.isqrt(9)}')
print(f'Raiz: {math.sqrt(7)}')
print(f'Raiz: {math.sqrt(9)}')


# math.dist - retorna a distância euclidiana entre dois pontos (3D e 2D)

# Ponto 3D
p3d1 = [12,50,40]
p3d2 = (6,7,13)
# Ponto 2D
p2d1 = [12,50]
p2d2 = [6,7]

print(f'Distância 3D: {math.dist(p3d1,p3d2)}')
print(f'Distância 2D: {math.dist(p2d1,p2d2)}')

# mat.hypot - retorna a hipotenusa (* -> desempacota)

print(f'Hipotenusa: {math.hypot(*p3d1)}')
print(f'Hipotenusa: {math.hypot(*p3d2)}')

# Estatistica
import statistics
# statistics.fmean - calcula a média de números reais

valores_reais = [1.45, 6.789, 3.45, 89.98]
valores_inteiros = [1, 6, 3, 8]

print(f'Média: {statistics.fmean(valores_reais)}')
print(f'Média: {statistics.fmean(valores_inteiros)}')

# statistics.fgeometric_mean - calcula a média geométrica

valores_reais = [1.45, 6.789, 3.45, 89.98]
valores_inteiros = [1, 6, 3, 8]

print(f'Média Geométrica: {statistics.geometric_mean(valores_reais)}')
print(f'Média Geométrica: {statistics.geometric_mean(valores_inteiros)}')

# statistics.multimode - retorna o valor mais frequente em uma sequência
