
'''
-----------------------------------------------------------------------------------------------------------
SE RECOLECTAN LOS DATOS DE LA PÁGINA OFICIAL DE LA LOTERÍA DE CÓRDOBA MEDIANTE LA TÉCNICA DEL WEB SCRAPPING
-----------------------------------------------------------------------------------------------------------
'''



#IMPORTACIÓN DE LIBRERIAS NECESARIAS
import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup    
from urllib.parse import urljoin
import numpy as np
import re
import tkinter as tk

'''Los numeros sorteados en la poceada se actulizan en una pagina distinta segun el dia.
 A la fecha 22/06/23 va en el dia 1844.
Por ende hay que iterar y guardar en una variable el ultimo dia para que el programa este actualizado.
 Esto lo hacemos agregando dias de mas y probando la extensión .xml para asi conseguir el ultimo dia'''
def ultimo_dia():
    ultimo_dia_poceada = 0
    dia_estimado_poceada = 1844
    while True:
            url = f"https://www.loteriadecordoba.com.ar/files/poceada/0{dia_estimado_poceada}.xml"
            response = requests.head(url)
            if response.status_code == 200 and response.headers.get('content-type') == 'application/xml':
                dia_estimado_poceada+=1
            else:
                ultimo_dia_poceada = dia_estimado_poceada-1
                break
    return ultimo_dia_poceada
'''Una vez obtenido el ultimo dia hay que preguntar al usuario cuantos resultados desea extraer.
Ventana de tkinter que pide al usuario la cantidad de dias que desea analizar'''

def seleccion_dias():
    global dias_iterar
    dias_iterar = 1
    def obtener_numero():
        global dias_iterar
        dias_iterar= int(entry.get())
        ventana.destroy()
    ventana = tk.Tk()
    ventana.iconbitmap("img/analisis.ico")
    ventana.title("")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 450
    alto_ventana = 150
    x = int((ancho_pantalla - ancho_ventana) / 2)
    y = int((alto_pantalla - alto_ventana) / 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    label = tk.Label(ventana, text="Ingrese la cantidad de dias a extraer:", font=("Segoe UI", 16, "bold"))
    label.place(relx=0.5,rely=0.2, anchor="center")
    entry = tk.Entry(ventana,font=("Segoe UI", 20, "bold"))
    entry.focus()
    entry.place(relx=0.5,rely=0.5,relheight=0.2,relwidth=0.4,anchor="center")
    boton = tk.Button(ventana, text="Aceptar", font=("Segoe UI",12,"bold"),command=obtener_numero, borderwidth=4)
    boton.place(relx=0.5,rely=0.8,anchor="center")
    ventana.mainloop()
    return dias_iterar

    #Bucle que extrae los 20 numeros de la poceada e itera la cantidad de dias que el usuario quiere y los almacena en una lista bidimensional  
def extraer(dias, ultimo_dia):
    ultimo_d= ultimo_dia
    lista_listas_numeros=[]
    lista_listas_fechas=[]
    for i in range(dias):
        print("Descargando ",i+1," de ", dias,"dias")
        #Traer el url sumandole el dia de la poceada
        url_inicial = 'https://www.loteriadecordoba.com.ar/juegos/poceada-cordobesa?sorteo='+str(ultimo_d)
        #Hacer el request
        r= requests.get(url_inicial)
        #Ahora vamos a generar texto plano 
        s= BeautifulSoup(r.content, "html.parser")
        #vamos a buscar los 20 numeros sorteados
        dias_poceada = (s.find_all("h2", class_ ="fdo-blanco"))
        #buscamos las fechas de dichos sorteos
        fecha_dias = (s.find_all("h2", class_ ="fdo-gris01 print-none"))



        #los agregamos a una lista como strings
        lista_num = []
        lista_num_limpia = []
        for i in dias_poceada:
            lista_num.append(str(i))
        #Extramos solo el texto de cada etiqueta html
        for i in lista_num:
            lista_num_limpia.append(i[23:25])
        
        #Agregar
        lista_listas_numeros.append(lista_num_limpia)
        ultimo_d= ultimo_d-1

        #hacemos exactamente los mismo para las fechas
        fecha_num = []
        lista_fecha_limpia = []
        for i in fecha_dias:
            fecha_num.append(str(i))
        #Extramos solo el texto de cada etiqueta html
        for i in fecha_num:
            lista_fecha_limpia.append(i[41:51])
                
        #Agregar
        lista_listas_fechas.append(lista_fecha_limpia)
    return lista_listas_numeros, lista_listas_fechas


#Funcion madre para que ejecuta las demas funciones y se la llama desde el main
def recoleccion():
    ultimo_d = ultimo_dia()
    seleccion_d = seleccion_dias()
    lista_de_listas = extraer(seleccion_d, ultimo_d)
    return lista_de_listas
