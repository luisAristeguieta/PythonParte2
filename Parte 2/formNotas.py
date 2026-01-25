from tkinter import Tk,Entry,Label,Button
from utilitariosImagen import obtenerImagen
from PIL import Image, ImageTk

notas=[]
#FUNCIONES
#def fnAgregarNota():
    # Validaciones: 
    # Que no este vacio
    # Que no sea string
    # Encuentre en el rango de 0 a 10

# Capturo valor: 
def fnAgregarNota():

    lblNota.config(text="")
    lblPromedio.config(text="")
    
    notaTexto =txtNota.get()

    if notaTexto == "":
        lblNota.config(text="Ingrese el valor de la nota")
        return

    try:
        notaTexto = float(notaTexto)
    except:
        lblNota.config(text="Solo se permite valores numericos")
        return
    
    if notaTexto < 0 or notaTexto > 10:
        lblNota.config(text="La nota debe estar entre 0 y 10")
        return
    
    global notas
    notas.append(notaTexto);
    lblNota.config(text=f"Nota agregada correctamente: {notaTexto}")
    txtNota.delete(0, "end")

#def fnCalcularPromedio():
    #
def fnCalcularPromedio():
    lblNota.config(text="Ingrese una nota")
    lblPromedio.config(text="")

    global notas

    if len(notas) == 0:
        lblPromedio.config(text="No existe nota agregada")
        return
    
    totalNota = 0;

    for i in range(len(notas)):
        totalNota += notas[i]
    promedio = round(totalNota / len(notas),2)
    lblPromedio.config(text=f"El promedio de las notas es {promedio}")
    
    if promedio < 5:
        nueva = obtenerImagen("emoji1.jpg")
    else:
        nueva = obtenerImagen("emoji2.jpg")

    lblImg.config(image=nueva)
    lblImg.image = nueva  # referencia obligatoria


#PARTE GRAFICA
ventana=Tk()
ventana.geometry("300x300")
ventana.title("PROMEDIO DE NOTAS")

lblNota=Label(text="Ingrese una nota")
lblNota.pack()

txtNota=Entry()
txtNota.pack()

btnAgregarNota=Button(text="AGREGAR NOTA", command=fnAgregarNota)
btnAgregarNota.pack()

btnCalcularPromedio=Button(text="CALCULAR PROMEDIO", command=fnCalcularPromedio)
btnCalcularPromedio.pack()

lblPromedio=Label(text="",fg="red")
lblPromedio.pack()

imgInicial = obtenerImagen("emoji3.jpg")
lblImg = Label(image=imgInicial)
lblImg.image = imgInicial  # referencia obligatoria
lblImg.pack()


ventana.mainloop()