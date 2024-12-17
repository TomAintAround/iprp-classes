# Exerício 5.12

from math import pow, factorial,sin

def meuSin(angulo: float, iterador: int, precisao: float, sinAnterior: float) -> float:
    parcela: float = lambda x, j: (pow(-1, j) * pow(x, (2 * j + 1))) / factorial(2 * j + 1)
    sin: float = parcela(angulo, iterador)
    novaPrecisao: float = abs(sin - sinAnterior)

    if novaPrecisao > precisao:
        return sin + meuSin(angulo, iterador + 1, precisao, sin)
    else:
        return sin

def perguntaPrecisao(precisao: float) -> float:
    if precisao < 0:
        novaPrecisao: float = float(input('Insire a precisão (um número natural ou 0): ').strip())
        return perguntaPrecisao(novaPrecisao)
    else:
        return precisao

def main() -> None:
    numeroInvalido: float = -1.0
    angulo: float = float(input('Insire o ângulo em radianos: ').strip())
    precisao: float = perguntaPrecisao(numeroInvalido)

    print(meuSin(angulo, 0, precisao, 0.0))

if __name__ == '__main__':
    main()
