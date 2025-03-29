# Exercício 6.5

from random import randint

def perguntar(frase: str) -> int:
    valor: int = int(input(frase).strip())
    if valor > 0:
        return valor
    else:
        print('Insire um número natural.')
        return perguntar(frase)

def lancamentoDados(numeroDeLancamentos: int, lista: list = []) -> list:
    if numeroDeLancamentos > 0:
        lancamento1: int = randint(1, 6)
        lancamento2: int = randint(1, 6)
        soma: int = lancamento1 + lancamento2
        lista.append(soma)
        return lancamentoDados(numeroDeLancamentos - 1, lista)
    else:
        return lista

def percentagemNumerosPares(listaDeLancamentos: list) -> float:
    somaNumerosPares: int = sum([x for x in listaDeLancamentos if x % 2 == 0])
    return somaNumerosPares / sum(listaDeLancamentos) * 100

def main() -> None:
    numeroDeLancamentos: int = perguntar('Insire o número de lançamentos: ')
    listaDeLancamentos: list = lancamentoDados(numeroDeLancamentos)

    print(listaDeLancamentos)
    print(f'A percentagem de números pares é {percentagemNumerosPares(listaDeLancamentos):.2f}%.')

if __name__ == '__main__':
    main()
