# Exercício 2.9

import turtle

def espiral(comprimento, angulo, extra, final):
    if extra != final:
        turtle.stamp()
        turtle.forward(comprimento * extra)
        turtle.right(angulo)
        espiral(comprimento, angulo, extra + 1, final)

turtle.up()
turtle.color('red')
espiral(1, 30, 1, 200)