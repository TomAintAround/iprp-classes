# Exercício 5.17

numeroDeSequencias = int(input('Insire o número de sequências: ').strip())

print('Padrão A:')
for numero in range(1, numeroDeSequencias + 1):
    for progresso in range(1, numero + 1):
        print(progresso, end=' ')

    print('')


print('\nPadrão B:')
for numero in range(numeroDeSequencias, 0, -1):
    for progresso in range(1, numero + 1):
        print(progresso, end=' ')

    print('')

print('\nPadrão C:')
for numero in range(1, numeroDeSequencias + 1):
    for progresso in range(numero, 0, -1):
        alinhamento = 2 * (numeroDeSequencias - numero + 1) - 1

        if progresso == numero:
            print('{0:>{1}}'.format(progresso, alinhamento), end=' ')
        else:
            print(progresso, end=' ')

    print('')
