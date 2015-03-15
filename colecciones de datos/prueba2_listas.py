# -*- coding: utf-8 -*-

lista = range(1,10)

for numero in lista:
    print numero,
    if numero %3 == 0:
        print

#------------------------------------------------

lista2 = 'a b c d e f g h i'.split()

contador = 1

for letra in lista2:
    print letra,
    if contador % 3 == 0:
        print
    contador += 1

#Opción 2

for n, letra in enumerate(lista2):
    print letra,
    if (n+1) % 3 == 0:
        print

#--------------------------------------------------

lista_alumnos = 'Luis Pérez,MaríaMartínez,Pilar Fernández'.split(',')

for n, alumno in enumerate(lista_alumnos):
    print n+1, alumno
