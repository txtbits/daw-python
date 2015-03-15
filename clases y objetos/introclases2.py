'''
Created on 12/12/2011

@author: chra
'''

class Trabajador(object):
    def __init__ (self, nombre):
        self.nombre = nombre
        self.antiguedad = 0
        self.salario = 800
    def aumenta_sueldo(self, cantidad):
        self.salario += cantidad
    
    
t1 = Trabajador('Ana')
print t1.nombre, t1.antiguedad, t1.salario

print '---------------------'

t2 = Trabajador('Pepe')
print t2.nombre, t2.antiguedad, t2.salario

print '---- Aumento sueldo ----'
t1.aumenta_sueldo(200)
print t1.nombre, t1.antiguedad, t1.salario