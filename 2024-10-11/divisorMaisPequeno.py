# Exercício 5.8

from math import sqrt

numeroInicial = 1
while numeroInicial <= 1:
    numeroInicial = int(input('Escolhe um número natural maior do que 1: ').strip())

for possivelDivisor in range(int(sqrt(numeroInicial)), 1, -1):
    if numeroInicial % possivelDivisor == 0:
        divisor = possivelDivisor

try:
    divisor
    print('O menor divisor de {0} (que não é 1) é {1}.'.format(numeroInicial, divisor))
except NameError:
    print('Como {0} é um número primo, o seu menor divisor é 1.'.format(numeroInicial))