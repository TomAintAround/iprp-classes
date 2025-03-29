# Exercício 5.15

from math import factorial

precisao = -1
while precisao < 0:
    precisao = int(input('Escola um número natural ou 0. Quanto maior for, maior será a precisão: ').strip())

e = 0
for i in range(precisao + 1):
    e += 1 / factorial(i)

print('O número aproximado de e é:\n{}'.format(e))
