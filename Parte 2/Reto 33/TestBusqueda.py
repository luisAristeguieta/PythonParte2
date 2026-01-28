from transporte import buscarEstudiante

estudiantes=["1-Juan-Perez-9","2-Rosario-Tijeras-10","1-Chito-Vera-10","1-Ricardo Lopez-10","2-John-Cena-10"]

print(f"Estudiantes: {estudiantes}")

encontrado=buscarEstudiante(estudiantes,1,10)
print(f" EL PRIMER ESTUDIANTE DEL CURSO 1, CON NOTA 10, es: {encontrado}")