# -*- coding: cp1252 -*-
from easygui import *

x1 = enterbox('Introduce un numero: ')
x2 = enterbox('Introduce un numero: ')
x3 = enterbox('Introduce un numero: ')

# Convierte los n�meros
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

mayor = x1
if x2 > mayor:
    mayor = x2
if x3 > mayor:
    mayor = x3

msgbox('El numero mayor es %d' %mayor)
