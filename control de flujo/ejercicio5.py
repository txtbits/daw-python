# -*- coding: cp1252 -*-
'''
Escribe un programa que pida el ph de una solución y muestre
el mensaje de si la solución es ácida (ph < 7.0)
o peligrósamente ácida: ph < 3.0)
'''

from easygui import *

ph = float(enterbox('Introduce el ph de la solución'))


if ph < 3.0:
    msgbox('El ph %.1f es peligrósamente ácido' %ph)
elif ph >= 3.0 and ph < 7.0:
    msgbox('El ph %.1f es ácido' %ph)
else:
    msgbox('El ph %.1f es normal' %ph)
