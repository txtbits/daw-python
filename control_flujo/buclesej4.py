# -*- coding: cp1252 -*-
'''
Escribe un programa que pida al usuario una contrase�a
(usa la palabra oculta que quieras).
El programa volver� a pedir la contrase�a hasta que la adivine el jugador.
Modifica el programa. Haz que el programa permita un m�ximo de 5 intentos.
Si a los 5 intentos no ha introducido bien la contrase�a,
mostrar� el mensaje de error y terminar�.
'''

from easygui import *


oculta = passwordbox('Introduce la contrase�a secreta')

intentos = 0
respuesta = ''

while intentos != 5 and respuesta !=oculta :
    respuesta = enterbox('Introduce la contrase�a')
    intentos += 1
    if intentos == 5:
        msgbox('Eres tonto y no has acertado')

if respuesta == oculta:
    msgbox('Has acertado!')
