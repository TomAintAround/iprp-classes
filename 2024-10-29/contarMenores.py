# Exercício 6.4

def main() -> None:
    lista: list = [6, 7, 5, 3, 7, 9, 6, 5, 7, 65, 2, 63, 97]
    numero: int = 8

    print(len([x for x in lista if x < numero]))

if __name__ == '__main__':
    main()