# Exercício 1.11

from math import pow, pi

raio = eval(input("Qual é o raio da base do cone (em cm)? "))
altura = eval(input("Qual é a altura do cone (em cm)? "))

volume = ( pi * pow(raio, 2) * altura ) / 3

print("O volume do cone é de {:.2f} cm³".format(volume))
