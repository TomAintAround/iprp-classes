# Exercício 2.13

import turtle

def perguntarRaio() -> float:
    try:
        raio: float = float(input('Insire o raio: ').strip())

        if raio <= 0:
            raise ValueError
        else:
            return raio
    except ValueError:
        raise ValueError('Insire um número maior que 0.')

def desenhar(raio: float) -> None:
    turtle.pen(speed = 10)
    turtle.hideturtle()
    turtle.setheading(-90)
    turtle.circle(raio, 180)
    turtle.left(180)
    turtle.circle(raio, -180)
    turtle.exitonclick()

def main() -> None:
    raio: float = perguntarRaio()
    desenhar(raio)

if __name__ == '__main__':
    main()