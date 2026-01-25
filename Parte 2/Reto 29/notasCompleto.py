from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utilNotas import buscarEstudiante


#VARIABLES GLOBALES
estudiantes=["1757124670#Luis#Jimenez#10#10#10",
             "1757124671#Luis1#Jimenez2#9#9#9",
             "1757124672#Luis2#Jimenez2#8#8#8"]

#messagebox.showinfo(title="", message="")
#FUNCIONES

def limpiarErrores():
    lblErrorCedula.config(text="")
    lblErrorNombre.config(text="")
    lblErrorApellido.config(text="")
    lblErrorNota1.config(text="")
    lblErrorNota2.config(text="")
    lblErrorNota3.config(text="")


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
            return
    messagebox.showinfo(title="Importante", message="Sin Registro")
    return

def guardar():
    limpiarErrores()

    if not validarVacios():
        return

    cedula = txtCedula.get().strip()
    nombre = txtNombre.get().strip()
    apellido = txtApellido.get().strip()

    notas = convertirFloat()
    if notas is None:
        return
    
    nota1 = notas[0]
    nota2 = notas[1]
    nota3 = notas[2]

    estEncontrado = buscarEstudiante(cedula, estudiantes)
    if estEncontrado is None:
        estudiantes.append(f"{cedula}#{nombre}#{apellido}#{nota1}#{nota2}#{nota3}")
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
            errores[i].config(text="Solo numérico")
            return None

        if nota < 0 or nota > 10:
            errores[i].config(text="0 a 10")
            return None

        notas.append(nota)

    return notas


def validarVacios():
    listaEntradas = [txtCedula.get(), txtNombre.get(), txtApellido.get(),txtNota1.get(), txtNota2.get(), txtNota3.get()]
    listaErrores = [lblErrorCedula, lblErrorNombre, lblErrorApellido,lblErrorNota1, lblErrorNota2, lblErrorNota3]

    hayError = False

    for i in range(len(listaEntradas)):
        if listaEntradas[i] == "":
            listaErrores[i].config(text="Requerido")
            hayError = True

    return not hayError
     
def nuevo ():
    txtCedula.delete(0,END)
    txtNombre.delete(0,END)
    txtApellido.delete(0,END)
    txtNota1.delete(0,END)
    txtNota2.delete(0,END)
    txtNota3.delete(0,END)  

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
txtCedula=ttk.Entry(frRegistro,state="normal")
txtNombre=ttk.Entry(frRegistro)
txtApellido=ttk.Entry(frRegistro)
txtNota1=ttk.Entry(frRegistro)
txtNota2=ttk.Entry(frRegistro)
txtNota3=ttk.Entry(frRegistro)
lblErrorCedula=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNombre=ttk.Label(frRegistro,text="",foreground="red")
lblErrorApellido=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota1=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota2=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota3=ttk.Label(frRegistro,text="",foreground="red")
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
txtNota1.grid(row=5,column=2)
lblErrorNota1.grid(row=5,column=3)

lblNota2.grid(row=6,column=1,pady=2)
txtNota2.grid(row=6,column=2)
lblErrorNota2.grid(row=6,column=3)

lblNota3.grid(row=7,column=1,pady=2)
txtNota3.grid(row=7,column=2)
lblErrorNota3.grid(row=7,column=3)

frBotones.grid(row=8,column=0,columnspan=4,pady=10)
ventana.mainloop()

