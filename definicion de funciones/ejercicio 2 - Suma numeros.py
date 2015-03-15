# -*- coding: utf-8 -*-
'''
Escribe (y comprueba) la definición de dos funciones:
sumaN(n)  --> Devuelve la suma de los primeros n números naturales
sumaNCubos(n) --> Devuelve la suma de los cubos
de los primeros n números naturales
'''

def suma(n):
    suma = 0
    for x in range(n+1):
        suma += x
    return suma

def suma_cubos(n+1):
    suma_cubos = 0
    for x in range(n):
        suma_cubos += (x**3)
    return suma_cubos

n = int(raw_input('Introduce el valor de N: '))

print suma(n)
print suma_cubos(n)
