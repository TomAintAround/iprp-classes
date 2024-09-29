# Exercício 3.16

frase = str(input("Insira a sua frase abaixo.\n").strip())

for i in range(0, len(frase) + 1):
    progresso = len(frase) - i
    segmento = ''
    while progresso < len(frase):
        segmento = segmento + frase[progresso]
        progresso = progresso + 1
    
    print(segmento)