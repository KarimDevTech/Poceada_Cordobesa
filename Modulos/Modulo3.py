'''
---------------------------------------------------------------------
SE COMPARA ARRAY CON ARRAY PARA ENCONTRAR LAS COINCIDENCIAS GANADORAS
---------------------------------------------------------------------
'''
import numpy as np
import tkinter as tk

#Funcion para generar comparaciones entre arrays sin repeticiones todos con todos.
#La comparacion devuelve los sorteos en donde haya N cantidad de numeros iguales
def analizar(arr, arrF):
    coincidencias_ganadoras = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if np.array_equal(arr[i], arr[j]):
                pass
            else:
                if i<j:
                    elementos_comunes = np.intersect1d(arr[i], arr[j])
                    cantidad_elementos_comunes = len(elementos_comunes)
                    if cantidad_elementos_comunes ==8:
                        print("ALTA COINCIDENCIA ENTRE EL DIA: ", arrF[i][0], "Y EL DIA: ",arrF[j][0] ,elementos_comunes)
                        array_a_lista = list(elementos_comunes)
                        lista_str_a_int = [int(num) for num in array_a_lista]
                        coincidencias_ganadoras.append(lista_str_a_int)
    return coincidencias_ganadoras
















'''def analizar(arr):
    array = arr
    coincidencias = []
    set_temporal2= set({})
    for i in range(len(array)):
        for j in range(len(array)):
            if con[i]!=con[j] and i<j:
                comparacion = con[i]&con[j]
                coin = (len(comparacion))
                if coin >= 8:
                    print("ALTA COINCIDENCIA ENTRE EL DIA: ", i+1, "Y EL DIA: ", j+1 ,sorted(con[i]&con[j]))
                    for k in comparacion:
                        set_temporal2.add(k)
                    coincidencias.append(set_temporal2)
                    set_temporal2= set({})  
    print("la longitud del set de coincidencias es: ", len(coincidencias))'''