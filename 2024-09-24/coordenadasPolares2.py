# Exercício 1.17

from math import atan, sqrt, pow, pi

def polar(x, y):
    distancia = sqrt(pow(x, 2) + pow(y, 2))

    if x == 0:
        if y > 0:
            angulo = pi / 2
        elif y < 0:
            angulo = 3 * pi / 2
        else:
            angulo = 0
    elif x < 0:
        angulo = atan(y / x) + pi
    else:
        angulo = atan(y / x)

    return (distancia, angulo)

x = eval(input("Qual é a abcissa x? "))
y = eval(input("Qual é a ordenada y? "))

print("Essas coordenadas convertidas para polar são {}.".format(polar(x, y)))