# Exercício 1.9

from math import pow

def imc(peso, altura):
    return peso / pow(altura, 2)

peso = eval(input("Qual é o seu peso? "))
altura = eval(input("Qual é a sua altura? "))

if altura >= 5:
    altura = altura / 100

print("O seu IMC é de {:.2f}.".format(imc(peso, altura)))