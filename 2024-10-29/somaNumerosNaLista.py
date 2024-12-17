# Exercício 6.2

def main() -> None:
    lista: list = [1, 5, 8, 3, 66, 3, 5, 7, 634, 63456, 6, 63, 2]
    somaDePares: int = sum([x for x in lista if x % 2 == 0])
    somadeImpares: int = sum([x for x in lista if x % 2 != 0])
    print((somaDePares, somadeImpares))

if __name__ == '__main__':
    main()
