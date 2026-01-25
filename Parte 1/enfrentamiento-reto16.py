import random

print("Juego de Puntajes entre 2 jugadores");

nombreJugador1 = input("Jugador 1, typea tu nombre");
nombreJugador2 = input("Jugador 2, typea tu nombre");

input(f"{nombreJugador1}, presione la tecla enter");
lanzamientoJugador1 = random.randint(1,6);
print(f"<{nombreJugador1}>, sacaste: <{lanzamientoJugador1}>");


input(f"{nombreJugador2}, presione la tecla enter");
lanzamientoJugador2 = random.randint(1,6);
print(f"<{nombreJugador2}>, sacaste: <{lanzamientoJugador2}>");

if lanzamientoJugador1 > lanzamientoJugador2 :
    print(f"El ganador es: {nombreJugador1}");
elif lanzamientoJugador2 > lanzamientoJugador1 :
    print(f"El ganador es: {nombreJugador2}");
else:
    print(f"El {nombreJugador1} y {nombreJugador2} están empatados..!");