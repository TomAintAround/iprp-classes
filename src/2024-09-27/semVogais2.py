# Exercício 3.13

frase = str(input("Insira a sua frase abaixo.\n").strip())
vogais = 'AÁÀÂÃÄaáàâãäEÉÈÊẼËeéèêẽëIÍÌÎĨÏiíìîĩïOÓòÔÕÖoóòôõöUÚÙÛŨÜuúùûũü'

for i in range(0, len(vogais)):
    frase = frase.replace(vogais[i], " ")

print(frase)
