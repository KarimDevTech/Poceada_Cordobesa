import Modulos.Modulo1 as Modulo1,Modulos.Modulo2 as Modulo2, Modulos.Modulo3 as Modulo3, Modulos.Modulo4 as Modulo4 ,Modulos.Modulo5 as Modulo5

#Llamar a la funcion madre del modulo1 que ejecuta la recoleccion de datos mediante el web scrapping
#se obtienen listas con los 20 numeros sorteados cada dia y su respectiva fecha
listas = Modulo1.recoleccion()
lista_num = listas[0]
lista_fechas = listas[1]
print()
#Se mandan las listas al modulo2 para su transformacion a np.arrays
array_num = Modulo2.crear_arrays(lista_num)
array_fechas = Modulo2.crear_arrays(lista_fechas)

#Se mandan los array al modulo3 para analizar que 8 numeros se repiten en los sorteos. retorna una lista de enteros con los resultados
coincidencias_ganadoras = Modulo3.analizar(array_num,array_fechas)
print()

#Se llama al modulo4 que convierte los datos en archivos 'csv' para su analisis
lista_20numeros = []
for i in array_num:
    lista= [int(num) for num in i]
    lista_20numeros.append(lista)
Modulo4.convertir_a_csv(lista_20numeros, coincidencias_ganadoras)

#Llamar a modulo5 que pregunta al usuario si desea probar una jugada ganadora
Modulo5.probar_jugada(array_num, array_fechas)