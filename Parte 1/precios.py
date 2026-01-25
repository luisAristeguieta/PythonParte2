nombreProducto = input("Ingrese el nombre del Producto");
precioProducto = input("Ingrese el valor del producto");
cantidad = input("Ingrese la cantidad de productos");

valorTotal =  float(precioProducto) * int(cantidad);

print(f"El valor a pagar por la cantidad de  {cantidad} y {nombreProducto} es: {valorTotal}");