# Exercício 3.13

frase = 'A vida é uma constante oscilação entre a ânsia de ter e o tédio de possuir.'
vogais = 'AÁÀÂÃÄaáàâãäEÉÈÊẼËeéèêẽëIÍÌÎĨÏiíìîĩïOÓòÔÕÖoóòôõöUÚÙÛŨÜuúùûũü'

'''
novaFrase = ''
for i in range(0, len(frase)):
    if frase[i] == 'a':
        letra = ' '
    else:
        letra = frase[i]
    novaFrase = novaFrase + letra

print(novaFrase)
'''

'''
for i in range(0, len(frase)):
    if frase[i] in vogais:
        letra = ' '
    else:
        letra = frase[i]
    print(letra, end="")
'''

for i in range(0, len(vogais)):
    frase = frase.replace(vogais[i], " ")

print(frase)