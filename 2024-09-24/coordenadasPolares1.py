# Exercício 1.17

from math import atan2, sqrt, pow, pi

x = eval(input("Qual é a abcissa x? "))
y = eval(input("Qual é a ordenada y? "))

angulo = atan2(y, x)

distancia = sqrt(pow(x, 2) + pow(y, 2))

print("Essas coordenadas convertidas para polar são ({}, {}).".format(distancia, angulo))