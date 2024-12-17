# Exercício 2.12

import turtle
from sys import setrecursionlimit
from random import randint, choice

def escolherLimite() -> float:
    try:
        limite: float = float(input('Escolha o limite da distância do turtle: ').strip())
        
        if limite <= 0:
            raise ValueError
        else:
            return limite
    except ValueError:
        raise ValueError('Escolha um número maior que 0.')

def acao(limite: float) -> None:
    if turtle.distance(0, 0) < limite:
        turtle.forward(2)
    else:
        comportamentos: tuple = (comportamento1, comportamento2)
        choice(comportamentos)()

    acao(limite)

def comportamento1() -> None:
    turtle.setheading(turtle.towards(0, 0))
    turtle.forward(1)

def comportamento2() -> None:
    turtle.setheading(180 + randint(-90, 90))
    turtle.forward(1)

def main() -> None:
    limite: float = escolherLimite()

    setrecursionlimit(10000)
    turtle.hideturtle()
    turtle.pen(speed = 10)
    turtle.forward(limite)
    acao(limite)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
