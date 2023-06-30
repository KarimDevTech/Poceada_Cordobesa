'''
-------------------------------------------------------------------------------------------------
INTERFAZ GRAFICA OPCIONAL PARA EL USUARIO. RECIBE UNA JUGADA Y SE FIJA SI HUBIESE SALIDO GANADORA
-------------------------------------------------------------------------------------------------
'''

import tkinter as tk
import numpy as np
from tkinter import messagebox
def probar_jugada(array_num, fechas):
    def ventana():
        def analizar_jugada(jugada):
            cantidad_victorias = 0
            dias_victoria = []
            for i in range(len(array_num)):
                similitud = len(np.intersect1d(jugada, array_num[i]))
                if similitud == 8:
                    dias_victoria.append(i)
                    cantidad_victorias+=1      
            if cantidad_victorias ==0:  
                print(f"LO SIENTO su jugada no es ganadora, pruebe aumentar los dias extraidos o cambiar la combinacion")
            if cantidad_victorias > 0:
                for i in dias_victoria:
                    print(f"¡FELICITACIONES! tu jugada fue ganadora el dia: {fechas[i]}")

        def obtener_jugada():
            jugada = np.array([])
            for entry in entries:
                valor = entry.get()
                jugada = np.append(jugada, valor)
            analizar_jugada(jugada)
            # Crear la ventana    
        ventana = tk.Tk()
        ventana.title("¿SE HUBIESE CONVERTIDO EN MILLONARIO?")

        ventana.deiconify()
        # Obtener el ancho y alto de la ventana
        ancho_ventana = 420
        alto_ventana = 180

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()

        # Calcular la posición para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer la posición de la ventana
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear el título
        titulo = tk.Label(ventana, text="INGRESE SU JUGADA:", font=("Segoe UI",18,"bold"))
        titulo.pack(pady=20)

        # Crear el subtítulo
        subtitulo = tk.Label(ventana, text="Los números de un dígito con un 0 adelante, ejemplo: 01, 05, 09")
        subtitulo.pack()

        # Crear una lista para almacenar los campos de entrada
        entries = []

        # Crear un marco para contener los campos de entrada
        marco_entries = tk.Frame(ventana)
        marco_entries.pack()

        # Crear los campos de entrada
        for _ in range(8):
            entry = tk.Entry(marco_entries, width=5)
            entry.pack(side=tk.LEFT, padx=5)
            entries.append(entry)

        # Crear el botón para obtener la jugada
        boton = tk.Button(ventana, text="Obtener resultados", command=obtener_jugada,font=("Segoe UI",12,"bold"),borderwidth=4)
        boton.pack(pady=10)
        # Ejecutar el bucle principal de la ventana
        ventana.mainloop()

    respuesta = messagebox.askquestion("Mensaje", "¿DESEA PROBAR UNA JUGADA PARA VER SUS COINCIDENCIAS?")
    if respuesta == "yes":
        ventana()
    else:
        print("Chau, nos vemos!")

