from funciones import calcularDescuento,calcularPrecioFinal

valorDescuento1=calcularDescuento(50,40)
valorFinal1=calcularPrecioFinal(50,40)
print(f"Para un producto que cuesta USD 50, el descuento del 40% es {valorDescuento1} , por lo tanto debe pagar {valorFinal1}")

valorDescuento2=calcularDescuento(80,25)
valorFinal2=calcularPrecioFinal(80,25)
print(f"Para un producto que cuesta USD 80, el descuento del 25% es {valorDescuento2} , por lo tanto debe pagar {valorFinal2}")

valorDescuento3=calcularDescuento(77,15)
valorFinal3=calcularPrecioFinal(77,15)
print(f"Para un producto que cuesta USD 77, el descuento del 15% es {valorDescuento3} , por lo tanto debe pagar {valorFinal3}")
