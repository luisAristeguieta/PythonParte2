
def determinarResultadosIMC (imc):
    if imc >=0 and imc < 16 :
        return "Delgadez Severa";
    if imc >= 16 and imc < 17 :
        return "Delgadez Moderada";
    if imc >= 17 and imc < 18.5 :
        return "Delgadez Leve";
    if imc >= 18.5 and imc < 25 :
        return "Peso Normal";
    if imc >= 25 and imc < 30 :
        return "Sobrepeso";
    if imc >= 30 and imc < 35 :
        return "Obesidad Grado 1";
    if imc >= 35 and imc < 40 :
        return "Obesidad Grado 2";
    if imc >= 40 :
        return "Obesidad Grado 3";
    return "IMC Fuera de Rango"

def encontrarMayor(valor1,valor2,valor3):
    mayorActual = valor1;

    if valor2 > mayorActual:
        mayorActual = valor2;

    if valor3 > mayorActual:
        mayorActual = valor3;
    
    return mayorActual;

def encontrarMenor(valor1,valor2,valor3,valor4):
    menorActual = valor1;

    if valor2 < menorActual:
        menorActual = valor2;

    if valor3 < menorActual:
        menorActual = valor3;
    
    if valor4 < menorActual:
        menorActual = valor4;
    
    return menorActual;

def calcularEdad (anioNacimiento):
    anioActual = 2026;
    # Uso de operador Ternario: valor_si_verdadero if condicion else valor_si_falso
    return (anioActual - anioNacimiento) if (anioNacimiento >= 0 and anioNacimiento <= anioActual) else (-1);

def calcularCuota (monto,interesAnual,numeroMeses):
    return (monto * (interesAnual / 12 / 100)) / (1 - (1 + (interesAnual / 12 / 100)) ** (-numeroMeses))