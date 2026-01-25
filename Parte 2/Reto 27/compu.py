from tkinter import Tk,Entry,Label,Button
from utilitariosImagen import obtenerImagen

def apagar ():
    apaga = obtenerImagen("apagada.PNG")
    lblImg.config(image=apaga)
    lblImg.image = apaga
    btnApagar.config(state="disabled")
    btnEncender.config(state="normal")

def encencender ():
    enciende = obtenerImagen("encendida.PNG")
    lblImg.config(image=enciende)
    lblImg.image = enciende
    btnEncender.config(state="disabled")
    btnApagar.config(state="normal")

#PARTE GRAFICA
ventana=Tk()
ventana.geometry("600x600")
ventana.title("COMPUTADOR")

imgApagada = obtenerImagen("apagada.PNG")
lblImg = Label(image=imgApagada)
lblImg.image = imgApagada  # referencia obligatoria
lblImg.pack()

btnApagar=Button(text="APAGAR", command= apagar, state="disabled")
btnApagar.pack()

btnEncender=Button(text="ENCENDER", command= encencender, state="normal")
btnEncender.pack()

ventana.mainloop()