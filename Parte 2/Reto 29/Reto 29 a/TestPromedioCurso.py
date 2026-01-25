from utilNotas import calcularPromedioCurso

estudiantes=[
    "1714616123#Santiago#Mosquera#10#10#10#0#10",
    ]

resultado=calcularPromedioCurso(estudiantes)
print(f"Promedio1: {resultado}")
estudiantes.append("1714616112#Roberto#Mosquera#5#5#10#0#7.5")
resultado=calcularPromedioCurso(estudiantes)
print(f"Promedio2: {resultado}")
estudiantes.append("1714616112#Roberto#Mosquera#5#5#10#3#7.25")
resultado=calcularPromedioCurso(estudiantes)
print(f"Promedio2: {resultado}")