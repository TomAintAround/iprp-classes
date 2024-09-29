# Exercício 3.2

from math import sqrt

a = eval(input("Qual é o comprimento do lado \"a\" do triângulo? ").strip())
b = eval(input("Qual é o comprimento do lado \"b\" do triângulo? ").strip())
c = eval(input("Qual é o comprimento do lado \"c\" do triângulo? ").strip())

s = (a + b + c) / 2

area = sqrt(s * (s - a) * (s - b) * (s - c))

print("A área é {:.2f}.".format(area))