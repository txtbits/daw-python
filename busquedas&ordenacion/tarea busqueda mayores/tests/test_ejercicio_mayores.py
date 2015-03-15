# -*- coding: utf-8 -*-

from ejercicio_mayores import *

lista1 = [1,2,3,4,5]
lista2 = [1,20,30,4,5]
lista3 = [8,9,1,2,3,4,5]
lista4 = [10,9,1,2,3,4,5]
lista5 = [9,9,1,2,3,4,5]

def test_busqueda_mayores_fin():
    assert buscar_mayores_1(lista1) == [4,3]
    assert buscar_mayores_2(lista1) == [4,3]
    assert buscar_mayores_3(lista1) == [4,3]
    assert lista1 == [1,2,3,4,5]
    
def test_busqueda_mayores_medio():
    assert buscar_mayores_1(lista2) == [2,1]
    assert buscar_mayores_2(lista2) == [2,1]
    assert buscar_mayores_3(lista2) == [2,1]
    assert lista2 == [1,20,30,4,5]
    
def test_busqueda_mayores_inicio():
    assert buscar_mayores_1(lista3) == [1,0]
    assert buscar_mayores_2(lista3) == [1,0]
    assert buscar_mayores_3(lista3) == [1,0]
    assert lista3 == [8,9,1,2,3,4,5]
    
def test_busqueda_mayores_reves():
    assert buscar_mayores_1(lista4) == [0,1]
    assert buscar_mayores_2(lista4) == [0,1]
    assert buscar_mayores_3(lista4) == [0,1]
    assert lista4 == [10,9,1,2,3,4,5]
    

def test_busqueda_mayores_iguales():
    assert buscar_mayores_1(lista5) == [0,1]
    assert buscar_mayores_2(lista5) == [0,1]
    assert buscar_mayores_3(lista5) == [0,1]
    assert lista5 == [9,9,1,2,3,4,5]
