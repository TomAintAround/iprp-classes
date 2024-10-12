# Exercício 5.7

palavra1 = 'qwerty'
palavra2 = 'qwertyuiop'
while len(palavra1) != len(palavra2):
    palavra1 = input('Insire a primeira palavra: ').strip()
    palavra2 = input('Insire a segunda palavra (com o comprimento igual à primeira): ').strip()

palavrasDiferentes = 0
for letra in range(len(palavra1)):
    if palavra1[letra] != palavra2[letra]:
        palavrasDiferentes += 1

if palavrasDiferentes / len(palavra1) < 0.10:
    print('São palavras amigas.')
else:
    print('Não são palavras amigas.')