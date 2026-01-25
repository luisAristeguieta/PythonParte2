import random

print("Juego Dados");

input("Lanazar dos dados, presione la tecla enter");
lanzamientoDado1 = random.randint(1,6);
lanzamientoDado2 = random.randint(1,6);
sumaLanzamientos = lanzamientoDado1 + lanzamientoDado2;
print(f"Ha obtenido: <{lanzamientoDado1}>, y: <{lanzamientoDado2}> y el total es: <{sumaLanzamientos}>");

# Uso de operador Ternario: valor_si_verdadero if condicion else valor_si_falso // 
print("Te salvaste") if sumaLanzamientos >= 8 else print("Lo siento no es tu día de suerte, no te salvas");
