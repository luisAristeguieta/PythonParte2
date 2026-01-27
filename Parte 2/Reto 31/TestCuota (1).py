from credito import calcularCuota

resultado1=calcularCuota(10000,16,10)
print("RECIBE UN PRESTAMO DE 10 000, al 16% de interés anual, para pagar en 10 años")
print(f"    Debe pagar 10 cuotas de {resultado1}")

resultado2=calcularCuota(20000,15,3)
print("RECIBE UN PRESTAMO DE 20 000, al 15% de interés anual, para pagar en 3 años")
print(f"    Debe pagar 3 cuotas de {resultado2}")