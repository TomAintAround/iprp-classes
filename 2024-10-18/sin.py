# Exerício 5.12

from math import pow, factorial

def meuSin(angulo, precisao):
    sin = 0
    precisaoAtual = 10000000000
    i = 0
    while precisaoAtual > precisao:
        ultimoSin = sin
        termo = (pow(-1, i) * pow(angulo, (2 * i + 1))) / factorial(2 * i + 1)
        sin += termo
        precisaoAtual = abs(sin - ultimoSin)
        i += 1

    return sin

angulo = eval(input('Insire o ângulo em radianos: ').strip())

precisao = -1
while precisao <= 0:
    precisao = eval(input('Insire a precisão: ').strip())

print(meuSin(angulo, precisao))