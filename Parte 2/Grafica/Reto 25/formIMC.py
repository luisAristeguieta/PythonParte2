import tkinter as tk

#*********FUNCIONES********

def resultadoIMC():
    lblErrorPeso.config(text="");
    lblErrorEstatura.config(text="");
    lblInterpretacion.config(text="");
    lblIMC.config(text="Su IMC es:");

    # Tomar valores y valdo:
    pesoTexto = txtPeso.get();
    estaturaTexto = txtEstatura.get();

    if pesoTexto == "":
        lblErrorPeso.config(text="Ingrese el peso");
        return;

    if estaturaTexto == "":
        lblErrorEstatura.config(text="Ingrese la estatura");
        return;

    peso = float(pesoTexto);
    estatura_cm = float(estaturaTexto);

    # agrago condiciones si esta todo ok:
    if peso <= 0 or peso > 150:
        lblErrorPeso.config(text="Peso inválido (0 < peso ≤ 150 kg)");
        return;

    if estatura_cm <= 30 or estatura_cm > 230:
        lblErrorEstatura.config(text="Estatura inválida (30 < estatura ≤ 230 cm)");
        return;


    estatura_m = estatura_cm / 100;
    imc = round(peso / (estatura_m ** 2), 4);

    lblIMC.config(text=f"Su IMC es: {imc}");

    if imc < 16:
        resultado = "Delgadez Severa";
    elif imc < 17:
        resultado = "Delgadez Moderada";
    elif imc < 18.5:
        resultado = "Delgadez Leve";
    elif imc < 25:
        resultado = "Peso Normal";
    elif imc < 30:
        resultado = "Sobrepeso";
    elif imc < 35:
        resultado = "Obesidad Grado 1";
    elif imc < 40:
        resultado = "Obesidad Grado 2";
    else:
        resultado = "Obesidad Grado 3";

    lblInterpretacion.config(text=f"RESULTADO: {resultado}");

#*********PARTE VISUAL*****
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("INDICE DE MASA CORPORAL")
lblIngresePeso=tk.Label(text="Ingrese su peso en kilos")
lblIngresePeso.pack()
txtPeso=tk.Entry()
txtPeso.pack()
lblErrorPeso=tk.Label(text="",fg="red")
lblErrorPeso.pack()
lblIngreseEstatura=tk.Label(text="Ingrese su estatura en centimetros")
lblIngreseEstatura.pack()
txtEstatura=tk.Entry()
txtEstatura.pack()
lblErrorEstatura=tk.Label(text="",fg="red")
lblErrorEstatura.pack()
(tk.Button(text="CALCULAR IMC", command= resultadoIMC)).pack()
lblIMC=tk.Label(text="Su IMC es:",fg="blue")
lblIMC.pack()
lblInterpretacion=tk.Label(text="",fg="blue")
lblInterpretacion.pack()
ventana.mainloop()
