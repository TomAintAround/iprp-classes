from math import sin, cos, pi
import turtle
from random import randint, random

def mickey() -> None:
    raioCara: float = random() * randint(1, 100)
    raioOrelhas: float = raioCara / 2
    vermelhosPossiveis: int = randint(0, 255) / 255
    verdesPossiveis: int = randint(0, 255) / 255
    azuisPossiveis: int = randint(0, 255) / 255
    cor: tuple = (vermelhosPossiveis, verdesPossiveis, azuisPossiveis)
    xCoord: float = random() * randint(-840, 840)
    yCoord: float = random() * randint(-410, 410)
    yOrelhas: float = yCoord + sin(pi / 4) * (raioCara + raioOrelhas)
    xOrelha1: float = xCoord + cos(pi / 4) * (raioCara + raioOrelhas)
    xOrelha2: float = xCoord + cos(3 * pi / 4) * (raioCara + raioOrelhas)

    turtle.pencolor(cor)
    turtle.teleport(xCoord, yCoord)
    turtle.dot(raioCara * 2)
    turtle.teleport(xOrelha1, yOrelhas)
    turtle.dot(raioOrelhas * 2)
    turtle.teleport(xOrelha2, yOrelhas)
    turtle.dot(raioOrelhas * 2)

def main() -> None:
    turtle.hideturtle()
    while True:
        mickey()
    turtle.exitonclick()

if __name__ == '__main__':
    main()