# -*- coding: cp1252 -*-
'''
Escribe un programa que pida el ph de una soluci�n y muestre
el mensaje de si la soluci�n es �cida (ph < 7.0)
o peligr�samente �cida: ph < 3.0)
'''

from easygui import *

ph = float(enterbox('Introduce el ph de la soluci�n'))


if ph < 3.0:
    msgbox('El ph %.1f es peligr�samente �cido' %ph)
elif ph >= 3.0 and ph < 7.0:
    msgbox('El ph %.1f es �cido' %ph)
else:
    msgbox('El ph %.1f es normal' %ph)
