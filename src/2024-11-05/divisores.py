from math import sqrt

def perguntarValor() -> int:
    try:
        valor: int = int(input('Insire o valor: ').strip())

        if valor <= 0:
            raise ValueError
        else:
            return valor
    except ValueError:
        print('Insire um número natural.')
        return perguntarValor()

def main() -> None:
    valor: int = perguntarValor()
    divisores: list = []

    for numero in range(1, int(sqrt(valor) + 1)):
        if numero == sqrt(valor):
            divisores.append(numero)
            break

        if valor % numero == 0:
            outroNumero: int = int(valor / numero)
            divisores.append(numero)
            divisores.append(outroNumero)
    
    divisores.sort()
    print(divisores)

if __name__ == '__main__':
    main()
