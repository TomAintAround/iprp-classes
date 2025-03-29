# Exercício 3.3

from math import pi, sin


alt = 0
while alt <= 0:
    alt = eval(input("Qual é a altura (em metros) que pretende que a escada alcance? ").strip())

ang = 0
while ang <= 0 or ang >= 90:
    ang = eval(input("Qual é o ângulo (em graus) que pretende que a escada faça com o solo? ").strip())

ang = pi / 180 * ang

comp = alt / sin(ang)

print("O comprimento da escada deve ser {:.2f} metros.".format(comp))
