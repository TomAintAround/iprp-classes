# Exercício 5.19

import turtle
from random import choice
from math import pi, radians, sin, cos, isclose

def perguntar(tipo, pergunta: str, fraseErro: str, condicao) -> float:
    valor = tipo(input(pergunta).strip())

    if condicao(valor):
        return valor
    else:
        raise ValueError(fraseErro)

def quadradro(lado: float) -> None:
    for repeticoes in range(4):
        turtle.forward(lado)
        turtle.left(90)

def linhas(angulo: int, comprimento: float, quantidade: int, posInicial: float, comprimentoColunas: float, alturaLinhas: float) -> None:
    turtle.setheading(angulo)
    for linha in range(1, quantidade -1):
        x: float = posInicial + comprimentoColunas * linha
        y: float = posInicial + alturaLinhas * linha
        turtle.teleport(x, y)
        turtle.forward(comprimento)

def coordenadasPossiveis(posInicial: float, alturaLinha: float) -> list:
    lista = [posInicial]
    multiplicador = 1
    while lista[-1] < -posInicial:
        proximoElemento = posInicial + alturaLinha * multiplicador
        multiplicador += 1
        lista += [proximoElemento]
    return lista

def passeio(posInicial: float, alturaLinha: float, passosRestantes: int) -> None:
    coordenadas: list = coordenadasPossiveis(posInicial, alturaLinha)
    xInicial: float = choice(coordenadas)
    yInicial: float = choice(coordenadas)
    angulosPossiveis: list = [90, -90, 0, 180]

    turtle.showturtle()
    turtle.pen(pencolor='red', pensize=(alturaLinha / 20))
    turtle.teleport(xInicial, yInicial)
    turtle.dot(alturaLinha / 4)

    while passosRestantes > 0:
        angulo: float = choice(angulosPossiveis)
        anguloRadianos: float = radians(angulo)
        xSeguinte = turtle.xcor() + cos(anguloRadianos) * alturaLinha
        ySeguinte = turtle.ycor() + sin(anguloRadianos) * alturaLinha
        eMaior = lambda coordenada: abs(coordenada) > abs(posInicial)
        estaPerto = lambda coordenada: isclose(abs(coordenada), abs(posInicial))
        eMaiorCorrigido = lambda coordenada: eMaior(coordenada) and not estaPerto(coordenada)

        if eMaiorCorrigido(xSeguinte) or eMaiorCorrigido(ySeguinte):
            angulo += 180
        
        turtle.setheading(angulo)
        turtle.forward(alturaLinha)
        passosRestantes -= 1

def main() -> None:
    perguntaLadoGrelha: str = 'Insire o comprimento do lado da grelha: '
    perguntaQuantidadeLinhas: str = 'Insire a quantidade de linhas e colunas: '
    perguntaNumeroPassos: str = 'Insire o número de passos: '
    erroLadoGrelha: str = 'Insire um número maior que 0.'
    erroQuantidadeLinhas: str = 'Insire um número inteiro maior que 1.'
    erroNumeroPassos: str = 'Insire um número inteiro maior que 0.'
    condicaoLadoGrelha = lambda valor: valor > 0
    condicaoQuantidadeLinhas = lambda valor: valor > 1
    condicaoNumeroLinhas = lambda valor: valor > 0
    
    ladoGrelha: float = perguntar(float, perguntaLadoGrelha, erroLadoGrelha, condicaoLadoGrelha)
    posInicial: float = -ladoGrelha / 2
    quantidadeLinhas: int = perguntar(int, perguntaQuantidadeLinhas, erroQuantidadeLinhas, condicaoQuantidadeLinhas)
    anguloLinhas: int = 0
    anguloColunas: int = 90
    alturaLinha: float = ladoGrelha / (quantidadeLinhas - 1)
    numeroPassos: int = perguntar(int, perguntaNumeroPassos, erroNumeroPassos, condicaoNumeroLinhas)

    turtle.hideturtle()
    turtle.pen(speed=10)
    turtle.teleport(posInicial, posInicial)
    quadradro(ladoGrelha)
    linhas(anguloColunas, ladoGrelha, quantidadeLinhas, posInicial, alturaLinha, 0)
    linhas(anguloLinhas, ladoGrelha, quantidadeLinhas, posInicial, 0, alturaLinha)
    passeio(posInicial, alturaLinha, numeroPassos)
    turtle.exitonclick()

if __name__ == '__main__':
    main()