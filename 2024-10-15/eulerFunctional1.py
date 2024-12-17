# Exercício 5.15

def factorial(n):
    if n == 0:
        return 1
    
    r = n

    for i in range(1, n):
        r *= i
    
    return r

precisao = -1
while precisao < 0:
    precisao = int(input('Escola um número natural ou 0. Quanto maior for, maior será a precisão: ').strip())

e = 0
for i in range(precisao):
    e += 1 / factorial(i)

print('O número aproximado de e é:\n{}'.format(e))
