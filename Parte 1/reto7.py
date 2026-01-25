nombreUsuario = input("Ingrese su nombre");
edadUsuario = input("Ingrese su Edad");
nombreAmigo = input("Ingrese el nombre de una amigo");
edadAmigo = input("Ingrese la Edad de una amigo");
comentarioANumero = int (input("Valor probado")) # Esto es una prueba si al colocarlo asi, puedo colocar un numero

resultadoSuma =  int(edadUsuario) + int(edadAmigo);
diferenciaEdades =  int(edadUsuario) - int(edadAmigo);
print(f"La suma de las edades de {nombreUsuario} y {nombreAmigo} es: {resultadoSuma}");
print(f"La diferencia de las edades de {nombreUsuario} y {nombreAmigo} es: {diferenciaEdades}");
print (f"{comentarioANumero}")