# -*- coding: cp1252 -*-
'''
1. Escribe un programa que pida un n�mero y lo muestre al rev�s

1234 --> 4321
'''


#Leer n�mero

numero = raw_input('Escribe un n�mero: ')


#SOLUCI�N 1: TRATAR COMO LETRA
#Transformar n�mero

alreves = ''
for letra in numero:
    alreves = letra + alreves

print alreves

if numero == alreves:
    print "El n�mero es capic�a"
else:
    print "El n�mero NO es capic�a"

#SOLUCI�N 2: TRATAR COMO ENTERO
#Transformar n�mero

numero = int(numero)

resultado = 0
while numero != 0:
    resultado = resultado * 10 + numero %10
    numero = numero / 10

print resultado
