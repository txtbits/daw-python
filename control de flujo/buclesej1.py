# -*- coding: utf-8 -*-

'''Escribe un programa que pida un número y escriba su tabla de multiplicar.
Haz dos versiones: una con range y otra con while.
'''

from easygui import *

numero = int(enterbox('Introduce un número'))

for i in range (11):
    print '%2d * %2d = %2d' % (numero, i, (numero*i))




i = 0
while i<=10: 
    print '%2d * %2d = %2d' % (numero, i, (numero*i))
    i += 1
