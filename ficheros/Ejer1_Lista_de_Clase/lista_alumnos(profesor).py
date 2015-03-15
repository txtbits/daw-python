# -*- coding: utf-8 -*-
'''



Created on 25/11/2011

@author: Alumno
'''
import os

def crea_fichero():
    # crear fichero en modo escritura
    nom_fichero = 'lista_alumnos.txt'
    if os.path.exists(nom_fichero):
        # añadir
        fw = open(nom_fichero)
    else:
        #crear
        fw = open(nom_fichero, 'w')
    
    # pido nombres al usuario (hasta entrada vacía)
    while True:
        nombre = raw_input('Intro nombre alumno > ')
    # escribo nombre en el fichero + \n
        if nombre:
            fw.write(nombre + '\n')
        else:
            break
    # cerrar el fichero
    fw.close()

def lee_fichero():
    fr = open('lista_alumnos.txt')
    #n = 1 #número de alumno
    for n, linea in enumerate(fr):
        print n+1, linea.strip()
        #n += 1
    fr.close()
    
#crea_fichero()

lee_fichero()

