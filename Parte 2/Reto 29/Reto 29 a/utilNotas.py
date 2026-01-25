
def buscarEstudiante (cedula,arrayEstudiantes):
    for est in arrayEstudiantes:
        divisionEstudiantes = est.split("#")
        if divisionEstudiantes[0] == cedula:
            return divisionEstudiantes
    return None

def calcularTotal (n1,n2,n3,faltas):
    n4 = 10;

    if faltas > 0 and faltas < 4:
        n4 = 9
    elif faltas == 4 or faltas == 5:
        n4 = 8
    elif faltas > 5:
        n4 = 7

    return round(((n1+n2+n3+n4 )/4 ),2)

def calcularPromedioCurso(listaEstudiantes):
    totalSuma = 0

    for est in listaEstudiantes:
        divisionEstudiantes = est.split("#")
        notaStr = divisionEstudiantes[7]
        nota = float(notaStr)
        totalSuma += nota
    return round((totalSuma/len(listaEstudiantes)),4)


  
