def conta_consoantes_unicas(frase):
    frase = frase.lower()
    consoantes = 'bcdfghjklmnpqrstvwxyz'

    count = 0
    usados = ''
    for letter in frase:
        if letter in consoantes and letter not in usados:
            count += 1
            usados += letter

    return count

print(conta_consoantes_unicas("abbccddeeff"))
