# -*- coding: cp1252 -*-
'''
Escribe un programa que pida al usuario una contraseña
(usa la palabra oculta que quieras).
El programa volverá a pedir la contraseña hasta que la adivine el jugador.
Modifica el programa. Haz que el programa permita un máximo de 5 intentos.
Si a los 5 intentos no ha introducido bien la contraseña,
mostrará el mensaje de error y terminará.
'''

from easygui import *


oculta = passwordbox('Introduce la contraseña secreta')

intentos = 0
respuesta = ''

while intentos != 5 and respuesta !=oculta :
    respuesta = enterbox('Introduce la contraseña')
    intentos += 1
    if intentos == 5:
        msgbox('Eres tonto y no has acertado')

if respuesta == oculta:
    msgbox('Has acertado!')
