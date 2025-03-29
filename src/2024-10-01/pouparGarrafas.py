# Exercício 1.15

garrafas = [5, 1.5, 0.5, 0.25, 0]
capacidade = eval(input("Qual é a quantidade de água que quer armazenar? ").strip())

listaDeGarrafas = []
for i, j in zip(garrafas, garrafas[1:]):
    while capacidade > 0:
        listaDeGarrafas += [i]
        capacidade -= i

    if capacidade == 0:
        break
    elif j < capacidade + i:
        break
    elif i != 0.25:
        capacidade += i
        listaDeGarrafas.pop()

print("Precisa de {} garrafas de 5 litros, {} garrafas de 1.5 litros, {} garrafas de 0.5 litros e {} garrafas de 0.25 litros.".format(listaDeGarrafas.count(5), listaDeGarrafas.count(1.5), listaDeGarrafas.count(0.5), listaDeGarrafas.count(0.25)))
