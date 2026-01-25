import random

print("PENINTENCIAS POR VALOR")
input("PRESIONE LA TECLA ENTER PARA LANZAR LOS DADOS")

dado = random.randint(1,6)
penitencia = " ";

if dado == 1:
    penitencia = "Penitencia 1 es : Salta"
elif dado == 2:
    penitencia = "Penitencia 2 es: Corre 100 m"
elif dado == 3:
    penitencia = "Penitencia 3 es: Baila"
elif dado == 4:
    penitencia = "Penitencia 4 es Aplaude 10 veces"
elif dado == 5:
    penitencia = "Penitencia 5 es: Mencionar una verdad incomoda"
elif dado == 6:
    penitencia ="Penitencia 6 es: Escribe una canción"

print(f"Ha obtenido el valor de: {dado} y la {penitencia}")
