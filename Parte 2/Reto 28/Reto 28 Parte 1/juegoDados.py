from tkinter import *
from utilitariosImagen import obtenerImagen
from random import randint

ventana=Tk()
ventana.geometry("600x400")
ventana.title("JUEGO DADOS")

imagenDado = [ 
    obtenerImagen("dadoIncognita.png",200),
    obtenerImagen("dados1.png",200),
    obtenerImagen("dados2.png",200),
    obtenerImagen("dados3.png",200),
    obtenerImagen("dados4.png",200),
    obtenerImagen("dados5.png",200),
    obtenerImagen("dados6.png",200)
]

numeroDado1 = 0
numeroDado2 = 0

def valorDado1 ():
    global numeroDado1
    numeroDado1 = randint(1,6)
    lblDadoJugador1.config(image=imagenDado[numeroDado1])
    resultado ();

def valorDado2 ():
    global numeroDado2
    numeroDado2 = randint(1,6)
    lblDadoJugador2.config(image=imagenDado[numeroDado2])
    resultado ();


def resultado ():
    if numeroDado1 == 0 or numeroDado2 == 0 :
     return lblResultado.config(text="Resultado")
    
    if numeroDado1 > numeroDado2:   
       lblResultado.config(text="Gana el Jugador #1")
       return 
    
    if numeroDado1 < numeroDado2:
       return lblResultado.config(text="Gana el Jugador #2")
    
    return lblResultado.config(text="Empate")
       
def reinicia ():
    global numeroDado1
    global numeroDado2
    numeroDado1 = 0
    numeroDado2 = 0
    lblResultado.config(text="Resultado")
    lblDadoJugador1.config(image = imagenDado[0])
    lblDadoJugador2.config(image = imagenDado[0])

framePrincipal = Frame(ventana)
framePrincipal.place(x=100,y=100)

imgIncognita = obtenerImagen("dadoIncognita.png",100)

lblTitulo=Label(framePrincipal,text="VEAMOS QUIEN ES EL MEJOR")
lblTitulo.grid(row=0,column=0,columnspan=3, padx=150)

lblDadoJugador1=Label(framePrincipal,image = imagenDado[0])
lblDadoJugador1.grid(row=1,column=0)

btnLanzar1=Button(framePrincipal,text="LANZAR", command=valorDado1)
btnLanzar1.grid(row=2,column=0)

lblDadoJugador2=Label(framePrincipal,image = imagenDado[0])
lblDadoJugador2.grid(row=1,column=2)

btnLanzar2=Button(framePrincipal,text="LANZAR", command=valorDado2)
btnLanzar2.grid(row=2,column=2)

lblResultado=Label(framePrincipal,text="Resultado")
lblResultado.grid(row=3,column=0,columnspan=3)

btnReiniciar=Button(framePrincipal,text="Nueva Partida", command=reinicia)
btnReiniciar.grid(row=4,column=0,columnspan=3)


ventana.mainloop()