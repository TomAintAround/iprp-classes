# Exercício 3.14

frase = str(input("Insira a sua frase abaixo.\n").strip())
comprimento = int(input("Insira o comprimento das cadeias: ").strip())

for i in range(0, len(frase) - comprimento + 1):
    progresso = 0
    segmento = ''
    while progresso < comprimento:
        segmento = segmento + frase[i + progresso]
        progresso = progresso + 1
    
    print(segmento)