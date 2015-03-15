#-*- coding: utf-8 -*-
'''

Haz un programa que a partir de la información de los datos de http://datos.zaragoza.es
muestre los tramos con tráfico negro, rojo y amarillo (ordenados y agrupados así)
'''
from urllib2 import urlopen
from json import load
 
urlt = 'http://www.zaragoza.es/trafico/estado/estadoFicherosTrafico.json'

fichero = load(urlopen(urlt))

print datos

'''

f = urlopen('http://www.zaragoza.es/trafico/estado/barrios.json')
doc = f.read()

from json import loads
datos = loads(doc[3:])

datos.keys()
datos = datos.get('barrios')
datos[0].keys()

for b in datos:
    print b.get('name')
    
'''