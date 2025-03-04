import tkinter as tk
from tkinter import ttk
def saludar():
    resultado.config(text=f"hola, {entrada.get()}!")
def seleccionar():
    resultado.config(text=f"seleccionaste {combobox.get()}")
def seleccionar_color():
    resultado.config(text=f"seleccionaste {combobox.get()}")
ventana = tk.Tk()
ventana.title("ejemplo de GUI")
ventana.geometry("400x400")

ventana.config(bg="lightblue")
etiqueta = tk.Label(ventana, text="Escribe tu nombre",font="Arial").pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar ,font="Arial")
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Crear una etiqueta para el Combobox
etiqueta_combobox = tk.Label(ventana, text="Selecciona una opcion", font="Arial")
etiqueta_combobox.pack()

# Crear el Combobox
opciones = ["opcion 1", "opccion 2", "opcion 3"]
combobox = ttk.Combobox(ventana, values=opciones)
combobox.pack()
combobox.current(0)

etiqueta_combobox = tk.Label(ventana, text="Selecciona un color", font="Arial")
etiqueta_combobox.pack()
col= {
    "rojo": "red",
    "verde": "green",
    "azul": "blue"
}

combobox = ttk.Combobox(ventana, values=(col.keys()))
combobox.pack()
combobox.current(0)

ventana.mainloop()