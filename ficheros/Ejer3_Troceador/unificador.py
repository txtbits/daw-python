# -*- coding: utf-8 -*-

'''
Escribe un programa troceador.py que pedirá un fichero de una imagen o una canción y la troceará en archivos más pequeños de 521 bytes.
El programa irá numerandolos archivos (trozo1, trozo2, etc) Un segundo programa tomará los archivos troceados y recompondrá el archivo original
'''

def abrir_trozo(namefile):
    fr = open(namefile, 'rb')
    return fr
   
def leer_trozo(f):
    contenido = f.read()
    return contenido

def reconstruir_fichero(fr,fw):
    contenido = leer_trozo(fr)
    fw.write(contenido)
    

import os

cont = 1
fw = open('unido.jpg', 'wb')
namefile = 'trozo' + str(cont)
print namefile
while os.path.exists(namefile):
    cont += 1
    fr = abrir_trozo(namefile)
    reconstruir_fichero(fr,fw)
    fr.close()
    namefile = 'trozo' + str(cont)
    print namefile
fw.close()