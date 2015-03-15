# -*- coding: utf-8 -*-
'''

Crea un programa que analice el fichero y muestre:
- Los años y sus temperaturas (máxima, mínima y media), ordenados por año
- Los años y su tempertura media, ordenados por temperatura en orden descendente
- Crea un fichero html:
    Encabezado: Temperaturas de Zaragoza
    Fuente: (la url, como un enlace)
    Tabla con las temperaturas (media, máxima y mínima)
    Los encabezados de la tabla serán claros.
'''

def obtener_listado(f):
    listado = []
    for n,linea in enumerate(f):
        if n != 0:
            registro = linea.split()
            listado.append(registro)
    return listado

def listado_anio(f):
    listado = obtener_listado(f)    
    listado.sort()
    
    for x in listado:
        print x[0:4]

def listado_temp(f):
    listado = obtener_listado(f)
    listado.sort(key=itemgetter(1), reverse=True)
    
    for x in listado:
        if not '-' in x[1:4]:
            print x[0:4]

def crear_html(f):
    fw = open('temperaturas.html', 'w')
    listado = obtener_listado(f)    
    fw.write('<html><head><title>Temperaturas de Zaragoza</title></head>')
    fw.write('<body>')
    fw.write('<h1>Temperaturas de Zaragoza</h1>')
    fw.write('<table style="text-align:center; border:1px solid #000; border-radius:5px;">')
    fw.write('<tr><td>A&ntilde;o</td><td>Media</td><td>Maxima</td><td>Minima</td></tr>')
    for linea in listado:
        fw.write('<tr>')
        for x in range(4):
            if x == 0:
                fw.write('<td style="background-color:#3E6; font-weight:bold;">'+linea[x]+'</td>')
            else:
                fw.write('<td style="width:100px; border:1px solid #000; background-color:#E9E;">'+linea[x]+'</td>')
        fw.write('</tr>')
    fw.write('</table>')
    fw.write('</body></html>')
    

import sys
from operator import itemgetter

try:
    # Instrucción con riesgo
    f = open('temperaturas_zaragoza.txt')
except IOError:
    print 'Error, el fichero temperaturas_zaragoza no existe'
    sys.exit()


opcion = int(raw_input('''¿Qué quieres hacer?: 
1 - Listado ordenado por año (1)
2 - Listado ordenado por temperatura media (2)
3 - Crear archivo html (3)
4 - Salir (4)
>> '''))

while opcion != 4:

    if opcion == 1:
        listado_anio(f)
    if opcion == 2:
        listado_temp(f)
    if opcion == 3:
        crear_html(f)
    opcion = int(raw_input('''¿Qué quieres hacer?: 
1 - Listado ordenado por año (1)
2 - Listado ordenado por temperatura media (2)
3 - Crear archivo html (3)
4 - Salir (4)
>> '''))
