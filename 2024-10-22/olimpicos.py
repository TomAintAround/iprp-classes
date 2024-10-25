# Exercício 2.16

import turtle

def circunferencia(cores: tuple, raio: float, xInicial: float, yInicial: float, repeticoes: int = 5) -> None:
    if repeticoes > 0:
        cor: str = cores[5 - repeticoes]
        turtle.pencolor(cor)
        turtle.circle(raio)

        novoX: float = xInicial + raio * 6 / 5
        novoY: float = -yInicial
        turtle.teleport(novoX, novoY)
        circunferencia(cores, raio, novoX, novoY, repeticoes - 1)

def main() -> None:
    raio: float = 200.0
    xInicial: float = -2.5 * raio
    yInicial: float = raio / 2 - raio / 10
    cores: tuple = ('blue', 'yellow', 'black', 'lime', 'red')

    turtle.pen(speed=10)
    turtle.pensize(10)
    turtle.hideturtle()
    turtle.teleport(xInicial, yInicial)
    circunferencia(cores, raio, xInicial, yInicial)
    turtle.exitonclick()

if __name__ == '__main__':
    main()