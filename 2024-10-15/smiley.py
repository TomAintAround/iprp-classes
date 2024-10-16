# Exercício 2.7

import turtle

def smiley(raio):
    def olhos(raioCirculo, multiplicador):
        if multiplicador <= 1:
            turtle.penup()
            turtle.goto(multiplicador * 50, raioCirculo)
            turtle.begin_fill()
            turtle.circle(raioCirculo / 10)
            turtle.end_fill()
            return olhos(raioCirculo, multiplicador + 2)
        else:
            turtle.pendown()
            return None
    
    def boca(raioCirculo):
        turtle.penup()
        turtle.right(15)
        turtle.goto(-1 * raioCirculo + raioCirculo / 2, raioCirculo / 2)
        turtle.pendown()
        turtle.circle(raioCirculo * 2, 30)

    turtle.hideturtle()
    turtle.circle(raio)
    olhos(raio, -1)
    boca(raio)
    turtle.exitonclick()

smiley(200)