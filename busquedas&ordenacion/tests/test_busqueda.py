# -*- coding: utf-8 -*-
'''
Created on 15/02/2012

@author: chra
'''

from algoritmos_busqueda import *

lista_n = range(1000)
lista_p =['hola', 'adios', 'luis', 'python']

''' ------- WHILE --------- '''

def test_b_lineal_w_enteros():
    assert busqueda_lineal_w(0, lista_n) == 0
    assert busqueda_lineal_w(1000, lista_n) == 1000
    assert busqueda_lineal_w(50, lista_n) == 50

def test_b_lineal_w_palabras():
    assert busqueda_lineal_w('noesta', lista_p) == 4
    assert busqueda_lineal_w('python', lista_p) == 3
   
''' ---------- FOR ---------- '''
 
def test_b_lineal_f_enteros():
    assert busqueda_lineal_for_enu(1000, lista_n) == 1000
    assert busqueda_lineal_for_enu(-1, lista_n) == 1000

def test_b_lineal_f_palabras():
    assert busqueda_lineal_for('noesta', lista_p) == 4
    assert busqueda_lineal_for_enu('hola', lista_p) == 0

''' ------- CENTINELA --------- '''

def test_b_lineal_centi_enteros():
    assert busqueda_lineal_centinela(0, lista_n) == 0
    assert busqueda_lineal_centinela(1000, lista_n) == 1000

def test_b_lineal_centi_palabras():
    assert busqueda_lineal_centinela('adios', lista_p) == 1

''' --------- TIMING ----------- '''
    

    