# Exercício 6.3

def main() -> None:
    lista1: list = [1, 2, 3]
    lista2: list = ['a', 'b', 'c']
    
    listaFinal: list = []
    for i in range(len(lista1)):
        listaFinal.append(lista1[i])
        listaFinal.append(lista2[i])

    print(listaFinal)

if __name__ == '__main__':
    main()
