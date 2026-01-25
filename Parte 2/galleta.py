import random

def generarFortuna():
    valorRandom = random.randint(1,5);
    if valorRandom == 1:
        print("Ganarás un carro");
    elif valorRandom == 2:
        print("Los astros estan contigo");
    elif valorRandom == 3:
        print("Vienen buen tiempo en tu trabajo");
    elif valorRandom == 4:
        print("En los proximos ganarás una membresia");
    elif valorRandom == 5:
        print("Algo espectacular llegará a tu vida");