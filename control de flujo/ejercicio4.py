# -*- coding: cp1252 -*-
'''
Un a�o es bisiesto si es divisible entre 4, excepto el �ltimo de cada siglo
(aquel divisible por 100), salvo que este �ltimo sea divisible por 400
(http://es.wikipedia.org/wiki/A%C3%B1o_bisiesto).
Haz un programa que pida un a�o y muestre un mensaje de si es o no bisiesto.
'''

from easygui import *

year = float(enterbox('Introduce el a�o'))


if (year % 4) != 0:
    msgbox('El a�o %.0f NO es bisiesto' % year)
elif (year % 100) == 0 and (year % 400) != 0:
    msgbox('El a�o %.0f NO es bisiesto' % year)
else:
    msgbox('El a�o %.0f es bisiesto' % year)
    
