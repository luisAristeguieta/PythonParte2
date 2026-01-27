def calcularIVA (precio): 
    return round((precio*0.15),2)

def calcularAporteEmpleado (sueldo): 
    return round((sueldo*0.0945),2)

def calcularAporteEmpresa (sueldo): 
    return round((sueldo*0.0121),2)

def calcularDescuento(precio,porcentaje):
    return round((precio*porcentaje/100),2)

def calcularPrecioFinal(precio,porcentaje):
    return round((precio -(precio*porcentaje/100)),2)