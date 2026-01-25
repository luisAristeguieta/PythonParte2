from tkinter import *
from utilitariosImagen import obtenerImagen
from random import randint

numeroDado1 = 0
numeroDado2 = 0
PuntajeJugador1 = 0
PuntajeJugador2 = 0

def valorDado1 ():
    global numeroDado1
    numeroDado1 = randint(1,6)
    lblDadoJugador1.config(image=imagenes[numeroDado1])
    resultado ();
    btnLanzar1.config(state="disabled")
    ganadorFinal ()

def valorDado2 ():
    global numeroDado2
    numeroDado2 = randint(1,6)
    lblDadoJugador2.config(image=imagenes[numeroDado2])
    resultado ();
    btnLanzar2.config(state="disabled")
    ganadorFinal ()


def resultado ():
    if numeroDado1 == 0 or numeroDado2 == 0 :
     return lblResultado.config(text="")
    
    if numeroDado1 > numeroDado2:
       global PuntajeJugador1
       PuntajeJugador1 += 1
       lblPuntajeJugador1.config(text=PuntajeJugador1)
       lblResultado.config(text="Gana el Jugador #1")
       btnNuevaPartida.config(state="normal")
       return
    
    if numeroDado1 < numeroDado2:
       global PuntajeJugador2
       PuntajeJugador2 += 1 
       lblPuntajeJugador2.config(text=PuntajeJugador2)
       btnNuevaPartida.config(state="normal")
       lblResultado.config(text="Gana el Jugador #2")
       return
    
    btnNuevaPartida.config(state="normal")
    lblResultado.config(text="Empate")
    return

def ganadorFinal():
    global PuntajeJugador1, PuntajeJugador2
    global imgGanador, imgPerdedor

    if PuntajeJugador1 < 3 and PuntajeJugador2 < 3:
        return

    imgGanador = obtenerImagen("ganador.png", 100)
    imgPerdedor = obtenerImagen("perdedor.jpg", 100)

    if PuntajeJugador1 == 3:
        lblDadoJugador1.config(image=imgGanador)
        lblDadoJugador2.config(image=imgPerdedor)
        btnLanzar1.config(state="disabled")
        btnLanzar2.config(state="disabled")
        return

    if PuntajeJugador2 == 3:
        lblDadoJugador2.config(image=imgGanador)
        lblDadoJugador1.config(image=imgPerdedor)
        btnLanzar1.config(state="disabled")
        btnLanzar2.config(state="disabled")
        return
   

def reinicia ():
    
    global numeroDado1, numeroDado2
    numeroDado1 = 0
    numeroDado2 = 0
    lblResultado.config(text="")
    lblDadoJugador1.config(image = imagenes[0])
    lblDadoJugador2.config(image = imagenes[0])
    btnLanzar1.config(state="normal")
    btnLanzar2.config(state="normal")
    btnNuevaPartida.config(state="disabled")
    global PuntajeJugador1, PuntajeJugador2
    if PuntajeJugador1 == 3 or PuntajeJugador2 == 3:
        lblDadoJugador1.config(image = imagenes[0])
        lblDadoJugador2.config(image = imagenes[0])
        lblPuntajeJugador1.config(text="0")
        lblPuntajeJugador2.config(text="0")
        PuntajeJugador1 = 0
        PuntajeJugador2 = 0

        
    
    
ventana=Tk()
ventana.geometry("500x400")
ventana.title("JUEGO DADOS")


imagenes=[
    obtenerImagen("dadoIncognita.png",100),#0
    obtenerImagen("dados1.png",100),#1
    obtenerImagen("dados2.png",100),#2
    obtenerImagen("dados3.png",100),
    obtenerImagen("dados4.png",100),
    obtenerImagen("dados5.png",100),
    obtenerImagen("dados6.png",100)#6
]

framePrincipal=Frame(ventana,bg="white")
framePrincipal.place(x=50,y=50)

lblTitulo=Label(framePrincipal,text="VEAMOS QUIEN ES EL MEJOR",font=("Arial", 15),bg="white")
lblDadoJugador1=Label(framePrincipal,image=imagenes[0])
btnLanzar1=Button(framePrincipal,text="LANZAR",command=valorDado1,bg="black",fg="white",font=("Arial", 12))
lblDadoJugador2=Label(framePrincipal,image=imagenes[0])
btnLanzar2=Button(framePrincipal,text="LANZAR",command=valorDado2,bg="black",fg="white",font=("Arial", 12))
lblResultado=Label(framePrincipal,text="",fg="red",font=("Arial", 15),bg="white")
btnNuevaPartida=Button(framePrincipal,text="NUEVA PARTIDA",command=reinicia,bg="lime",font=("Arial", 12),state="disabled")
lblPuntajeJugador1=Label(framePrincipal,text="0",fg="blue",font=("Arial", 25),bg="white")
lblPuntajeJugador2=Label(framePrincipal,text="0",fg="blue",font=("Arial", 25),bg="white")

lblTitulo.grid(row=0,column=0,columnspan=3,padx=50)
lblResultado.grid(row=4,column=0,columnspan=3)
lblPuntajeJugador1.grid(row=1,column=0)
lblPuntajeJugador2.grid(row=1,column=2)
lblDadoJugador1.grid(row=2,column=0)
lblDadoJugador2.grid(row=2,column=2)
btnLanzar1.grid(row=3,column=0,pady=20)
btnLanzar2.grid(row=3,column=2)
btnNuevaPartida.grid(row=5,column=1)

ventana.mainloop()
