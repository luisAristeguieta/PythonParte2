from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utilNotas import *
#VARIABLES GLOBALES
estudiantes=[
    "1714616123#Santiago#Mosquera#10#2.6#8.5#0#7.77",
    "0814616123#Santiago#Ramos#9.5#2.6#8.5#0#7.65",
    "1614616123#Maritza#Ramos#8.3#2.6#7.2#0#7.5"
    ]


def limpiarErrores():
    lblErrorCedula.config(text="")
    lblErrorNombre.config(text="")
    lblErrorApellido.config(text="")
    lblErrorNota1.config(text="")
    lblErrorNota2.config(text="")
    lblErrorNota3.config(text="")
    lblErrorInasistencias.config(text="")


def buscar ():
    estudianteEncontrado = buscarEstudiante(txtCedula.get(),estudiantes)
    nuevo()
    limpiarErrores()
    if estudianteEncontrado != None:
            txtCedula.insert(0,estudianteEncontrado[0])
            txtNombre.insert(0,estudianteEncontrado[1])
            txtApellido.insert(0,estudianteEncontrado[2])
            txtNota1.insert(0,estudianteEncontrado[3])
            txtNota2.insert(0,estudianteEncontrado[4])
            txtNota3.insert(0,estudianteEncontrado[5])
            txtInasistencias.insert(0,estudianteEncontrado[6])
            lblTotal.config(text=f"{estudianteEncontrado[7]}")
            return
    messagebox.showinfo(title="Importante", message="Sin Registro")
    return

def guardar():
    limpiarErrores()

    if not validarVacios():
        return

    cedula = txtCedula.get()
    nombre = txtNombre.get()
    apellido = txtApellido.get()

    notas = convertirFloat()
    if notas is None:
        return
    
    nota1 = notas[0]
    nota2 = notas[1]
    nota3 = notas[2]

    faltas = txtInasistencias.get()

    try:
        numeroFaltas = int(faltas)
        if numeroFaltas < 0: 
            return lblErrorInasistencias.config(text="Solo valores mayores a 0")
    except ValueError:
        return lblErrorInasistencias.config(text="Solo valores numérico")
    
    notaPromedio = calcularTotal(nota1,nota2,nota3,numeroFaltas)


    estEncontrado = buscarEstudiante(cedula, estudiantes)
    if estEncontrado is None:
        estudiantes.append(f"{cedula}#{nombre}#{apellido}#{nota1}#{nota2}#{nota3}#{numeroFaltas}#{notaPromedio}")
        messagebox.showinfo(title="IMPORTANTE", message="Estudiante Guardado")
        nuevo()
    else:
        lblErrorCedula.config(text="Ya existe")


def convertirFloat():
    lblErrorNota1.config(text="")
    lblErrorNota2.config(text="")
    lblErrorNota3.config(text="")


    listaNotaStr = [txtNota1.get(), txtNota2.get(), txtNota3.get()]
    errores = [lblErrorNota1, lblErrorNota2, lblErrorNota3]
    notas = []

    for i in range(3):
        try:
            nota = float(listaNotaStr[i])
        except ValueError:
            errores[i].config(text="Solo valores numérico")
            return None

        if nota < 0 or nota > 10:
            errores[i].config(text="Rango entre 0 a 10")
            return None

        notas.append(nota)

    return notas


def validarVacios():
    listaEntradas = [txtCedula.get(), txtNombre.get(), txtApellido.get(),txtNota1.get(), txtNota2.get(), txtNota3.get(), txtInasistencias.get()]
    listaErrores = [lblErrorCedula, lblErrorNombre, lblErrorApellido,lblErrorNota1, lblErrorNota2, lblErrorNota3, lblErrorInasistencias]

    hayError = False

    for i in range(len(listaEntradas)):
        if listaEntradas[i] == "":
            listaErrores[i].config(text="Requerido")
            hayError = True

    return not hayError


def validarInasistencia(faltas) :
    try:
        numeroFaltas = float(faltas)
        if numeroFaltas == 0:
            return 10
        if numeroFaltas > 0 and numeroFaltas < 4:
            return 9
        if numeroFaltas > 0 and numeroFaltas < 4:
            return 9
        if numeroFaltas == 4 and numeroFaltas == 5:
            return 8
        if numeroFaltas > 5:
            return 7
        lblErrorInasistencias.config(text="Valor debe ser mayor a 0")
        return None
    except ValueError:
        lblErrorInasistencias.config(text="Solo valores numérico")
        return None
    
     
def nuevo ():
    txtCedula.delete(0,END)
    txtNombre.delete(0,END)
    txtApellido.delete(0,END)
    txtNota1.delete(0,END)
    txtNota2.delete(0,END)
    txtNota3.delete(0,END) 
    txtInasistencias.delete(0,END)
    lblTotal.config(text="0.00")

#GRAFICA
ventana=Tk()
ventana.title("NOTAS")
ventana.geometry("600x400")
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)
tabControl.add(tab1,text="REGISTRO")
tabControl.add(tab2,text="LISTA")
tabControl.add(tab3,text="BUSQUEDA")
tabControl.pack(expand = 1, fill ="both") 
#TAB REGISTRO
frRegistro= Frame(tab1)
frRegistro.place(x=100,y=100)
lblCedula=ttk.Label(frRegistro,text="CEDULA:")
lblNombre=ttk.Label(frRegistro,text="NOMBRE:")
lblApellido=ttk.Label(frRegistro,text="APELLIDO:")
lblNota1=ttk.Label(frRegistro,text="NOTA 1:")
lblNota2=ttk.Label(frRegistro,text="NOTA 2:")
lblNota3=ttk.Label(frRegistro,text="NOTA 3:")
lblInsasistencias=ttk.Label(frRegistro,text="INASISTENCIAS:")
lblTituloPromedio=ttk.Label(frRegistro,text="PROMEDIO:")
lblTotal=ttk.Label(frRegistro,text="0.00",foreground="blue")

txtCedula=ttk.Entry(frRegistro)
txtNombre=ttk.Entry(frRegistro)
txtApellido=ttk.Entry(frRegistro)
txtNota1=ttk.Entry(frRegistro)
txtNota2=ttk.Entry(frRegistro)
txtNota3=ttk.Entry(frRegistro)
txtInasistencias=ttk.Entry(frRegistro)
lblErrorCedula=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNombre=ttk.Label(frRegistro,text="",foreground="red")
lblErrorApellido=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota1=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota2=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota3=ttk.Label(frRegistro,text="",foreground="red")
lblErrorInasistencias=ttk.Label(frRegistro,text="",foreground="red")
frBotones=Frame(frRegistro)
btnGuardar=ttk.Button(frBotones,text="GUARDAR",width=20,command=guardar)
btnNuevo=ttk.Button(frBotones,text="NUEVO",width=20,command=nuevo)
btnBuscar=ttk.Button(frBotones,text="BUSCAR",width=20,command=buscar)
btnGuardar.grid(row=0,column=0,padx=10)
btnNuevo.grid(row=0,column=1,padx=10)
btnBuscar.grid(row=0,column=2,padx=10)

lblCedula.grid(row=2,column=1,padx=30)
txtCedula.grid(row=2,column=2,pady=2)
lblErrorCedula.grid(row=2,column=3)
lblNombre.grid(row=3,column=1,pady=2)
txtNombre.grid(row=3,column=2)
lblErrorNombre.grid(row=3,column=3)
lblApellido.grid(row=4,column=1,pady=2)
txtApellido.grid(row=4,column=2)
lblErrorApellido.grid(row=4,column=3)
lblNota1.grid(row=5,column=1,pady=2)
lblErrorApellido.grid(row=4,column=3)
txtNota1.grid(row=5,column=2)
lblErrorNota1.grid(row=5,column=3)
lblNota2.grid(row=6,column=1,pady=2)
txtNota2.grid(row=6,column=2)
lblErrorNota2.grid(row=6,column=3)
lblNota3.grid(row=7,column=1,pady=2)
txtNota3.grid(row=7,column=2)
lblErrorNota3.grid(row=7,column=3)
lblInsasistencias.grid(row=8,column=1)
txtInasistencias.grid(row=8,column=2)
lblErrorInasistencias.grid(row=8,column=3)
lblTituloPromedio.grid(row=9,column=1)
lblTotal.grid(row=9,column=2)
frBotones.grid(row=10,column=0,columnspan=4,pady=10)

ventana.mainloop()


