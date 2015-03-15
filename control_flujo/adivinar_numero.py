# -*- coding: utf-8 -*-
''' Vamos a crear el juego de adivinar un número.
El programa selecciona de forma aleatoria un número del 1 al 100 que el jugador
tendrá que adivinar. El programa irá preguntando un número al jugador.
Si el jugador dice uno mayor, el programa le informará de que el número oculto
es menor (y al revés si dice uno menor). El jugador tiene 10 oportunidades
para adivinar el número.
Crea un nuevo proyecto para este programa en tu repositorio.
Dale una interfaz gráfica con easygui. Incluye alguna imagen en las ventanas.
Escribe comentarios en el código que ayuden a otro programador
a modificar el programa.
Puedes crear diferentes niveles en el juego dando menos oportunidades,
contando el tiempo, etc

'''
from easygui import *

# Generamos número aleatorio
import random

x = random.randint(1,100)


# Se pide el nivel de dificultad
dificultad = int(enterbox('Elige la dificultad\nFácil --> 10 intentos (1)\nMedio --> 8 intentos (2)\nDifícil --> 5 intentos (3)'))

# Según el nivel elegido, se le asigna a intentos un número diferente y se muestra un mensaje
if dificultad == 1:
    intentos = 10
    msgbox('Has elegido la dificultad fácil. Tienes %d intentos.' % intentos)
elif dificultad == 2:
    intentos = 8
    msgbox('Has elegido la dificultad media. Tienes %d intentos.' % intentos)
else:
    intentos = 5
    msgbox('Has elegido la dificultad difícil. Tienes %d intentos.' % intentos)


# Inicializamos el contador a 1
cont = 1

# bucle para contabilizar el número de oportunidades
while cont <= intentos:
    # Pedimos al usuario que introduzca el número a adivinar
    numero = int(enterbox('Introduce el número: '))
    # Comprobamos si el número introducido por el usuario es igual al generado aleatoriamente
    if numero > x:
        # Evaluamos el valor del contador para mostrar un mensaje u otro
        if cont <= (intentos-1):
            msgbox('Te has pasado. El número es menor.\nLlevas %d intentos.' % cont)
        else:
           msgbox('Has fallado. Has agotado el número de intentos y no has acertado el número.\nEl número era el %d' % x) 
    elif numero < x:
        # Evaluamos el valor del contador para mostrar un mensaje u otro
        if cont <= (intentos -1):
            msgbox ('No has llegado. El número es mayor.\nLlevas %d intentos.' % cont)
        else:
           msgbox('Has fallado. Has agotado el número de intentos y no has acertado el número.\nEl número era el %d' % x) 
    else:
        msgbox ('Has acertado!')
        break # en caso de acertar, salimos del while
    # Sumamos 1 al contador de oportunidades
    cont += 1

