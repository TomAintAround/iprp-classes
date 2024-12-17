# Exercício 2.18

import turtle

def perguntarRaio() -> None:
    try:
        comprimentoRaio: float = float(input('Insire o comprimento do raio do círculo: ').strip())

        if comprimentoRaio > 0:
            return comprimentoRaio
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Insire um número maior que 0.')

def circuloGrande(raio: float) -> None:
    turtle.setheading(-90)
    turtle.circle(raio)

def semiCirculo(raio: float) -> None:
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.forward(raio * 2)
    turtle.setheading(90)
    turtle.circle(raio, -180)
    turtle.end_fill()

def circuloPequeno(cor: str, x: float, y: float, diametro: float) -> None:
    turtle.pen(pencolor=cor)
    turtle.teleport(x, y)
    turtle.dot(diametro)

def main() -> None:
    raio: float = perguntarRaio()
    diametroMedio: float = raio
    diametroPequeno: float = raio / 4
    xCirculo1: float = -(raio / 2)
    yCirculo1: float = 0
    xCirculo2: float = raio / 2
    yCirculo2: float = yCirculo1

    turtle.hideturtle()
    turtle.pen(speed=10, fillcolor='black')
    turtle.teleport(-raio, 0)
    circuloGrande(raio)
    semiCirculo(raio)
    circuloPequeno('black', xCirculo1, yCirculo1, diametroMedio)
    circuloPequeno('white', xCirculo2, yCirculo2, diametroMedio)
    circuloPequeno('white', xCirculo1, yCirculo1, diametroPequeno)
    circuloPequeno('black', xCirculo2, yCirculo2, diametroPequeno)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
