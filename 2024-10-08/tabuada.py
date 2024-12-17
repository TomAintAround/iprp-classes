# Exercício 4.14

numero = 11
while numero > 10:
    numero = int(input('Escola um número inteiro menor ou igual a 10: ').strip())

print('Tabuada do número {}\n---------------------'.format(numero))
for i in range(1, 11):
    print('{0} x {1:>2} = {2:>4}'.format(numero, i, numero * i))
