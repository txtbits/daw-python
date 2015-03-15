# -*- coding: utf-8 -*-
'''
sumaNCubos(n) --> Devuelve la suma de los cubos
de los primeros n números naturales
'''

def sumaNCubos(n):
    resultado = 0
    for x in range(1, n+1):
        resultado += x**3 # x*x*x
    return resultado

def sumaNCubosv2(n):
    return([x**3 for x in range(1, n+1)])

print 'sumaNCubos(5)', sumaNCubos(5)

print 'sumaNCubos(5)', sumaNCubosv2(5)
