# Exercício 1.17

from math import atan2, sqrt, pow, pi

def polar(x, y):
    distancia = sqrt(pow(x, 2) + pow(y, 2))
    angulo = atan2(y, x)

    return (distancia, angulo)

x = eval(input("Qual é a abcissa x? "))
y = eval(input("Qual é a ordenada y? "))

print("Essas coordenadas convertidas para polar são {}.".format(polar(x, y)))
