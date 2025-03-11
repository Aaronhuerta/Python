import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import folium
import webbrowser
import random
import threading
import time

# Definir dimensiones de la ventana
ancho = 800
alto = 600

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Simulación de Camión en Aguascalientes')
ventana.geometry(f"{ancho}x{alto}")

# Crear un lienzo para dibujar el mapa y el camión
lienzo = tk.Canvas(ventana, width=ancho, height=alto)
lienzo.pack()

# Coordenadas de la ruta principal
ruta_principal = [
    [21.8818, -102.2912],
    [21.8820, -102.2900],
    [21.8830, -102.2890],
    [21.8840, -102.2880],
    [21.8850, -102.2870],
    [21.8860, -102.2860],
    [21.8870, -102.2850],
    [21.8880, -102.2840],
    [21.8890, -102.2830],
    [21.8900, -102.2820],
    [21.8910, -102.2810],
    [21.8920, -102.2800],
    [21.8930, -102.2790],
    [21.8940, -102.2780],
    [21.8950, -102.2770],
    [21.8960, -102.2760],
    [21.8970, -102.2750],
    [21.8980, -102.2740],
    [21.8990, -102.2730]
]

# Función para crear el mapa y mostrar la posición del camión
def crear_mapa(posicion_actual, ruta):
    mapa = folium.Map(location=posicion_actual, zoom_start=15)
    for punto in ruta:
        folium.Marker(location=punto, icon=folium.Icon(color='blue')).add_to(mapa)
    folium.Marker(location=posicion_actual, popup='Camión', icon=folium.Icon(color='red', icon='truck')).add_to(mapa)
    mapa.save('mapa_camion_aguascalientes.html')
    webbrowser.open('mapa_camion_aguascalientes.html')

# Convertir coordenadas a píxeles (asumiendo una escala arbitraria)
def convertir_coordenadas(lat, lon, ancho, alto):
    lat_min, lat_max = 21.85, 22.00  # Ajustar según el área de interés
    lon_min, lon_max = -102.35, -102.25  # Ajustar según el área de interés
    x = int((lon - lon_min) / (lon_max - lon_min) * ancho)
    y = int((lat_max - lat) / (lat_max - lat_min) * alto)
    return [x, y]

# Intentar cargar la imagen del camión
try:
    imagen_camion = Image.open("camion.png")
    imagen_camion = imagen_camion.resize((30, 30), Image.ANTIALIAS)
    imagen_camion_tk = ImageTk.PhotoImage('camion.png')
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    imagen_camion_tk = None

# Crear un widget para la imagen del camión si se cargó correctamente
if imagen_camion_tk:
    camion = lienzo.create_image(0, 0, image=imagen_camion_tk)
else:
    camion = lienzo.create_oval(0, 0, 20, 20, fill="red")

# Posición inicial del camión
posicion_actual = ruta_principal[0]
x, y = convertir_coordenadas(posicion_actual[0], posicion_actual[1], ancho, alto)
lienzo.coords(camion, x, y)

# Función para actualizar la posición del camión
def actualizar_posicion():
    global posicion_actual, ruta_principal
    while ruta_principal:
        siguiente_punto = ruta_principal.pop(0)
        posicion_actual = siguiente_punto
        x, y = convertir_coordenadas(posicion_actual[0], posicion_actual[1], ancho, alto)
        lienzo.coords(camion, x, y)
        
        # Simular detección de accidente y redirigir ruta
        if random.random() < 0.1:  # 10% de probabilidad de accidente
            print("Accidente detectado, redirigiendo ruta...")
            # Redirigir a una ruta alternativa (simplemente volviendo al punto de inicio en este caso)
            ruta_principal = [[21.8818, -102.2912]] + ruta_principal

        # Actualizar el mapa
        crear_mapa(posicion_actual, ruta_principal)

        # Mostrar la nueva ubicación en consola
        print(f'Latitud: {posicion_actual[0]}, Longitud: {posicion_actual[1]}')
        time.sleep(2)

# Ejecutar la función de actualización en un hilo separado
hilo_actualizacion = threading.Thread(target=actualizar_posicion)
hilo_actualizacion.start()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
