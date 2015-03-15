#-*- coding: utf-8 -*-

import unicodedata

def textplain(s):
    def normalize(c):
        return unicodedata.normalize("NFD", c)[0]
    return ''.join(normalize(c) for c in s)


def cuenta_vocales(cadena):
    '''devuelve el número de vocales de una cadena'''
    vocales = 0
    cadena = unicode(cadena, encoding= 'utf-8')
    cadena = cadena.lower()
    cadena = textplain(cadena)
    for x in cadena:
        if x in u'aeiou':
            vocales += 1
    return vocales

if __name__== '__main__':
    print textplain(u'españa')
    print cuenta_vocales('frío')
