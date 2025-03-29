# DESAFIO 2, 25/10/2024

from math import floor

def harmonica(n):
    resultado = 0
    for i in range(1, n + 1):
        resultado += 1 / i
    return resultado

x: int = int(input())

index: int = 1
resultado = 1
while resultado != 0:
    resultado: int = floor(harmonica(index) * 100000) % x
    index += 1
print(index - 1)
