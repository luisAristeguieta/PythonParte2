def calcularPromedio (nota1,nota2,nota3): 
    return (nota1 + nota2 + nota3 )/3;

def consultarMulta (tipoMulta):

    if tipoMulta < 1 or tipoMulta > 4 :
        return -1;
    else:
        if tipoMulta == 1 :
            return 10;
        if tipoMulta == 2 :
            return 15;
        if tipoMulta == 3 :
            return 20;
        if tipoMulta == 4 :
            return 30;

def calcularValorHora(salario):
    return salario / 160;

def calcularSubtotal(precioProducto, cantidad, porcentajeDescuento):
    return (cantidad * precioProducto) - ((cantidad * precioProducto) * (porcentajeDescuento/100));

def calcularValorDescuento(precio, porcentajeDescuento):
    return (precio * (porcentajeDescuento/100));