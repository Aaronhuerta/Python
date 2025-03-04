import tkinter as tk
from tkinter import ttk

def saludar():
    resultado.config(text=f"hola, {entrada.get()}!")

def seleccionar():
    resultado.config(text=f"seleccionaste {combobox_opciones.get()}")

def seleccionar_color(event):
    color = combobox_colores.get()
    if color == "rojo":
        ventana.config(bg="red")
    elif color == "verde":
        ventana.config(bg="green")
    elif color == "azul":
        ventana.config(bg="blue")

ventana = tk.Tk()
ventana.title("ejemplo de GUI")
ventana.geometry("400x400")

ventana.config(bg="lightblue")
etiqueta = tk.Label(ventana, text="Escribe tu nombre", font="Arial")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Crear una etiqueta para el Combobox de opciones
etiqueta_combobox_opciones = tk.Label(ventana, text="Selecciona una opcion", font="Arial")
etiqueta_combobox_opciones.pack()

# Crear el Combobox de opciones
opciones = ["opcion 1", "opccion 2", "opcion 3"]
combobox_opciones = ttk.Combobox(ventana, values=opciones)
combobox_opciones.pack()
combobox_opciones.current(0)

# Crear una etiqueta para el Combobox de colores
etiqueta_combobox_colores = tk.Label(ventana, text="Selecciona un color", font="Arial")
etiqueta_combobox_colores.pack()

# Crear el Combobox de colores
colores = ["rojo", "verde", "azul"]
combobox_colores = ttk.Combobox(ventana, values=colores)
combobox_colores.pack()
combobox_colores.current(0)

# Vincular la selección del Combobox de colores al método seleccionar_color
combobox_colores.bind("<<ComboboxSelected>>", seleccionar_color)

ventana.mainloop()
