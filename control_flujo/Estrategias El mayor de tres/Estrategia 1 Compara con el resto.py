# -*- coding: cp1252 -*-
from easygui import *

x1 = enterbox('Introduce un numero: ')
x2 = enterbox('Introduce un numero: ')
x3 = enterbox('Introduce un numero: ')

# Convierte los n�meros
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

if x1 >= x2 and x1 >= x3:
    mayor = x1
elif x2 >= x1 and x2 >= x3:
    mayor = x2
elif x3 >= x2 and x3 >= x1:
    mayor = x3

msgbox('El numero mayor es %d' %mayor)
