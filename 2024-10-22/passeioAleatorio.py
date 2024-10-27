# Exercício 5.19

import turtle
from random import choice
from math import radians, sin, cos, isclose

def perguntar(tipo, pergunta: str, fraseErro: str, condicao) -> float:
    valor = tipo(input(pergunta).strip())

    if condicao(valor):
        return valor
    else:
        raise ValueError(fraseErro)

def retangulo(comprimento: float, altura: float) -> None:
    for _ in range(2):
        turtle.forward(comprimento)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)

def linhas(angulo: int, quantidade: int, xInicial: float, yInicial: float, ladoQuadrado: float, comprimento: float, eColuna: bool, eLinha: bool) -> None:
    turtle.setheading(angulo)
    for linha in range(1, quantidade):
        x: float = xInicial + ladoQuadrado * linha * eColuna
        y: float = yInicial + ladoQuadrado * linha * eLinha
        turtle.teleport(x, y)
        turtle.forward(comprimento)

def coordenadasPossiveis(quantidade: int, posicaoInicial: float, ladoQuadrado: float) -> list:
    lista: list = []
    for elemento in range(quantidade + 1):
        posicao: float = posicaoInicial + ladoQuadrado * elemento
        lista += [posicao]
    return lista

def posicaoInicialAleatoria(quantidadeColunas: int, quantidadeLinhas: int, xInicial: float, yInicial: float, ladoQuadrado: float) -> None:
    x: float = choice(coordenadasPossiveis(quantidadeColunas, xInicial, ladoQuadrado))
    y: float = choice(coordenadasPossiveis(quantidadeLinhas, yInicial, ladoQuadrado))
    turtle.pen(pencolor='red')
    turtle.teleport(x, y)
    turtle.dot(ladoQuadrado / 4)

def passeioAleatorio(numeroPassos: int, ladoQuadrado: float, xInicial: float, yInicial: float) -> None:
    turtle.pen(pencolor='red', pensize=(ladoQuadrado / 10))
    for _ in range(numeroPassos):
        anguloAtual: int = choice([90, -90, 0, 180])
        proximoX: float = turtle.xcor() + cos(radians(anguloAtual)) * ladoQuadrado
        proximoY: float = turtle.ycor() + sin(radians(anguloAtual)) * ladoQuadrado
        eMaiorX: bool = abs(proximoX) > abs(xInicial)
        eMaiorY: bool = abs(proximoY) > abs(yInicial)
        eProximoX: bool = isclose(abs(proximoX), abs(xInicial))
        eProximoY: bool = isclose(abs(proximoY), abs(yInicial))
        coordenadaInvalidaX: bool = eMaiorX and not eProximoX
        coordenadaInvalidaY: bool = eMaiorY and not eProximoY
        coordenadaInvalida: bool = coordenadaInvalidaX or coordenadaInvalidaY

        if coordenadaInvalida:
            anguloAtual += 180
        
        turtle.setheading(anguloAtual)
        turtle.forward(ladoQuadrado)

def main() -> None:
    perguntaLadoQuadrado: str = 'Insire o comprimento do lado dos quadrados: '
    perguntaQuantidadeLinhas: str = 'Insire a quantidade de linhas: '
    perguntaQuantidadeColunas: str = 'Insire a quantidade de colunas: '
    perguntaNumeroPassos: str = 'Insire o número de passos: '
    erroLadoQuadrado: str = 'Insire um número maior que 0.'
    erroQuantidadeLinhas: str = 'Insire um número inteiro maior que 1.'
    erroQuantidadeColunas: str = 'Insire um número inteiro maior que 1.'
    erroNumeroPassos: str = 'Insire um número inteiro maior que 0.'
    condicaoLadoQuadrado = lambda valor: valor > 0
    condicaoQuantidadeLinhas = lambda valor: valor > 0
    condicaoQuantidadeColunas = lambda valor: valor > 0
    condicaoNumeroPassos = lambda valor: valor > 0
    
    ladoQuadrado: float = perguntar(float, perguntaLadoQuadrado, erroLadoQuadrado, condicaoLadoQuadrado)
    quantidadeLinhas: int = perguntar(int, perguntaQuantidadeLinhas, erroQuantidadeLinhas, condicaoQuantidadeLinhas)
    quantidadeColunas: int = perguntar(int, perguntaQuantidadeColunas, erroQuantidadeColunas, condicaoQuantidadeColunas)
    comprimentoLinha: float = ladoQuadrado * quantidadeColunas
    alturaColuna: float = ladoQuadrado * quantidadeLinhas
    xInicial: float = -(comprimentoLinha) / 2
    yInicial: float = -(alturaColuna) / 2
    anguloLinha: int = 0
    anguloColuna: int = 90
    numeroPassos: int = perguntar(int, perguntaNumeroPassos, erroNumeroPassos, condicaoNumeroPassos)

    #turtle.hideturtle()
    turtle.pen(speed=10)
    turtle.teleport(xInicial, yInicial)
    retangulo(comprimentoLinha, alturaColuna)
    linhas(anguloColuna, quantidadeColunas, xInicial, yInicial, ladoQuadrado, alturaColuna, True, False)
    linhas(anguloLinha, quantidadeLinhas, xInicial, yInicial, ladoQuadrado, comprimentoLinha, False, True)
    posicaoInicialAleatoria(quantidadeColunas, quantidadeLinhas, xInicial, yInicial, ladoQuadrado)
    passeioAleatorio(numeroPassos, ladoQuadrado, xInicial, yInicial)
    turtle.exitonclick()

if __name__ == '__main__':
    main()