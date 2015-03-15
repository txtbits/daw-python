# -*- coding: cp1252 -*-
import random

from easygui import *

# Creamos una lista de palabras
palabras = ['python', 'easygui', 'yeso', 'pantalla', 'ahorcado', 'bitbucket', 'rst2pdf']

# Seleccionamos una palabra al azar de la lista
oculta = random.choice(palabras) # devuelve una palabra al azar


# Creamos la etiqueta de letras introducidas
letras_introducidas= ''


respuesta = ''

monigote = [r'''
    _________
    |
    |
    |
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |
    |
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |         |
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |        /|
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |        /|\
    |
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |        /|\
    |        /
    |
    |
    ''',
    r'''
    _________
    |         |
    |         0
    |        /|\
    |        / \
    |
    |
    ''']

cont = -1

# Bucle para realizar las funciones hasta que el usuario acierte la palabra
while respuesta != oculta and cont <7:
    respuesta = ''
    # Pedimos una letra al usuario
    letra = enterbox('Introduce una letra: ', 'Ahorcado v.1')

    #Concatenamos la letra pedida a la lista de letras introducidas
    letras_introducidas += letra
    # Bucle que recorre oculta y compara si la letra introducida está o no
    for l in oculta:
        fallarletra = False
        if l in letras_introducidas:
            # Si la letra está, la concatena a la variable respuesta
            respuesta += l            
        else:
            # Si la letra NO está, concatena una barrabaja a "respuesta"
            respuesta += '_ '
            fallarletra = True
    if fallarletra == True:
       cont += 1
    # Muestra respuesta al usuario
    msgbox('%s \n%s' %(monigote[cont], respuesta), 'Ahorcado v.1')

if respuesta == oculta:
    msgbox('%s \nHas acertado!\nLa respuesta es:\n\n %s' %(monigote[cont], oculta), 'Ahorcado v.1')
if cont <= 7:
    msgbox('%s \nHas agotado el número de intentos.\nLa respuesta era:\n\n %s' %(monigote[cont], oculta), 'Ahorcado v.1')
