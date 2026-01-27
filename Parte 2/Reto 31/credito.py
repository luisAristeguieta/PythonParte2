def calcularInteresSimple(monto, plazo, tasa):
    return (monto * tasa/100)*plazo

def calcularInteresCompuesto(monto, plazo, tasa):
    return round(((monto)*((1+(tasa/100))**plazo)) - monto ,2)

def calcularCuota(monto, tasa, plazo):
    return round(monto * ((1 + tasa / 100) ** plazo * tasa / 100) / ((1 + tasa / 100) ** plazo - 1),2)

