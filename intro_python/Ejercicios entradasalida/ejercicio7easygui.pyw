#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
from math import sqrt
import easygui

print 'Ejercicio 7'
print '-'*60

cateto1 = easygui.enterbox('Introduce cateto1: ','Calcular hipotenusa')
cateto1 = float(cateto1)
cateto2 = easygui.enterbox('Introduce cateto2: ','Calcular hipotenusa')
cateto2 = float(cateto2)

hipotenusa = sqrt ( (cateto1**2) + (cateto2**2))

easygui.msgbox('La hipotenusa es: %f' % hipotenusa, 'Calcular hipotenusa')

