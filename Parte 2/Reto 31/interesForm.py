from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from credito import *


def limpiarErrores():
    lblErrorMonto.config(text="")
    lblErrorPlazo.config(text="")
    lblErrorTasa.config(text="")

def limpiar():
    txtMonto.delete(0, END)
    txtPlazo.delete(0, END)
    txtTasa.delete(0, END)
    lblTotal.config(text="0.00")
    limpiarErrores()

def validarRango(txtValor, lblError, minimo, maximo):
    valorStr = txtValor.get()

    if valorStr == "":
        lblError.config(text="Requerido")
        return None

    try:
        valor = float(valorStr)
    except ValueError:
        lblError.config(text="Debe ser numérico")
        return None

    valor = float(valorStr)
    if valor < minimo or valor > maximo:
        lblError.config(text=f"Rango {minimo}-{maximo}")
        return None

    return valor

def obtenerDatos():
    limpiarErrores()

    monto = validarRango(txtMonto, lblErrorMonto, 1000, 50000)
    plazo =validarRango(txtPlazo, lblErrorPlazo, 1, 15)
    tasa  = validarRango(txtTasa,  lblErrorTasa, 3, 20)

    if monto is None or plazo is None or tasa is None:
        return None

    return monto, plazo, tasa

def ejecutarInteresSimple():
    datos = obtenerDatos()
    if datos is None:
        return

    monto, plazo, tasa = datos
    interes = round(calcularInteresSimple(monto, plazo, tasa),2)
    lblTotal.config(text=f"{interes}")

def ejecutarInteresCompuesto():
    datos = obtenerDatos()
    if datos is None:
        return

    monto, plazo, tasa = datos
    interes = round(calcularInteresCompuesto(monto, plazo, tasa),2)
    lblTotal.config(text=f"{interes:.2f}")

#GRAFICA
ventana=Tk()
ventana.title("Calculo de Cuota")
ventana.geometry("700x400")
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)
tabControl.add(tab1,text="REGISTRO")
tabControl.pack(expand = 1, fill ="both") 

#TAB REGISTRO
frRegistro= Frame(tab1)
frRegistro.place(x=100,y=100)
lblMonto=ttk.Label(frRegistro,text="MONTO:")
lblPlazo=ttk.Label(frRegistro,text="PLAZO:")
lblTasa=ttk.Label(frRegistro,text="TASA:")
lblTituloPromedio=ttk.Label(frRegistro,text="CUOTA:")
lblTotal=ttk.Label(frRegistro,text="0.00",foreground="blue")


txtMonto=ttk.Entry(frRegistro,state="normal")
txtPlazo=ttk.Entry(frRegistro)
txtTasa=ttk.Entry(frRegistro)

lblErrorMonto=ttk.Label(frRegistro,text="",foreground="red")
lblErrorPlazo=ttk.Label(frRegistro,text="",foreground="red")
lblErrorTasa=ttk.Label(frRegistro,text="",foreground="red")

frBotones=Frame(frRegistro)
btnGuardar=ttk.Button(frBotones,text="CALCULAR SIMPLE",width=25,command=ejecutarInteresSimple)
btnNuevo=ttk.Button(frBotones,text="CALCULAR COMPUESTO",width=25,command=ejecutarInteresCompuesto)
btnBuscar=ttk.Button(frBotones,text="LIMPIAR",width=20,command=limpiar)
btnGuardar.grid(row=6,column=0,padx=10)
btnNuevo.grid(row=6,column=1,padx=10)
btnBuscar.grid(row=6,column=2,padx=10)

lblMonto.grid(row=2,column=1,padx=30)
txtMonto.grid(row=2,column=2,pady=2)
lblErrorMonto.grid(row=2,column=3)

lblPlazo.grid(row=3,column=1,pady=2)
txtPlazo.grid(row=3,column=2)
lblErrorPlazo.grid(row=3,column=3)

lblTasa.grid(row=4,column=1,pady=2)
txtTasa.grid(row=4,column=2)
lblErrorTasa.grid(row=4,column=3)

lblTituloPromedio.grid(row=5,column=1)
lblTotal.grid(row=5,column=2)


frBotones.grid(row=8,column=0,columnspan=4,pady=10)
ventana.mainloop()