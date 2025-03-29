# Exercício 4.13

print("{0}{1:>15}\n---------------------".format('Milhas', 'Quilómetros'))
for i in range(10, 21):
    print('{0:>6.2f}{1:>15.2f}'.format(i, i * 1.609))
