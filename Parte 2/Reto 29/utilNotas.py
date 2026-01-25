
def buscarEstudiante (cedula,arrayEstudiantes):
    for est in arrayEstudiantes:
        divisionEstudiantes = est.split("#")
        if divisionEstudiantes[0] == cedula:
            return divisionEstudiantes
    return None