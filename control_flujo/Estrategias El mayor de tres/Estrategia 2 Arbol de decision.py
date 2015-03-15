# -*- coding: cp1252 -*-
from easygui import *

x1 = enterbox('Introduce un numero: ')
x2 = enterbox('Introduce un numero: ')
x3 = enterbox('Introduce un numero: ')

# Convierte los números
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

if x1 >= x2:
    if x1 >= x3:
        mayor = x1
    else:
        mayor = x3
else:
    if x2 >= x3:
        mayor = x2
    else:
        mayor = x3

msgbox('El numero mayor es %d' %mayor)
