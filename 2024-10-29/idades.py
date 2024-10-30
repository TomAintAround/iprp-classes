# Exercício 6.1 - 6.6

def perguntar(frase: str) -> int:
    valor = int(input(frase).strip())
    if valor <= 0:
        print('Insire um número natural.')
        return perguntar(frase)
    else:
        return valor

def listaIdades(numeroDeAlunos: int) -> list:
    lista: list = []
    for numero in range(1, numeroDeAlunos + 1):
        idade: int = perguntar(f'Insire a idade do aluno nº {numero}: ')
        lista.append(idade)
    return lista

def main() -> None:
    numeroDeAlunos: int = perguntar('Insire o número de alunos da turma: ')
    idades: list = listaIdades(numeroDeAlunos)
    valorReferencia: int = perguntar('Insire um valor de referência: ')

    idadesInvertidas: list = idades[:]
    idadesInvertidas.reverse()

    idadesSemPrimeiroUltimo: list = idades[:]
    idadesSemPrimeiroUltimo.pop(0)
    idadesSemPrimeiroUltimo.pop(-1)

    idadesMenorReferencia: list = [x for x in idades if x < valorReferencia]

    idades17Anos: list = [x for x in idades if x == 17]

    print(f'1. Há {len(idades)} alunos.')
    print(f'2. Lista de idades: {idades}.')
    print(f'3. Lista de idades invertida: {idadesInvertidas}.')
    print(f'4. Lista de idades excluindo a primeira e a última: {idadesSemPrimeiroUltimo}.')
    print(f'5. A menor idade é {min(idades)} e a maior idade é {max(idades)}.')
    print(f'6. A soma de todas as idades é {sum(idades)}.')
    print(f'7. Lista de idades menores que {valorReferencia}: {[idadesMenorReferencia]}.')
    print(f'8. Há {len(idades17Anos)} alunos com 17 anos.')

if __name__ == '__main__':
    main()