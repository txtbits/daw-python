# -*- coding: cp1252 -*-
'''
El ordenador de nuestro coche calcula los kil�metros que
nos quedan antes de repostar. Crea un programa que pida:
tama�o del dep�sito (en litros), porcentaje del dep�sito que est� lleno
y litros de consumo por 100kms.
El programa mostrar� los kil�metros que quedan de autonom�a.
Si quedan menos de 30 kil�metros
mostrar� un aviso de que hay que repostar porque estamos usando la reserva.
'''

from easygui import *

t_deposito = int(enterbox('Introduce el tama�o del dep�sito (en litros)'))
porcentaje_d= int(enterbox('Introduce el porcentaje del dep�sito'))
consumo = float(enterbox('Introduce el consumo por cada 100kms. (en litros)'))

litros = t_deposito * (porcentaje_d/100.)
autonomia = (litros * 100) / consumo


if autonomia < 30:
    msgbox('Tienes que ir a repostar')
else:
    msgbox('Continua con tu viaje')
