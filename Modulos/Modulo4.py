'''
---------------------------------------------------------------------------------------------------------
FUNCION QUE RECIBE LOS DATOS OBTENIDOS Y LOS TRANSFORMA EN CSV PARA SU POSTERIOR ANALISIS Y VISUALIZACIÓN
---------------------------------------------------------------------------------------------------------
'''
import csv
from tkinter import messagebox

def convertir_a_csv(numeros, coincidencias):
    def guardar_como_csv(lista, nombre_archivo):
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for fila in lista:
                escritor_csv.writerow(fila)
    coincidencias = coincidencias
    numeros = numeros
    guardar_como_csv(coincidencias, 'coincidencias.csv')
    guardar_como_csv(numeros, 'numeros.csv')
    messagebox.showinfo("Archivo Creado", f"Se han creado dos archivos 'numeros' y 'coincidencias' con los datos obtenidos.")