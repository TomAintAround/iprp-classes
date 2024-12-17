import turtle

def triangulo(lado, x, y, angulo):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angulo)
    turtle.pendown()

    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
    
    return None

triangulo(100, -100, 200, 123)
turtle.exitonclick()
