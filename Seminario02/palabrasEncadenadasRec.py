#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Grupo 21
#Sistemas Distribuidos
#Jose Manuel Vidal
#Manuel Francisco

def listaMasLarga_rec(final, lista):
	if len(lista) > 0:
		for palabra in lista:
			if final == palabra[0]:
				lista.remove(palabra)
				return [palabra] + listaMasLarga_rec(palabra[-1], lista)
	return []

def listaMasLarga(lista):
	masLarga = []

	for palabra in lista:
		listaActual = list(lista)
		listaActual.remove(palabra)
		actual = [palabra] + listaMasLarga_rec(palabra[-1], listaActual)

		if len(masLarga) < len(actual):
			masLarga = actual

	return masLarga

#1. Pedimos el nombre del fichero al usuario
nombreFichero = raw_input("Introduce el nombre del fichero\n")


#2. Abrimos el fichero y lo procesamos
listaPalabras = []
with open(nombreFichero, 'r') as fichero:
	for linea in fichero:
		listaPalabras += linea.split()

#3. Recorremos la lista almacenando la cadena más larga
larga = listaMasLarga(listaPalabras)	

print "La lista más larga tiene ", len(larga), " y es ", larga
