# -*- coding: cp1252 -*-
'''
Una tienda hace un descuento del 10% por compras menores de 20€,
un 20% por compras entre 20 y 50€ y un 25% si la compra es mayor.
Escribe un programa que pida el precio de un producto
y muestre su precio final en las rebajas.
'''

from easygui import *

precio = float(enterbox('Introduce el precio'))

if precio < 20:
    precio = precio * 0.9
    #msgbox('El precio final con 10% de descuento es: '+ str(precio))
    msgbox('El precio final con 10%% de descuento es: %.2f' %precio)
elif precio >= 20 and precio <= 50:
    precio = precio * 0.8
    msgbox('El precio final con 20%% de descuento es: %.2f' %precio)
else:
    precio = precio * 0.75
    msgbox('El precio final con 25%% de descuento es: %.2f' %precio)



'''
consumo = float(enterbox('Introduce el precio'))

if consumo < 20:
    descuento = consumo * 0.1
elif consumo < 50:
    descuento = consumo * 0.2
else:
    descuento = consumo * 0.25

precio = consumo - descuento

msgbox('El precio final es %f' precio)
'''




'''
