# Exercício 5.14

from math import log1p

def numeroHarmonico(numero):
    return log1p(numero - 1) + gamma

def inputNumero(numero):
    if numero < 1:
        numero = int(input('Insire um número natural: ').strip())
        return inputNumero(numero)
    else:
        return numero

gamma = 0.5772156649
numeroHarmonico = lambda n: log1p(n - 1) + gamma
    
numeroInvalido = 0
numero = inputNumero(numeroInvalido)

print('O número harmónico de {0} é {1}.'.format(numero, numeroHarmonico(numero)))