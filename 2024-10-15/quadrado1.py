import turtle

def desenharQuadrado(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)

    return None

desenharQuadrado(1000)

turtle.exitonclick()
