# -*- coding: cp1252 -*-
from math import *


for numero in range (1, 11):
    print ' %3d %4d %5d %5.2f %6.3f' % (numero, numero**2,
                                        numero**3, sqrt(numero), numero**(1/3.))
