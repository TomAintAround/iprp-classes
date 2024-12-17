# Exercício 5.9

import random

numeroDeLancamentos = 0
while numeroDeLancamentos <= 0:
    numeroDeLancamentos = int(input('Insire o número de lançamentos do dado: ').strip())

numerosPares = 0
for i in range(numeroDeLancamentos):
    if random.randint(1,6) % 2 == 0:
        numerosPares += 1

percentagemNumerosPares = numerosPares / numeroDeLancamentos * 100
print('A percentagem de receber um número par é {:.2f}.'.format(percentagemNumerosPares))
