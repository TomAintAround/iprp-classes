# Exercício 1.17

from math import atan, sqrt, pow

x = eval(input("Qual é a abcissa x? "))
y = eval(input("Qual é a ordenada y? "))

angulo = atan(y / x)
distancia = sqrt(pow(x, 2) + pow(y, 2))

print("Essas coordenadas convertidas para polar são ({}, {}).".format(distancia, angulo))