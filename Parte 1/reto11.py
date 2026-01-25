import random

print("SI OBTIENES UN VALOR MAYOR O IGUAL A 8 GANAS")
input("PRESIONE LA TECLA ENTER PARA LANZAE LOS DADOS")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print(f"Ha obtenido {dado1} y {dado2}")

total = dado1 + dado2

print(f"Ha obtenido:  {dado1} y {dado2}, total:  {total}")


if total <= 8:
    print("Lo siento no es tu día de suerte, no te salvas")