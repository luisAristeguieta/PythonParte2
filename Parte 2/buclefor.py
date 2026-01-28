array = [0,10,20,30,40,50]

# Repaso de bucle for, sintexis en python: 

# print(f"El array es de longitud fija: {len(array)}")

#for i in array:
#    print(i);

#for i in range (len(array)):
   # print(f"Se evalua el indice en: {i} y el valor en el array es {array[i]}")



# Practica bucles anidados: 

dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]
# Repaso de listas / funciones y ciclo for:

listaNueva = []

def practicaLista (lista1,lista2):
    for i1 in range(len(lista1)):
        for i2 in range(len(lista2)):
            valorLista1 = lista1[i1]
            valorLista2 = lista2[i2]
            #mensaje = print(f" el valor del indice es: {i1} y su valor en la lista usando range es: {valorLista1} // el valor del indice es: {i2} y su valor en la lista usando range es: {valorLista2}")
            listaNueva.append(f" i1 {i1} y l1 {valorLista1} // i2 {i2} y l2: {valorLista2}")
    return listaNueva

print(practicaLista(dado1,dado1))

# Con esta practica se ve el nivel de interaccion entre dos listas  y el retorno depende del nivel.
