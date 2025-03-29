# Exercício 1.8

import math

comprimentoHamburgerQuadrado = 7.62
diametroHamburgerRedondo = 8.89

tamanhoHamburgerQuadrado = math.pow(comprimentoHamburgerQuadrado, 2)
tamanhoHamburgerRedondo = math.pi * math.pow((diametroHamburgerRedondo / 2), 2)

print("Tamanho do hamburger quadrado: {:.2f} cm².".format(tamanhoHamburgerQuadrado))
print("Tamanho do hamburger redondo: {:.2f} cm².".format(tamanhoHamburgerRedondo))

diferenca = tamanhoHamburgerQuadrado - tamanhoHamburgerRedondo

if tamanhoHamburgerQuadrado < tamanhoHamburgerRedondo:
    print("Foi enganado! Tem razões para protestar!")
elif tamanhoHamburgerQuadrado == tamanhoHamburgerRedondo:
    print("Não foi enganado. Não tem razões para protestar. Têm o mesmo tamanho")
else:
    print("O hamburger ficou maior! Não deve protestar.")
