import random
import csv

def crearLista():
	lista = list()
	return lista

def nombreArchivo():
	nombre = raw_input("Ingrese nombre del archivo: ")
	return nombre

def llenarLista(lista, limite):
	for i in range(0, limite):
		lista.append(random.randint(-9999, 9999))

def llenarListaConteo(lista, limite):
	for i in range(0, limite):
		lista.append(random.randint(0, 1000))

def crearCsv(lista, nombre):
	datos = open(nombre + ".csv", "w")
	datos_csv = csv.writer(datos)
	datos_csv.writerow(lista)
	datos.close()

def imprimirLista(lista):
	print lista

def leerCsv(lista_2, nombre):
	datos = open(nombre + ".csv", "r")
	datos_csv = csv.reader(datos, delimiter=",")
	for variable in (datos_csv):
		lista_2.append(variable)
	datos.close()
	return lista_2

def arreglalista(lista,nlista):
	for i in lista [0]:
		nlista.append(int(i))
	return nlista

def longitud(lista):
	return len(lista)

def imprimirTiempo(tiempo_final):
	print ("Proceso finalizado en %0.5f segundos" %tiempo_final)