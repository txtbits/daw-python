# -*- coding: cp1252 -*-
'''
2. Escribe un programa que pida una frase y que la codifique cambiando
el códigoascii de cada letra sumándole +2.
'''

frase = raw_input('Escribe una frase secreta: ')

secreta = ''

for letra in frase:
    asci = ord(letra)
    asci += 2

    secreta = secreta + chr(asci)

print secreta
