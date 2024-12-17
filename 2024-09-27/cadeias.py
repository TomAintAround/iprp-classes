# Exercício 3.14

frase = str(input("Insira a sua frase abaixo.\n").strip())
comprimento = int(input("Insira o comprimento das cadeias: ").strip())

for i in range(0, len(frase) - comprimento + 1):
    progresso = i + comprimento
    print(frase[i:progresso])
