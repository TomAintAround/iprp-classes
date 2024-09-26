# Exercício 1.17

from math import atan, sqrt, pow, pi

x = eval(input("Qual é a abcissa x? "))
y = eval(input("Qual é a ordenada y? "))

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

distancia = sqrt(pow(x, 2) + pow(y, 2))

print("Essas coordenadas convertidas para polar são ({}, {}).".format(distancia, angulo))