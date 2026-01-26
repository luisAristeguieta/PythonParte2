def calcularProbabilidadGanar(cartas, cartaMenor, cartaMayor):
    valorMenor = obtenerValorCarta(cartaMenor)
    valorMayor = obtenerValorCarta(cartaMayor)

    cartasGanadoras = 0

    for carta in cartas:
        valorCarta = obtenerValorCarta(carta)
        if valorMenor < valorCarta < valorMayor:
            cartasGanadoras += 1

    totalCartas = len(cartas)

    if totalCartas == 0:
        return 0

    probabilidad = (cartasGanadoras / totalCartas) * 100

    return round(probabilidad, 2)

def obtenerValorCarta(secuenciaCarta):
    listaCarta = secuenciaCarta.split("-")
    return float(listaCarta[3])