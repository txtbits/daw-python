# -*- coding: utf-8 -*-

class Alumno(object):
    def __init__(self, nombre):
        self.nombre = nombre

def buscar_nombre_w(nombre, lista):
    '''Devuelve el índice del alumno en la lista.
    Si no está devuelve -1'''
    i = 0
    while i != len(lista) and lista[i].nombre != nombre:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1

def buscar_nombre(nombre, lista):
    i = 0
    for i, valor in enumerate(lista):
        if valor.nombre == nombre:
            return i
    return -1

if __name__ == '__main__':
    # profile
    import time
    lista = []
    for x in range(10000):
        lista.append(Alumno('Pepito'))
    lista.append(Alumno('Pepita'))
    timein = time.time()
    for x in range(10):
        buscar_nombre_w('Pepita', lista)
    timefin = time.time()
    print 'Busqueda con while', (timefin - timein) * 1000
    
    timein = time.time()
    for x in range(10):
        buscar_nombre('Pepita', lista)
    timefin = time.time()
    print 'Busqueda con for', (timefin - timein) * 1000
    

    