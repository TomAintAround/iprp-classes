# Exercício 4.12

from math import pow

numDeNumeros = int(input("Quantos números naturais quer elevar a dois? ").strip())

print("{0}{1:>10}".format('Número', 'Quadrado'))
for i in range(1, numDeNumeros + 1):
    print('{0:>6}{1:>10}'.format(i, int(pow(i, 2))))
