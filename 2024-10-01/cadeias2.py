# Exercício 3.16

frase = str(input("Insira a sua frase abaixo.\n").strip())

for i in range(0, len(frase)):
    progresso = len(frase) - i - 1
    print(frase[progresso:len(frase)])