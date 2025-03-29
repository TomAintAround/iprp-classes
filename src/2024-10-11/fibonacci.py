# Exercício 5.20

numero = 0
while numero <= 0:
    numero = int(input('Escolhe um número natural: ').strip())

pnultimoNumero = 0
ultimoNumero = 0
fib = 1
while fib < numero:
    pnultimoNumero = ultimoNumero
    ultimoNumero = fib
    fib = pnultimoNumero + ultimoNumero

if numero == fib:
    print('{} pertence à sequência de Fibonacci.'.format(numero))
else:
    print('{} não pertence à sequência de Fibonacci.'.format(numero))
