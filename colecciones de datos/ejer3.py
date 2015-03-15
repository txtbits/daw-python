# -*- coding: utf-8 -*-
'''Escribe una función esta_ordenada(lista) La función recibe como parámetro
una lista y devuelve verdadero (True) si la lista está ordeanda y
falso si no lo está.
'''

import string

def ordenada(lista):
    
    lista_ord = lista[:]
    lista_ord.sort(key=string.upper)
    
    if lista_ord == lista:
        return True
    else:
        return False

lista = []

while True:
    nombre = raw_input('Inro nombre: ')
    if nombre == '':
        break
    lista.append(nombre)

print ordenada(lista)
