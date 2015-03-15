# -*- coding: utf-8 -*-

'''Escribe un programa lista_de_clase.py que pida nombres de alumnos y los introduzca en un fichero (lista_alumnos.txt. Cada alumno irá en una línea diferente.
 Una nueva función abrirá la lista de alumnos y la mostrará en pantalla, con los alumnos ordenados por orden alfabético.
'''

def pedir_nombre():
    nombre = raw_input('Introduce un nombre de alumno: ')
    nombre = nombre.title()
    nombre = nombre +'\n'
    return nombre

def escribir_fichero(nombre):
    f.write(nombre)


def mostrar_alumnos(f):
    print f.read()
    
f = open('lista_alumnos.txt', 'w')

x = 1
while x != 0:
    nombre = pedir_nombre()
    escribir_fichero(nombre)    
    x = int(raw_input('¿Quieres introducir otro alumno?\n1 = Sí\n0 = NO\n--> '))

f.close()
    
f = open('lista_alumnos.txt')
mostrar_alumnos(f)

f.close()