import turtle

def poligono(comprimentoLado, numeroLados, x, y, angulo):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angulo)
    turtle.pendown()

    anguloExterno = 360 / numeroLados

    for i in range(numeroLados):
        turtle.forward(comprimentoLado)
        turtle.left(anguloExterno)
    
    return None

poligono(100, 4, 100, -200, 78)
turtle.exitonclick()
