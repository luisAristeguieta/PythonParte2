from tkinter import *
from utilitariosImagen import obtenerImagen
from random import randint

META = 3  # puntos para ganar

# Estado del juego (listas para evitar duplicación)
dado = [0, 0]         # dado[0] jugador1, dado[1] jugador2
puntaje = [0, 0]      # puntaje[0] jugador1, puntaje[1] jugador2
lanzado = [False, False]  # saber si ya lanzó cada jugador

def lanzar(jugador):
    """jugador: 0 para J1, 1 para J2"""
    dado[jugador] = randint(1, 6)
    lblDado[jugador].config(image=imagenes[dado[jugador]])
    btnLanzar[jugador].config(state="disabled")
    lanzado[jugador] = True

    # Solo calcular resultado cuando ambos ya lanzaron
    if all(lanzado):
        resultado()
        ganadorFinal()

def resultado():
    if dado[0] > dado[1]:
        puntaje[0] += 1
        lblPuntaje[0].config(text=str(puntaje[0]))
        lblResultado.config(text="Gana el Jugador #1")
    elif dado[0] < dado[1]:
        puntaje[1] += 1
        lblPuntaje[1].config(text=str(puntaje[1]))
        lblResultado.config(text="Gana el Jugador #2")
    else:
        lblResultado.config(text="Empate")

    btnNuevaPartida.config(state="normal")

def ganadorFinal():
    # Si nadie llegó a la meta, no hacer nada
    if puntaje[0] < META and puntaje[1] < META:
        return

    # Determinar ganador/perdedor
    if puntaje[0] == META:
        ganador, perdedor = 0, 1
    else:
        ganador, perdedor = 1, 0

    lblDado[ganador].config(image=imgGanador)
    lblDado[perdedor].config(image=imgPerdedor)

    # Bloquear para que no sigan lanzando
    btnLanzar[0].config(state="disabled")
    btnLanzar[1].config(state="disabled")

def reinicia():
    dado[0] = dado[1] = 0
    lanzado[0] = lanzado[1] = False
    lblResultado.config(text="")

    lblDado[0].config(image=imagenes[0])
    lblDado[1].config(image=imagenes[0])

    btnLanzar[0].config(state="normal")
    btnLanzar[1].config(state="normal")
    btnNuevaPartida.config(state="disabled")

def nuevaPartida():
    """Nueva ronda (sin resetear puntajes)"""
    dado[0] = dado[1] = 0
    lanzado[0] = lanzado[1] = False
    lblResultado.config(text="")
    lblDado[0].config(image=imagenes[0])
    lblDado[1].config(image=imagenes[0])
    btnLanzar[0].config(state="normal")
    btnLanzar[1].config(state="normal")
    btnNuevaPartida.config(state="disabled")

def reiniciarJuegoCompleto():
    """Reinicia todo (incluye puntajes)"""
    puntaje[0] = puntaje[1] = 0
    lblPuntaje[0].config(text="0")
    lblPuntaje[1].config(text="0")
    nuevaPartida()


# ---------------- UI ----------------
ventana = Tk()
ventana.geometry("500x400")
ventana.title("JUEGO DADOS")

imagenes = [
    obtenerImagen("dadoIncognita.png", 100),  # 0
    obtenerImagen("dados1.png", 100),         # 1
    obtenerImagen("dados2.png", 100),         # 2
    obtenerImagen("dados3.png", 100),
    obtenerImagen("dados4.png", 100),
    obtenerImagen("dados5.png", 100),
    obtenerImagen("dados6.png", 100)          # 6
]

# Cargar imágenes finales una sola vez (evita recargar en cada jugada)
imgGanador = obtenerImagen("ganador.png", 100)
imgPerdedor = obtenerImagen("perdedor.jpg", 100)

framePrincipal = Frame(ventana, bg="white")
framePrincipal.place(x=50, y=50)

lblTitulo = Label(framePrincipal, text="VEAMOS QUIEN ES EL MEJOR", font=("Arial", 15), bg="white")
lblTitulo.grid(row=0, column=0, columnspan=3, padx=50)

lblPuntaje = [
    Label(framePrincipal, text="0", fg="blue", font=("Arial", 25), bg="white"),
    Label(framePrincipal, text="0", fg="blue", font=("Arial", 25), bg="white")
]
lblPuntaje[0].grid(row=1, column=0)
lblPuntaje[1].grid(row=1, column=2)

lblDado = [
    Label(framePrincipal, image=imagenes[0], bg="white"),
    Label(framePrincipal, image=imagenes[0], bg="white")
]
lblDado[0].grid(row=2, column=0)
lblDado[1].grid(row=2, column=2)

btnLanzar = [
    Button(framePrincipal, text="LANZAR", command=lambda: lanzar(0), bg="black", fg="white", font=("Arial", 12)),
    Button(framePrincipal, text="LANZAR", command=lambda: lanzar(1), bg="black", fg="white", font=("Arial", 12))
]
btnLanzar[0].grid(row=3, column=0, pady=20)
btnLanzar[1].grid(row=3, column=2)

lblResultado = Label(framePrincipal, text="", fg="red", font=("Arial", 15), bg="white")
lblResultado.grid(row=4, column=0, columnspan=3)

btnNuevaPartida = Button(framePrincipal, text="NUEVA PARTIDA", command=nuevaPartida,
                         bg="lime", font=("Arial", 12), state="disabled")
btnNuevaPartida.grid(row=5, column=1)

# Si quieres reiniciar TODO (incluye puntajes), puedes cambiar el command:
# btnNuevaPartida.config(command=reiniciarJuegoCompleto)

ventana.mainloop()

