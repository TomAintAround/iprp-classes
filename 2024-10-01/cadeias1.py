# Exercício 3.15

frase = str(input("Insira a sua frase abaixo.\n").strip())

for i in range(0, len(frase)):
    progresso = i + 1
    print(frase[:progresso])