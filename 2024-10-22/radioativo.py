# Exercício 2.17

import turtle
from math import pi, sin, cos

def perguntarRaio() -> None:
    try:
        comprimentoRaio: float = float(input('Insire o comprimento do raio: ').strip())

        if comprimentoRaio > 0:
            return comprimentoRaio
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Insire um número maior que 0.')

def frame(comprimentoLado: float, raio: float) -> None:
    turtle.pen(fillcolor='yellow')
    turtle.teleport(-comprimentoLado / 2, -comprimentoLado / 2)
    turtle.begin_fill()
    for repeticoes in range(4):
        turtle.forward(comprimentoLado)
        turtle.left(90)
    turtle.end_fill()

def arco(raio: float) -> None:
    anguloInicial: float = pi / 3
    for repeticoes in range(3):
        novoAngulo: float = anguloInicial + 2 * pi / 3 * repeticoes
        turtle.teleport(raio * cos(novoAngulo), raio * sin(novoAngulo))
        turtle.setheading(turtle.towards(0,0))
        turtle.pen(fillcolor='black')
        turtle.begin_fill()
        turtle.forward(raio)
        turtle.left(120)
        turtle.forward(raio)
        turtle.left(90)
        turtle.circle(raio, 60)
        turtle.end_fill()

def miniCirculo(raio) -> None:
    turtle.teleport(0, 0)
    turtle.dot(raio)
    turtle.teleport(raio / 2, 0)
    turtle.setheading(90)
    turtle.pen(pencolor='yellow')
    turtle.circle(raio / 2)

def main() -> None:
    raio: float = perguntarRaio()
    raioPequeno: float = raio * 2 / 5
    comprimentoLado: float = raio * 2 + raio / 10

    turtle.hideturtle()
    turtle.pen(speed=10, pensize=(raio / 100))
    frame(comprimentoLado, raio)
    arco(raio)
    miniCirculo(raioPequeno)

    turtle.exitonclick()

if __name__ == '__main__':
    main()