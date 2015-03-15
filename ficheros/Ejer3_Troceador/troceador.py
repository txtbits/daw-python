# -*- coding: utf-8 -*-

'''
Escribe un programa troceador.py que pedirá un fichero de una imagen o una canción y la troceará en archivos más pequeños de 521 bytes.
El programa irá numerandolos archivos (trozo1, trozo2, etc) Un segundo programa tomará los archivos troceados y recompondrá el archivo original
'''



def abrir_fichero(namefile):
    f = open(namefile, 'rb')
    return f
   
def leer_fichero(f):
    contenido = f.read(10000)
    return contenido

def grabar_fichero(cont,contenido):
    trozo = 'trozo'
    cont = str(cont)
    nom_fich = trozo + cont
    parte = open(nom_fich, 'wb')
    parte.write(contenido)
    parte.close()


namefile = raw_input('Introduce el nombre del fichero que quieres abrir: ')

f = abrir_fichero(namefile)
contenido = leer_fichero(f)
contador = 1
while contenido != '': 
    #grabar el contenido en otro fichero
    grabar_fichero(contador,contenido)
    contador += 1
    #volver a leer del fichero origen
    contenido = leer_fichero(f)

f.close()
