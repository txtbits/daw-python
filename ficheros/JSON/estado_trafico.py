# -*- coding: utf-8 -*-
'''
Haz un programa que a partir de la información de los datos de http://datos.zaragoza.es, 
muestre los tramos con tráfico negro, rojo y amarillo (ordenados y agrupados así) 
'''
def buscar_nombre(id,tramos):
    for x in tramos['tramos']:
        if x['id'] == id:
            nombre = x['name']
            return nombre
    
    

from urllib2 import urlopen
from json import load
import operator

urlt = 'http://www.zaragoza.es/trafico/estado/tramoswgs84.json'

tramos = load(urlopen(urlt))

urle = 'http://www.zaragoza.es/trafico/estado/estado.json'

estado = load(urlopen(urle))
estado_tramos = []
cont = 1
for x in estado['estados']:
    if x == 'b' or x == 'r' or x == 'y':
        nombre = buscar_nombre(cont,tramos)
        estado_tramos.append([nombre, x])
        #print '%s -----> %s' %(nombre, x)
    cont += 1


tramos_ord = sorted(estado_tramos, key=operator.itemgetter(1))


for tramo in tramos_ord:
    print tramo[0],'------->', tramo[1]
