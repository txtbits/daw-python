# -*- coding: utf-8 -*-
'''
Escribe un programa que pida una lista de nombres (acabada con un <intro>).
El programa mostrará la lista de nombres en orden alfabético sin repetir ninguno.
'''

lista = []

while True:
    nombre = raw_input('Inro nombre: ')
    if nombre == '':
        break
    lista.append(nombre)


lista_sin_repes = []

for nom in lista:
    if nom not in lista_sin_repes:
        lista_sin_repes.append(nom)

lista_sin_repes.sort()
for n in lista_sin_repes:
    print n
