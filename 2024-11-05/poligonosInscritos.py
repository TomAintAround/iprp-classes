from math import sin, cos, pi

def maiores_90_circulo(minLados: int, maxLados: int) -> list:
    ladosValidos: list = []
    areaCirculo: float = pi

    for lado in range(minLados, maxLados + 1):
        areaPoligono: float =  lado * cos(pi / lado) * sin(pi / lado)

        if areaPoligono > 0.9 * areaCirculo:
            ladosValidos.append(lado)
    
    return ladosValidos

def main() -> None:
    ladosValidos: list = maiores_90_circulo(3, 15)
    print('Polígonos com área maior do que 90% da área do círculo:')
    for lado in ladosValidos:
        print(f'Polígono com {lado} lados')

if __name__ == '__main__':
    main()