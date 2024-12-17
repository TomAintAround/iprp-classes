# Exercício 6.6

from collections.abc import Callable

class Pergunta:
    def __init__(self, frase, erro, condicao):
        self.frase: str = frase
        self.erro: str = erro
        self.condicao: Callable[[int], bool] = condicao

    def perguntar(self) -> int:
        valor: int = int(input(self.frase).strip())
        if self.condicao(valor):
            return valor

        print(self.erro)
        return self.perguntar()

def numeroElemento(limite: int, posicao: int = 0, numeros: list = []) -> list:
    if posicao < limite:
        numero: int = Pergunta(f'Insire o número do elemento da posição {posicao + 1}: ', '', lambda x: True).perguntar()
        return numeroElemento(limite, posicao + 1, numeros + [numero])
    
    return numeros

def somaComulativa(lista: list, limite: int, posicao: int = 0) -> int:
    if posicao < limite:
        return lista[posicao] + somaComulativa(lista, limite, posicao + 1)

    return lista[posicao]

def fazerLista(lista: list, posicao: int = 0, novaLista: list = []) -> list:
    if posicao < len(lista):
        numero: int = somaComulativa(lista, posicao)
        return fazerLista(lista, posicao + 1, novaLista + [numero])
    
    return novaLista

def main() -> None:
    limiteLista: Pergunta = Pergunta('Insire o comprimento da lista: ', 'Insire um número natural.', lambda x: x > 0).perguntar()
    lista: list = numeroElemento(limiteLista)
    print(f'A sua lista: {lista}\nA nova lista: {fazerLista(lista)}')

if __name__ == '__main__':
    main()
