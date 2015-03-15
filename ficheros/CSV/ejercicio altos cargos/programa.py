# -*- coding: utf-8 -*-
'''
Created on 02/12/2011
@author: chra

Usa los datos del fichero csv de:
http://opendata.euskadi.net/w79-contgen/es/contenidos/ds_general/sueldos_altos_cargos_2011/es_sueldos/altos_cargos_asesores.html
Crea un programa que:
- genere un nuevo fichero csv con los datos de retribuciones anuales (2009, 2010 y 2011)
- muestre la evolución de los sueldos en porcentajes entre los 3 años
- haga una gráfica (sueldos_euskadi.png) con la evolución de los sueldos.
'''

def crear_fichero(lector):
    # Crea un fichero 'retribucion.csv'
    fw = open('retribucion.csv', 'w')
    # CSV abre el fichero creado antes para poder escribir en él
    csvwriter = csv.writer(fw,  delimiter=";")
    # Escribe la línea de cabeceras
    csvwriter.writerow(('Nivel','Año 2009', 'Año 2010', 'Año 2011'))
    # Recorre el contenido de lector y por cada línea, guarda los datos del nivel y sueldos de 09-10-11
    for x in lector:
        dato1 = x['Año 2009 - Anual']
        dato1 = float(dato1.replace('.', '').replace(',', '.'))
        dato2 = x['Año 2010 - Anual']
        dato2 = float(dato2.replace('.', '').replace(',', '.'))
        dato3 = x['Año 2011 - Anual']
        dato3 = float(dato3.replace('.', '').replace(',', '.'))
        
        csvwriter.writerow((x['Nivel'],  dato1,  dato2, dato3))
        
    fw.close()

def mostrar_porcentajes():
    finput = open('retribucion.csv')
    lector = csv.DictReader(finput, delimiter=";") # si no se pone delimiter, coge la coma por defecto
    print "%-40s" %"Nivel", "%-18s" %'Porcentaje 2009', '%-18s' %'Porcentaje 2010', '%-18s' %'Porcentaje 2011'
    for x in lector:
        p1 = (float(x['Año 2010'])*100)/float(x['Año 2009'])
        p2 = (float(x['Año 2011'])*100)/float(x['Año 2010'])
        print "%-40.38s" %x['Nivel'], "%-18s" %'100', '%-9.2f' %(p1-100), '%18.2f' %(p2-100)
    finput.close()
        
    
import urllib2
import csv

url = 'http://opendata.euskadi.net/w79-contgen/es/contenidos/ds_general/sueldos_altos_cargos_2011/es_sueldos/contenidos/ds_general/sueldos_altos_cargos_2011/es_sueldos/adjuntos/sueldos_2011.csv'
 
req = urllib2.urlopen(url)
content = req.read()
 
# extraer el encoding de la cabecera
encoding = req.headers.get('content-type')
encoding = encoding.split('charset=')
encoding = encoding[-1]
 
# convertir a unidoce, usando el encoding apropiado
ucontent = unicode(content, encoding)

# Partimos en lineas a partir de la segunda en adelante
ucontent = ucontent.splitlines()[1:]

#Eliminamos las líneas vacías (el que codificó el fichero es un soplagaitas)
buenas = []
for linea in ucontent:
    if linea.split(';')[0]:
        buenas.append(linea)

ucontent = buenas

# Convertimos en un diccionario ucontent utilizamos como delimitador ";"
lector = csv.DictReader(ucontent, delimiter=";")

crear_fichero(lector)
mostrar_porcentajes()

print 'programa terminado'

'''
import codecs
# Si utilizaramos un fichero .csv
finput = codecs.open('sueldos.csv', 'r', 'iso-8859-1')
finput.readline()
lector = csv.DictReader(finput, delimiter=";") # si no se pone delimiter, coge la coma por defecto
'''