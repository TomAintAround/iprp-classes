altura = eval(input("Qual a sua altura (em metros) ? "))
sexo = eval(input("Qual o seu sexo (0 - Homem, 1 - Mulher) ? "))

if sexo == 0:
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print("O seu peso ideal é {:.2f}.".format(peso_ideal))