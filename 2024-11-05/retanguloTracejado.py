import turtle
from collections.abc import Callable

def linha(lado: float, ladoTracejado: float, espacamento: float, coordenada: Callable[[None], float], coordenadaIncial: float, multiplicador: int) -> None:
    espacoRestante = lado
    while espacoRestante >= espacamento + ladoTracejado:
        turtle.forward(ladoTracejado)
        turtle.up()
        turtle.forward(espacamento)
        turtle.down()
        espacoRestante = lado + multiplicador * coordenadaIncial - multiplicador * coordenada()

    if espacoRestante == 0:
        return

    if espacoRestante < ladoTracejado:
        turtle.forward(espacoRestante)
    else:
        turtle.forward(ladoTracejado)
        turtle.up()
        espacoRestante = lado + multiplicador * coordenadaIncial - multiplicador * coordenada()
        turtle.forward(espacoRestante)
        turtle.down()

def main() -> None:
    xInicial: float = -200.0
    yInicial: float = -500.0
    comprimento: float = 700.0
    comprimentoTracejado: float = comprimento / 10
    largura: float = 300.0
    espacamento: float = 31.0

    turtle.teleport(xInicial, yInicial)

    linha(comprimento, comprimentoTracejado, espacamento, lambda: turtle.xcor(), xInicial, 1)
    turtle.left(90)
    linha(largura, comprimentoTracejado, espacamento, lambda: turtle.ycor(), yInicial, 1)
    turtle.left(90)
    linha(comprimento, comprimentoTracejado, espacamento, lambda: turtle.xcor(), xInicial + comprimento, -1)
    turtle.left(90)
    linha(largura, comprimentoTracejado, espacamento, lambda: turtle.ycor(), yInicial + largura, -1)
    turtle.left(90)

    turtle.exitonclick()

if __name__ == '__main__':
    main()