def calcularTotal(lista) : 
    sumaTotal = 0
    for numero in range(len(lista)):
        sumaTotal += lista[numero]
    return sumaTotal

def validarListas(listaOrigen, listaDestino):
    return calcularTotal(listaOrigen) == calcularTotal(listaDestino)

def resolverProblema2 (listaOrigen, listaDestino):
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



def recuperarCurso (infoEstudiantes):
    listaEstudiante = infoEstudiantes.split("-")
    return int(listaEstudiante[0])

def recuperarNombreCompleto (infoEstudiantes):
    listaEstudiante = infoEstudiantes.split("-")
    return f" {listaEstudiante[1]} {listaEstudiante[2]}"

def recuperarNota (infoEstudiantes):
    listaEstudiante = infoEstudiantes.split("-")
    return int(listaEstudiante[3])

def buscarEstudiante (listaEstudiante, numeroCurso, nota): 
    for estudiante in range(len(listaEstudiante)):
        infoEstudiante = listaEstudiante[estudiante]
        if numeroCurso == recuperarCurso(infoEstudiante) and nota == recuperarNota(infoEstudiante):
            break
    return recuperarNombreCompleto(infoEstudiante)
    