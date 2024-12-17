# Exercício 2.7

import turtle

def smiley(raio):
    def olhos(raioCirculo, multiplicador):
        if multiplicador <= 1:
            turtle.teleport(multiplicador * 50, raioCirculo)
            turtle.dot(raioCirculo / 10 * 2)
            return olhos(raioCirculo, multiplicador + 2)
        else:
            turtle.pendown()
            return None
    
    def boca(raioCirculo):
        turtle.right(15)
        turtle.teleport(-1 * raioCirculo + raioCirculo / 2, raioCirculo / 2)
        turtle.circle(raioCirculo * 2, 30)

    turtle.hideturtle()
    turtle.circle(raio)
    olhos(raio, -1)
    boca(raio)
    turtle.exitonclick()

smiley(200)
