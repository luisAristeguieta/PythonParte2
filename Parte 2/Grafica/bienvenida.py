import tkinter as tk

# Funciones:
def saludar():
    print("Hey hola");

def modificaEtiqueta():
    lblMensaje.config(text="Etiqueta Modificada");

def mostrarSaludo():
    nombre = txtNombre.get();
    lblMensaje.config(text=f"Hola {nombre}");

# Interfaz Ventana:
ventana = tk.Tk();
ventana.title("Bienvenida");
ventana.geometry("600x300");
# Interfaz Etiquetas:
lblMensaje = tk.Label(text="Etiqueta 1",fg="red");
lblMensaje.pack();
# Interfaz Caja de texto:
txtNombre = tk.Entry(textvariable="Ingrese Su nombre");
txtNombre.pack()
# Interfaz Boton:
btnOk = tk.Button(text="OK", command=saludar);
#(tk.Button(text="OK")).pack(); # forma resumida de crear un boton()
btnOk.pack();
(tk.Button(text="Cambiar Etiqueta", command=modificaEtiqueta)).pack();
(tk.Button(text="Saludar", command=mostrarSaludo)).pack();
# Muestra todo lo creado bajo ventana:
ventana.mainloop();
