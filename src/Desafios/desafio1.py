# DESAFIO 1, 11/10/2024

numero = input()

num1 = int(numero[0])
num2 = int(numero[1])
num3 = int(numero[2])
somaDosDigitos = (num1 + num2 + num3) % 2 == 0
print(somaDosDigitos)
