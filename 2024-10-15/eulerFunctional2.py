# Exercício 5.15

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def euler(n):
    formula = 1 / factorial(n)
    if n == 0:
        return formula
    else:
        return formula + euler(n - 1)

def pergunta(n):
    if n < 0:
        precisao = int(input('Escola um número natural ou 0. Quanto maior for, maior será a precisão: ').strip())
        return pergunta(precisao)
    else:
        return euler(n)

'''
Este número é inválido para o problema e ao chamar a função pergunta()
com este número vai fazer esta função pedir um número novamente
'''
numeroInvalido = -1

e = pergunta(numeroInvalido)

print('O número aproximado de e é:\n{}'.format(e))
