# Exercício 5.15

from math import factorial

precisao = 0
while precisao <= 0:
    precisao = int(input('Escola um número natural. Quanto maior for, maior será a precisão: ').strip())

e = 0
for i in range(precisao):
    e += 1 / factorial(i)

print('O número aproximado de e é:\n{}'.format(e))