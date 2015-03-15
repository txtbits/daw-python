# -*- coding: utf-8 -*-
'''
Created on 15/02/2012

@author: chra
'''

def busqueda_lineal_w(v, L):
    '''Devuelve el índice de la primera ocurrencia del valor v en la lista L 
    o devuelve len(L) si v no está en L
    '''
    i = 0
    while i != len(L) and L[i] != v:
        i += 1
    return i

def busqueda_lineal_for(v, L):
    '''Devuelve el índice de la primera ocurrencia del valor v en la lista L 
    o devuelve len(L) si v no está en L
    '''
    i = 0
    for valor in L:
        if valor == v:
            return i
        i += 1
    return len(L)

def busqueda_lineal_for_enu(v, L):
    '''Devuelve el índice de la primera ocurrencia del valor v en la lista L 
    o devuelve len(L) si v no está en L
    '''
    i = 0
    for i, valor in enumerate(L):
        if valor == v:
            return i
    return len(L)

def busqueda_lineal_centinela(v, L):
    L.append(v)
    i = 0
    while L[i] != v:
        i += 1
    L.pop()
    return i

def time_it(busqueda, v, L):
    tini = time.time()
    busqueda(v, L)
    tfin = time.time()
    return (tfin - tini) * 1000