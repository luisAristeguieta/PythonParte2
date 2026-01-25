import tkinter as tk 

#########funciones

def btnConvertirF():
        lblResultado.config(text=f"Son {((float(txtCentigrados.get()) * 9/5) + 32)} grados farenheit")

#########parte visual
ventana = tk.Tk();
ventana.geometry("300x300")
ventana.title("CONVERTIDOR TEMPERATURA")

lblIngreseCentigrados=tk.Label(text="Ingrese la temperatura en Grados Centigrados")
lblIngreseCentigrados.pack()

txtCentigrados=tk.Entry()
txtCentigrados.pack()

btnConvertir=tk.Button(text="CONVERTIR A FARENHEIT", command= btnConvertirF)
btnConvertir.pack()

lblResultado=tk.Label(text="...")
lblResultado.pack()

ventana.mainloop()