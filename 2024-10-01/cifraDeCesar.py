# Exercício 3.20

def substituir(letra, distancia):
    if letra in minusculas:
        fazerFrase(minusculas, letra, distancia)
    elif letra in maiusculas:
        fazerFrase(maiusculas, letra, distancia)

def fazerFrase(capital, letra, distancia):
    novaFrase = ''
    novaLetra = (capital.index(letra) + distancia) % 26
    novaFrase += capital[novaLetra]
    print(novaFrase, end='')

frase = str(input("Insira a sua frase:\n").strip())
distancia = int(input("Insira a distância: ").strip())

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

novaFrase = ''
for letra in frase:
    if letra != ' ':
        substituir(letra, distancia)
    else:
        print(' ', end='')