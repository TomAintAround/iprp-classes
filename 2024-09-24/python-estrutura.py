# Isto é um comentário.
# Os comentários nunca são executados pelo interpretador,
# e servem para documentar o código e ajudar na sua compreensão.



import math # Importar um módulo

# Definir Variáveis
# Na linha abaixo estar a atribuir o nome x ao objecto 10
x = 10
z = 1.2

# Operação Aritmética. Na linha abaixo manipulamos dois objetos através 
# da operação soma: o objeto 5 é somado ao objeto cujo 
# o nome é x (neste caso será o objeto 10).
# Ao objeto que resulta da soma é atribuído o nome resultado
resultado = x + 5

# Exemplo do if-else 
if z >= 10:
    print(x)
else:
    print(resultado)

# Definição de uma função com um parametro nome
def cumprimentar(nome):
    print("Olá, ", nome)

# Chamar a função com o argumento "Nuno"
cumprimentar("Nuno")