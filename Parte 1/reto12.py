import random

print("PRUEBA TU SUERTE");
print("SI OBTIENES UN VALOR IGUAL A 6 GANAS");
input("PRESIONE LA TECLA ENTER")
numeroAleatorio = random.randint(1,6);
print(numeroAleatorio);

if numeroAleatorio==6:
    print("FELICIDADES GANASTE");
    print("ESTAS DE SUERTE");
else:
    print("LO SIENTO NO ES TU DIA DE SUERTE");
