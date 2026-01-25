import random

print("Juego Piedra, Papel o Tijera \n Usuario Vs Ordenador");
print("El juego consiste en la eleccion de un número donde: \n Piedra = 1 \n Papel = 2 \n Tijera = 3");

miEleccion = int (input("Ingresar un valor entre 1 y 3"));
eleccionOrdenador = random.randint(1,3);
# Aplico una funcion recibiendo el parametro del numero: 
def asignacionSimbolo(numero):
    if numero == 1 : 
        return "Piedra";
    elif numero == 2:
        return "Papel";
    elif numero == 3:
        return "Tijera";

def ganador(miEleccion, eleccionOrdenador):

    if miEleccion == eleccionOrdenador:
        return "Nadie gana"

    if (miEleccion == 1 and eleccionOrdenador == 3) or \
       (miEleccion == 2 and eleccionOrdenador == 1) or \
       (miEleccion == 3 and eleccionOrdenador == 2):
        return "Felicidades, ganaste"

    return "Ganó el ordenador"


if miEleccion >= 1 and miEleccion <= 3 :
    print("Elegiste " + asignacionSimbolo(miEleccion));
    print("El ordenador eligió " + asignacionSimbolo(eleccionOrdenador));
    print (ganador (miEleccion,eleccionOrdenador));
else :
    print("Debe elegir un número entre 1 y 3");
