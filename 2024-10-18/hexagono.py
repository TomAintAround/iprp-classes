# Exercícios 2.11

import turtle
from math import sin, cos, pi

anguloInicial: float = pi / 3

def pergunta() -> float:
    try:
        apotema: float = float(input('Insire o comprimento da apótema: ').strip())

        if apotema <= 0:
            raise ValueError
        else:
            return apotema
    except ValueError:
        raise ValueError('Insire um número maior que 0')

def bordas(apotema: float, repeticoes: int) -> None:
    if repeticoes > 0:
        turtle.left(60)
        turtle.forward(apotema)
        bordas(apotema, repeticoes - 1)

def ladosDoTriangulo(apotema: float, repeticoes: int) -> None:
    angulo = anguloInicial * (repeticoes + 2)

    if repeticoes <= 5:
        turtle.teleport(0, 0)
        turtle.goto(cos(angulo) * apotema, sin(angulo) * apotema)
        ladosDoTriangulo(apotema, repeticoes + 1)

def main() -> None:
    apotema: float = pergunta()

    turtle.hideturtle()
    turtle.goto(cos(anguloInicial) * apotema, sin(anguloInicial) * apotema)
    turtle.left(120)
    bordas(apotema, 6)
    ladosDoTriangulo(apotema, 0)
    turtle.exitonclick()

if __name__ == '__main__':
    main()