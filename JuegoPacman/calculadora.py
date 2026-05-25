import tkinter as tk

# Función para agregar números a la pantalla
def click_boton(valor):
    entrada.set(entrada.get() + str(valor))

# Función para limpiar la pantalla
def limpiar():
    entrada.set("")

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)
    except:
        entrada.set("Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.StringVar()

# Pantalla
pantalla = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (texto, fila, columna) in botones:
    if texto == "C":
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=limpiar)
    elif texto == "=":
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=lambda t=texto: click_boton(t))
    
    boton.grid(row=fila, column=columna)

# Ejecutar app
ventana.mainloop()