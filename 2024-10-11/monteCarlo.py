# Exercício 5.10

from math import sqrt

areaDoQuadrado = 4
area1 = 1
area2 = 1
area3 = 1 + sqrt(2)
area4 = sqrt(2)

probabilidadeNumeroImpar = (area1 + area3) / areaDoQuadrado
print('A probablidade do dardo cair num número ímpar é {:.2f}.'.format(probabilidadeNumeroImpar))