# -*- coding: cp1252 -*-
'''
1. Escribe un programa que pida un número y lo muestre al revés

1234 --> 4321
'''


#Leer número

numero = raw_input('Escribe un número: ')


#SOLUCIÓN 1: TRATAR COMO LETRA
#Transformar número

alreves = ''
for letra in numero:
    alreves = letra + alreves

print alreves

if numero == alreves:
    print "El número es capicúa"
else:
    print "El número NO es capicúa"

#SOLUCIÓN 2: TRATAR COMO ENTERO
#Transformar número

numero = int(numero)

resultado = 0
while numero != 0:
    resultado = resultado * 10 + numero %10
    numero = numero / 10

print resultado
