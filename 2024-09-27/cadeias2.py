# Exercício 3.15

frase = str(input("Insira a sua frase abaixo.\n").strip())

for i in range(0, len(frase)):
    progresso = 0
    segmento = ''
    while progresso < i:
        segmento = segmento + frase[progresso]
        progresso = progresso + 1
    
    print(segmento)