# Exercício 7.7

from random import randint
import turtle

def perguntarCoordenadas() -> int:
    """ Pergunta qual é o número de coordenadas

    Raises:
        ValueError: se o número for <= 0 ou não for número

    Returns:
        int: número de coordenadas definido pelo utilizador
    """    
    try:
        numeroDeCoordenadas: int = int(input("Insire o número de coordenadas: ").strip())

        if numeroDeCoordenadas > 0:
            return numeroDeCoordenadas
        else:
            raise ValueError
    except ValueError:
        print("Insire um número natural.")
        return perguntarCoordenadas()

def escreverCoordenadas(ficheiro, numeroCoordenadas: int) -> None:
    """Escreve as coordenadas aleatoriamente no ficheiro `coordenadas.txt`

    Args:
        ficheiro (_type_): ficheiro em modo de escrita
        numeroCoordenadas (int): número de coordenadas
    """    
    for _ in range(numeroCoordenadas):
        ficheiro.write(f"{(randint(0, 5), randint(0, 5))}\n")
    ficheiro.close()

def limparCoordenadas(coordenadas: list[str]) -> list[tuple[int]]:
    """Transformar a lista de coordenadas numa lista de tuplos de inteiros

    Args:
        coordenadas (list[str]): _description_

    Returns:
        list[tuple[int]]: _description_
    """    
    for i, coordenada in enumerate(coordenadas):
        coordenadas[i] = coordenada.replace("(", '').replace(", ", '').replace(")\n", '') # '(X, Y)' -> 'XY'
        numero1: int = int(coordenadas[i][0]) * 80 # 'X' -> X
        numero2: int = int(coordenadas[i][1]) * 80 # 'Y' -> Y
        coordenadas[i] = (numero1, numero2) # 'XY' -> (X, Y)
    return coordenadas

def desenhar(ficheiro) -> None:
    """Desenhar as trajetórias das coordenadas

    Args:
        ficheiro (_type_): ficheiro em modo de leitura onde estão as coordenadas
    """    
    coordenadas: list[str] = ficheiro.readlines()
    coordenadas: list[tuple[int]] = limparCoordenadas(coordenadas)

    turtle.pen(speed=1000)
    for coordenada in coordenadas:
        turtle.goto(coordenada)
    turtle.exitonclick()

def main() -> None:
    destino: str = "/home/tomm/Documents/University/IPRP/2024-11-12/coordenadas.txt"
    lerFicheiro = open(destino, 'r')
    escreverFicheiro = open(destino, 'w')
    numeroCoordenadas: int = perguntarCoordenadas()

    escreverCoordenadas(escreverFicheiro, numeroCoordenadas)
    desenhar(lerFicheiro)

if __name__ == '__main__':
    main()
