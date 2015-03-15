#-*- coding: utf-8 -*-
'''
Ejemplos de test con nose
'''


from funciones import *

def test_cuenta_vocales():
    assert cuenta_vocales('casa') == 2
    assert cuenta_vocales('CASA') == 2

def test_cuenta_vocales_vacia():
    assert cuenta_vocales('sdfg') == 0

def test_cuenta_vocales_acento():
    assert cuenta_vocales('frío') == 2
    assert cuenta_vocales('FRÍO') == 2
    assert cuenta_vocales('murciélago') == 5
    
def test_cuenta_vocales_dieresis():
    assert cuenta_vocales('cigüeña') == 4
    
def test_cuenta_vocales_multiples():
    assert cuenta_vocales('àcêntóòôö') == 6