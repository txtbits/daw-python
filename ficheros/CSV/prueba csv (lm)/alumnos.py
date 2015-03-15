# -*- coding: utf-8 -*-
'''
Created on 02/12/2011

@author: chra
'''

import csv
from operator import itemgetter

# ----- Función media de la notas de los alumnos ----------

def media(alumno):
    #devuelve la nota media a partir de un diccionario con datos de un alumno
    nota1 = int(alumno['Nota1'])
    nota2 = int(alumno.get('Nota2'))
    nota3 = int(alumno.get('Nota3'))
    return (nota1+nota2+nota3) / 3.

# ----------------------------------------------------------

fin = open('alumnos.csv')
lector = csv.DictReader(fin, delimiter=",") # si no se pone delimiter, coge la coma por defecto // devuelve diccionario
# lector = csv.reader(fin, delimiter=",") <-- Devuelve lista

alumnos = []
for linea in lector:
    alumnos.append((linea['Alumno'], media(linea)))

# -------- Ordenar por nombre de alumno -----------
alumnos.sort()
print 'Orden por nombre de alumno'
for al in alumnos:
    print "%-10s %6.2f" % al  #10 espacios entre cadena (nombre - nota media) y permite 6 digitos, 2 de ellos decimales.
# --------------------------------------------------

# --------- Ordenar por nota -----------------------
print '\nOrden por nota'
alumnos.sort(key=itemgetter(1),reverse=True)

for al in alumnos:
    print "%-10s %6.2f" % al
#---------------------------------------------------

# Crea un fichero 'lista_ordenada_notas.csv' y escribe la lista ordenada por notas
fw = open('lista_ordenada_notas.csv', 'w')
csvwriter = csv.writer(fw)
for al in alumnos:
    csvwriter.writerow(al)
    
fw.close()