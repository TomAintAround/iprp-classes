# DESAFIO 3, 15/11/2024

def removerEspaçosExtra(frase):
    spaceCount = 0
    for i, letra in enumerate(frase):
        if letra.isspace():
            spaceCount += 1
        else:
            if spaceCount not in (0, 1):
                frase = frase.replace(" " * spaceCount, " ", 1)     
            spaceCount = 0
    return frase

def contarVogais(frase):
    vogais = 'aeiou'
    stats = dict()
    for vogal in vogais:
        stats[vogal] = frase.count(vogal)
    return stats

if __name__ == '__main__':
    frase = input().strip()
    frase = removerEspaçosExtra(frase)
    stats = contarVogais(frase)

    for chave in sorted(stats):
        print(f" {chave} : {stats[chave]} ", end=",")
    print()
