# -*- coding: utf-8 -*-

from EjercicioAlumnos import *

lista = []

# Añadir 5 alumnos

lista.append(Alumno('Luis')) # i = 0
lista.append(Alumno('Mario'))
lista.append(Alumno('Pedro'))
lista.append(Alumno('Ana'))
lista.append(Alumno('Francisco'))

# Crear funciones de test

def test_encuentra_while():
    assert buscar_nombre_w('Luis', lista) == 0
    assert buscar_nombre_w('Francisco', lista) == 4
    assert buscar_nombre_w('José', lista) == -1
    
def test_encuentra():
    assert buscar_nombre('Luis', lista) == 0
    assert buscar_nombre('Francisco', lista) == 4
    assert buscar_nombre('José', lista) == -1