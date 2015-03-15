# -*- coding: utf-8 -*-


'''
Crea una clase Hora con atributos para las horas, los minutos y los segundos de la hora Incluye, al menos, los siguientes métodos:
Constructor predeterminado con el 00:00:00 como hora por defecto. En el constructor se podrán indicar horas, minutos y segundos.
leer(): pedirá al usuario las horas, los minutos y los segundos.
valida(): comprobará si la hora es correcta; si no lo es la ajustará. Será un método auxiliar (privado) que se llamará en el constructor parametrizado y en leer().
a_segundos(): devolverá el número de segundos transcurridos desde la medianoche.
de_segundos(int): hará que la hora sea la correspondiente a haber transcurrido desde la medianoche los segundos que se indiquen.
segundos_desde(Hora): devolverá el número de segundos entre la hora y la proporcionada.
siguiente(): pasará al segundo siguiente.
anterior(): pasará al segundo anterior.
copia(): devolverá un clon de la hora.
Además (métodos especiales):
print: mostrará la hora (07:03:21).
igual_que(Hora): indica si la hora es la misma que la proporcionada.
menor_que(Hora): indica si la hora es anterior a la proporcionada.
mayor_que(Hora): indica si la hora es posterior a la proporcionada.
Haz un dibujo (UML) de la clase con dia.
Crea los tests correspondientes para demostrar que el programa funciona bien.
'''

import datetime

class Hora(object):
    def __init__(self, h=0, m=0, s=0):
        self.hora = h
        self.min = m
        self.seg = s
        
    def __str__(self):
        return "%02d:%02d:%02d" % (self.hora, self.min, self.seg)
    
    def leer(self):
        self.hora = int(raw_input('Introduce la hora: '))
        self.min = int(raw_input('Introduce los minutos: '))
        self.seg = int(raw_input('Introduce los segundos: '))
    
    def incorrecta(self):
        if self.hora < 0 or self.min < 0 or self.seg < 0:
            raise SystemError
        
    def validar(self):
        if self.seg >= 60:
            self.min += self.seg/60 
            self.seg = self.seg % 60
        if self.min >= 60:
            self.hora += self.min/60
            self.min = self.min % 60
        if self.hora >= 24:
            self.hora = self.hora%24
            
    def a_segundos(self):
        return self.hora * 3600 + self.min * 60 + self.seg

    def de_segundos(self):
        pedir_segundos = raw_input('Introduce los segundos totales: ')
        #self.finalhora = pedir_segundos / 
        
    def segundos_desde(self, otra):
        return self.a_segundos() - otra.a_segundos()

    def igual_que(self):
        actual = datetime.datetime.now()
        if actual.hour == self.hora and actual.minute == self.min and actual.second == self.seg:
            return 'La hora es la misma'
        else:
            return 'La hora NO es la misma'
        
    def menor_que(self):
        actual = datetime.datetime.now()
        if actual.hour > self.hora:
            return 'La hora NO es menor'
        elif actual.hour < self.hora:
            return 'La hora es menor'
        elif actual.minute >  self.min:
            return 'La hora NO es menor'
        elif actual.minute <  self.min:
            return 'La hora es menor'
        elif actual.second > self.seg:
            return 'La hora es mayor'
        elif actual.second < self.seg:
            return 'La hora es menor'
        else:
            return 'La hora es la misma'
         
h1 = Hora(14, 05, 03)
h2 = Hora(13, 26)
print h1
print h1.igual_que()