# -*- coding: cp1252 -*-
'''
3. Escribe un programa que pida una frase cifrada con el mismo sistema y la descifre.

( Escribe un programa que pida una frase y que la codifique cambiando
el códigoascii de cada letra sumándole +2. )
'''

frase = raw_input('Escribe una frase secreta: ')

cifrado = ''

for letra in frase:
    asci = ord(letra)
    if asci != 32:
        asci += 2

    cifrado = cifrado + chr(asci)

print cifrado

raw_input('Pulsa una tecla para descifrar')

descifrado = ''

for letra in cifrado:
    asci = ord(letra)
    if asci != 32:
        asci -= 2

    descifrado = descifrado + chr(asci)

print descifrado
