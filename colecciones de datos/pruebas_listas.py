# -*- coding: cp1252 -*-
letras = ['a', 'b', 'm', 'c', 'Z']
letras.sort() #La letra Z (mayus) tiene un cód. ASCII inferior a letras (minus)
print letras

precios = "90 1000 500"
precios = precios.split()
print precios

nombres = 'Juan Ana Pedro Luis'
nombres = nombres.split()
print nombres
posicion = nombres.index('Pedro') # Ya que toma la primera posicion como valor 0
print posicion

nombres.append('Pedro') #Añade Pedro a la lista (al final)
print nombres

nombres.insert(0, 'Luis') #Inserta el nombres 'Luis' en la primera posicion (0)
print nombres

contador = nombres.count('Pedro')  #Cuenta las veces que se repite una cadena
print contador

nombres.remove('Ana') #Elimina la cadena 'Ana' de la lista
print nombres

letra = nombres.pop(2) #Saca de la lista a la cadena que determines
print 'El nombre quitado es el tercero de la lista: ', letra
print 'Los que quedan son: ', nombres
