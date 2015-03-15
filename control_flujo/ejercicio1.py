# -*- coding: cp1252 -*-
from easygui import *

'''
Crea un programa que tiene una palabra oculta. El programa pregunta la contraseña al jugador,
si la adivina muestra un mensaje de éxito. Si no, muestra el error.
'''

palabra = 'capullo'

password = passwordbox('Introduce la contraseña')

if palabra == password:
    msgbox('Access granted')
else:
    msgbox('Access denied')
