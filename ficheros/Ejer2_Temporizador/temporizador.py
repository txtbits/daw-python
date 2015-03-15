# -*- coding: utf-8 -*-

'''Escribe un programa temporizador.py que cada 5 segundos escriba el tiempo (hora, minuto, segudos) en una línea.
El programa creará el fichero si no existe. Cada vez que tenga que escribir, abrirá el archivo, escribirá en él y lo cerrará.
'''

from datetime import *
import os
import time

def abrir_f_read():
    # abrir fichero en modo lectura
    f = open('tiempo.txt')
    return f

def cerrar_f():
    # cerrar el fichero
    f.close()

def abrir_f_write():
    # abrir fichero en modo escritura
    f = open('tiempo.txt', 'w')
    return f

def leer_tiempo():
    # se lee la hora, se convierte a string y se le añade el salto de linea al final
    hora = str(datetime.time(datetime.now())).split('.')
    hora = hora[0]
    hora = hora + '\n'
    return hora

def escribir(datos,f):
    # funcion para escribir el contenido de la etiqueta DATOS en el fichero f
    f.write(datos)


while True:
    if os.path.exists('tiempo.txt'):        # si el fichero existe
        # se abre el fichero en modo lectura, se lee el contenido y se guarda en una etiqueta
        f = abrir_f_read()
        contenido = f.read()
        cerrar_f()
        # se abre el fichero en modo escritura, se lee la hora, y se escriben en el tiempo.txt el contenido anterior y la hora actual leída
        f = abrir_f_write()
        hora = leer_tiempo()
        escribir(contenido, f)
        escribir(hora,f)
        cerrar_f()
    
    else:       # si el fichero NO existe
        # se lee la hora actual, se abre el fichero en modo escritura y se escribe en el fichero abierto
        hora = leer_tiempo()
        f = abrir_f_write()
        escribir(hora,f)
        cerrar_f()
    time.sleep(5)

    