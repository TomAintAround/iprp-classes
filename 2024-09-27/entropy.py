# Exercício 3.7

from math import log

def sequence(p):
    return p * log(p, 2)

p1 = eval(input("Qual é o valor de p1? ").strip())
p2 = eval(input("Qual é o valor de p2? ").strip())

entropy = -1 * ( sequence(p1) + sequence(p2) )

print("O valor de entropia é {:.2f}.".format(entropy))