# Exercício 2.2

import turtle

def desenhar(comprimento, extra, limite, progresso):
    if progresso < limite:
        turtle.right(144)
        turtle.forward(comprimento)
        return desenhar(comprimento + extra, extra, limite, progresso + 1)
    else:
        return None

turtle.hideturtle()
desenhar(10, 10, 35, 0)
turtle.exitonclick()