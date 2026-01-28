def calcularTotal(lista) : 
    sumaTotal = 0
    for numero in range(len(lista)):
        sumaTotal += lista[numero]
    return sumaTotal

def validarListas(listaOrigen, listaDestino):
    return calcularTotal(listaOrigen) == calcularTotal(listaDestino)

def resolverProblema (listaOrigen, listaDestino):
    movimientos = []
    for indiceDestino in range(len(listaDestino)):
        for indiceOrigen in range(len(listaOrigen)):
            destino = listaDestino[indiceDestino]
            if destino == 0:
                break
            origen = listaOrigen[indiceOrigen]
            
            if origen > 0:
            #mensaje = f"destino:{destino} - origen:{origen}" Parte del paso 3
            #movimientos.append(mensaje)
            #print(mensaje)

                cantidadMovimiento = destino if destino < origen else origen
            
                movimientos.append(f"{indiceOrigen} - {indiceDestino} - {cantidadMovimiento}")            

                listaOrigen[indiceOrigen] -= cantidadMovimiento
                listaDestino[indiceDestino] -= cantidadMovimiento
            
    return movimientos