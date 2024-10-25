# Exercício 2.15

import turtle

def quadrados(distanciaInicial: float, numeroRepeticoes: int, anguloExtra: float, distanciaExtra: float) -> None:
    for multiplicador in range(0, numeroRepeticoes):
        turtle.setheading(-70 + anguloExtra * multiplicador)
        for repeticoes in range(4):
            turtle.forward(distanciaInicial + distanciaExtra * multiplicador)
            turtle.left(90)

def main() -> None:
    turtle.pen(speed=10)
    turtle.hideturtle()
    quadrados(50, 25, 10, 10)
    turtle.exitonclick()

if __name__ == '__main__':
    main()