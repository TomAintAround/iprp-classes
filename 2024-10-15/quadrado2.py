import turtle

def quadrado(lado, x, y, angulo):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angulo)
    turtle.pendown()

    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    
    turtle.hideturtle()

    return None

quadrado(100, -300, -20, -100)
turtle.exitonclick()