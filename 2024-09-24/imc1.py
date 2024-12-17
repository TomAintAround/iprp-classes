# Exercício 1.9

import math

peso = eval(input("Qual é o seu peso? "))
altura = eval(input("Qual é a sua altura? "))

if altura >= 10:
    altura = altura / 100

imc = peso / math.pow(altura, 2)

print("O seu IMC é de {:.2f}.".format(imc))
