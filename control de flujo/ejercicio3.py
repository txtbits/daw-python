# -*- coding: cp1252 -*-
'''
El ordenador de nuestro coche calcula los kilómetros que
nos quedan antes de repostar. Crea un programa que pida:
tamaño del depósito (en litros), porcentaje del depósito que está lleno
y litros de consumo por 100kms.
El programa mostrará los kilómetros que quedan de autonomía.
Si quedan menos de 30 kilómetros
mostrará un aviso de que hay que repostar porque estamos usando la reserva.
'''

from easygui import *

t_deposito = int(enterbox('Introduce el tamaño del depósito (en litros)'))
porcentaje_d= int(enterbox('Introduce el porcentaje del depósito'))
consumo = float(enterbox('Introduce el consumo por cada 100kms. (en litros)'))

litros = t_deposito * (porcentaje_d/100.)
autonomia = (litros * 100) / consumo


if autonomia < 30:
    msgbox('Tienes que ir a repostar')
else:
    msgbox('Continua con tu viaje')
