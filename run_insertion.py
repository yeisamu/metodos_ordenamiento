# -*- coding: utf-8 -*-
from funciones import *
from insertion import *
import threading
import time

def main():
    op = " "

    while op != "s" and op != "S":
        print"------------------------------------------"
        print("\t\tMETODOS DE ORDENAMIENTO\t\t")
        print("(a). Inserción Directa ")
        print("(b). Ordenamiento por Mezcla (Merge Sort) ")
        print("(c). Ordenamiento por Montones (Heap Sort) ")
        print("(d). Ordenamiento rápido (Quick Sort) ")
        print("(e). Ordenamiento por Conteo (Counting Sort) ")
        print("(f). Ordenamiento por Radix Sort ")
        print("(s). Salir")

        op = raw_input("Digite una Opción: ")

        if op == "a" or op == "A": # inserción Directa

            #tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg=canRegistros()
            hilo = threading.Thread(target=llenarLista, args=(lista, nreg,))
            hilo.start()
            hilo2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hilo2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)
            lista_ordenada = crearLista()
            nlista = crearLista()
            hilo3 = threading.Thread(target=leerCsv, args=(lista_ordenada, nombre,))
            hilo3.start()
            hilo3.join()
            nlista2 = arreglalista(lista_ordenada, nlista)
            tam = longitud(nlista2)
            insercionDirecta(nlista2, tam)
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)
            nombre_final = nombreArchivo()
            hilo2 = threading.Thread(target=crearCsv, args=(nlista2, nombre_final,))
            hilo2.start()


        if op == "b" or op == "B": #Ordenamiento por Mezcla (Merge Sort)

            tiempo_inicial = time.time()
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            hilo = threading.Thread(target=llenarLista, args=(lista, nreg,))
            hilo.start()
            hilo2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hilo2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)

            lista_ordenada = crearLista()
            leerCsv(lista_ordenada, nombre)

            nlista = crearLista()
            nlista2 = arreglalista(lista_ordenada, nlista)

            imprimirLista(mergesort(nlista2))

            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)
            nombre_final = nombreArchivo()
            hilo2 = threading.Thread(target=crearCsv, args=(mergesort(nlista2), nombre_final,))
            hilo2.start()

        if op == "c" or op == "C": #Ordenamiento por Montones (Heap Sort)

            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            hilo = threading.Thread(target=llenarLista, args=(lista, nreg,))
            hilo.start()
            hilo2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hilo2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)
            lista_ordenada = crearLista()
            nlista = crearLista()
            hilo3 = threading.Thread(target=leerCsv, args=(lista_ordenada, nombre,))
            hilo3.start()
            hilo3.join()
            nlista2 = arreglalista(lista_ordenada,nlista)

            tam = longitud(nlista2)
            heap_sort(nlista2)
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)

        if op == "d" or op == "D": #Ordenamiento rápido (Quick Sort)

            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            hilo = threading.Thread(target=llenarLista, args=(lista, nreg,))
            hilo.start()
            hilo2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hilo2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)
            lista_ordenada = crearLista()
            nlista = crearLista()

            hilo3 = threading.Thread(target=leerCsv, args=(lista_ordenada, nombre,))
            hilo3.start()
            hilo3.join()
            nlista2 = arreglalista(lista_ordenada, nlista)
            tam = longitud(nlista2)
            quicksort(nlista2, 0, tam - 1)
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)

        if op == "e" or op == "E": #Ordenamiento rápido (Quick Sort)
            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            hiloe = threading.Thread(target=llenarListaConteo, args=(lista, nreg,))
            hiloe.start()
            hiloe2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hiloe2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)
            # ordenar
            lista_ordenada = crearLista()
            nlista = crearLista()
            hiloe3 = threading.Thread(target=leerCsv, args=(lista_ordenada, nombre,))
            hiloe3.start()
            hiloe3.join()
            nlista2 = arreglalista(lista_ordenada, nlista)

            tam = longitud(nlista2)
            # print len(nlista2)
            counting_sort(nlista2, tam)
            # counting_sort(nlista2, 7)
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)

        if op == "f" or op == "F": #Ordenamiento Radix Sort

            lista = crearLista()
            nombre = nombreArchivo()
            nreg = canRegistros()
            hilof = threading.Thread(target=llenarListaConteo, args=(lista, nreg,))
            hilof.start()
            hilof2 = threading.Thread(target=crearCsv, args=(lista, nombre,))
            hilof2.start()
            tiempo_inicial = time.time()
            imprimirLista(lista)
            # ordenar
            lista_ordenada = crearLista()
            nlista = crearLista()
            hilof3 = threading.Thread(target=leerCsv, args=(lista_ordenada, nombre,))
            hilof3.start()
            hilof3.join()
            nlista2 = arreglalista(lista_ordenada,nlista)

            radix_sort(nlista2)
            imprimirLista(nlista2)
            tiempo_final = time.time() - tiempo_inicial
            imprimirTiempo(tiempo_final)

        if op == "S" or op == "s":

            print "Hasta Pronto."
            exit()

        else:
            print("Digite una Opción \n")

if __name__ == '__main__':
	main()