'''
Created on 10/02/2012

@author: Alumno
'''
from programa import *

def test_suma():
    assert suma( 0 , 0) == 0
    assert suma( 5, 5) == 10
    assert suma(-5, 5) == 0
        
def test_multiplica_positivos():
    assert multiplica( 5, 10) == 50

def test_multiplica_negativos():
    assert multiplica(-1, -5) == 5
    
def test_cuadrado():
    assert cuadrado(3) == 9
    assert cuadrado(-3) == 9