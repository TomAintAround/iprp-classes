# Exercício 5.11    

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def inputNumero(numero):
    if numero < 0:
        numero = int(input('Selecione um número inteiro ou 0: ').strip())
        return inputNumero(numero)
    else:
        return numero

numeroInvalido = -1
numero = inputNumero(numeroInvalido)

print('O factorial de {0} é {1}.'.format(numero, factorial(numero)))