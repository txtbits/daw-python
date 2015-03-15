 # -*- coding: utf-8 -*-
import os

f = open('fichero.txt') # abre el fichero

os.path.exists('fichero.txt') # para saber si existe el fichero


os.getcwd() # consultar el directorio de trabajo actual

os.listdir('.') # consultar los archivos del directorio actual

f.read() # lee el fichero entero y lo muestra por pantalla

f.tell() # nos indica la posición del fichero en la que está leyendo
f.seek(0) # nos posicionamos al inicio del fichero (byte 0 )

f.read(1) # lee solo un byte

f.readline() # lee una línea entera (con el salto de línea incluido)

for linea in f: #lee el fichero línea a línea
	print linea,
	
secreto = f.readline() #leemos una línea del fichero
secreto = secreto.strip() # quitamos el salto de línea

for linea in f
	print linea.strip() # imprime las lineas del archivo sin salto de linea
	
contenido = f.read()




f = open('fichero.txt', 'w') # abre el fichero en modo escritura (ojo que sobreescribe el contenido)

f.write(contenido.upper) # escribe el contenido de la etiqueta contenido pero en mayúsculas

f = open('fichero.txt', 'r+') # abre el fichero en modo lectura y escritura (Luis no lo aconseja)