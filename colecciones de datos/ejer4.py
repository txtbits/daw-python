# -*- coding: utf-8 -*-
'''Escribe una función tiene_duplicados(lista) que tome una lista y devuelva
verdadero si algún elemento aparece más de una vez.
La función no modificará la lista.'''

def duplicados(lista):
    for registro in lista:
        numero = lista.count(registro)
        if numero > 1:
            return True
    return False
        
            
    
lista = []

while True:
    nombre = raw_input('Inro nombre: ').upper()
    if nombre == '':
        break
    lista.append(nombre)

print duplicados(lista)
