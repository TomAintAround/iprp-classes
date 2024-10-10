# Exercício 4.15

acronimoCompleto = str(input("Insire o seu acrónimo: ").strip())

def acronimo(acronimo):
    for letra in acronimo:
        if letra.islower() or letra == ' ':
            acronimo = acronimo.replace(letra, '')
    
    return acronimo

print(acronimo(acronimoCompleto))