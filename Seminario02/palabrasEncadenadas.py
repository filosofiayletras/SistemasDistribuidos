#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Grupo 21
#Sistemas Distribuidos
#Jose Manuel Vidal
#Manuel Francisco


#1. Pedimos el nombre del fichero al usuario
nombreFichero = raw_input("Introduce el nombre del fichero\n")


#2. Abrimos el fichero y lo procesamos
listaPalabras = []
with open(nombreFichero, 'r') as fichero:
	for linea in fichero:
		listaPalabras += linea.split()

#3. Recorremos la lista almacenando la cadena más larga
listaMasLarga = []
listaActual   = []

for palabra in listaPalabras:
	copiaPalabras = list(listaPalabras)
	listaActual   = []
	listaActual.append(palabra)
	copiaPalabras.remove(palabra)
	
	i = 0
	while i < len(copiaPalabras):
		if listaActual[-1][-1] == copiaPalabras[i][0]:
			listaActual.append(copiaPalabras[i])
			copiaPalabras.remove(copiaPalabras[i])
			i = 0
		else:
			i += 1

	if len(listaMasLarga) < len(listaActual):
		listaMasLarga = listaActual

	

print "La lista más larga tiene ", len(listaMasLarga), " y es ", listaMasLarga
