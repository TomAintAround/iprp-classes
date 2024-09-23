# Exercício 1.8

import math

comprimentoHamburgerQuadrado = 7.62
diametroHamburgerRedondo = 8.89

volumeHamburgerQuadrado = math.pow(comprimentoHamburgerQuadrado, 3)
volumeHamburgerRedondo = 4 / 3 * math.pi * math.pow((diametroHamburgerRedondo / 2), 2)

diferencaVolume = volumeHamburgerQuadrado - volumeHamburgerRedondo

if volumeHamburgerQuadrado < volumeHamburgerRedondo:
    print("Foi enganado! Tem razões para protestar! A diferença de volume é de {:.2f} cm cúbicos.".format(round(diferencaVolume, 2)))
elif volumeHamburgerQuadrado == volumeHamburgerRedondo:
    print("Não foi enganado. Não tem razões para protestar. Têm o mesmo volume")
else:
    print("O hamburger ficou maior! Invés de protestar, deve agradecer! A diferença de volume é de {:.2f} cm cúbicos.".format(round(diferencaVolume, 2)))
