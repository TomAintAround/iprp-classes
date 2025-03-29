# Exercício 2.3

import turtle
from random import randint

def passeio(repeticoes):
    if repeticoes > 0:
        turtle.forward(randint(0, 500))
        turtle.left(randint(-180, 180))
        return passeio(repeticoes - 1)
    else:
        return None
    
turtle.hideturtle()
passeio(50)
turtle.exitonclick()
