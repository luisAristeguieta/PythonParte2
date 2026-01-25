edad = int (input("Ingresar el valor de su edad: "));
nombre = input("Ahora, ingrese su nombre: ");

# Se implementa un función:

def rangoDeEdades(edad):

    if edad >= 0 and edad <= 12:
        return " eres un niño";

    if edad > 12 and edad <= 17:
        return " eres un adolescente";

    if edad > 17 and edad <= 30:
        return " eres un adulto joven";

    if edad > 30 and edad <= 60:
        return " eres un adulto injoven";

    if edad > 60 and edad <= 120:
        return " eres un adulto mayor";
    
    return " su edad es incorrecta" 
        
print(nombre + rangoDeEdades(edad));