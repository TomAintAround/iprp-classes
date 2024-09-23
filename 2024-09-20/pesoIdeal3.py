def peso_homem(altura):
    return (72.7 * altura) - 58

def peso_mulher(altura):
    return (62.1 * altura) - 44.7

def peso_ideal(altura, sexo):
    if sexo == 0:
        return peso_homem(altura)
    else:
        return peso_mulher(altura)

sexo = 6
while sexo != 0 and sexo != 1:
    sexo = eval(input("Qual é o seu sexo (0 - Homem), 1 - Mulher)? "))

altura = 0
while altura <= 0:
    altura = eval(input("Qual é a sua altura? "))

if altura > 10:
    altura = altura / 100

print("O seu peso ideal é {:.2f} kg.".format(peso_ideal(altura, sexo)))