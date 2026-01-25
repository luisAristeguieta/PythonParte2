from utilNotas import calcularTotal

for numFaltas in range(8):
    total=calcularTotal(5,5,10,numFaltas)
    print(f"FALTAS: {numFaltas} ---> Nota 4: {total}")