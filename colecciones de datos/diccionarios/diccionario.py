# -*- coding: utf-8 -*-

import shelve

def abrir_agenda(ruta):
    '''
    abre un fichero shelve con ruta <nombre> y devuelve
    el enlace al fichero
    '''
    agenda = shelve.open(ruta)
    return agenda

def pedir_datos():
    nombre = raw_input('Introduce el nombre: ')
    edad = raw_input('Introduce la edad: ')
    curso = raw_input('Introduce el curso: ')
    estudiante = {}
    estudiante = {'nombre': nombre, 'edad': edad, 'curso': curso}
    return estudiante
        
def guarda(agenda, estudiante):
    agenda[estudiante['nombre']] = estudiante
    agenda.sync()
    
def buscar(agenda, nombre):
    for x in agenda:
        if nombre in x:
            print agenda[x]

def listado_agenda(agenda):
    for x in agenda:
        print agenda[x]

def cerrar_agenda(agenda):
    agenda.close()

opcion = 0
while opcion != 4:
    opcion = int(raw_input('''
        Selecciona la opción que deseas:
        1. Agregar un estudiante a la agenda
        2. Buscar un estudiante concreto
        3. Listado general de estudiantes
        4. Salir del programa
    '''))
    
    agenda = abrir_agenda('miagenda.dat')  # ruta de mi agenda
    
    if opcion == 1:
        estu = pedir_datos()
        guarda(agenda, estu)
    if opcion == 2:
        nombre = raw_input('Introduce el nombre a buscar: ')
        buscar(agenda, nombre)
    if opcion == 3:
        listado_agenda(agenda)
    if opcion == 4:
        cerrar_agenda(agenda)