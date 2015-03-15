# -*- coding: cp1252 -*-

from django.db import models
from django.utils import timezone
import datetime
#from django.core.management.validation import max_length

# Create your models here.

class Poliza(models.Model):
    datos = models.CharField(max_length=200)
    def __unicode__(self):
        return self.datos
    

class Asegurado(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    poliza = models.ForeignKey(Poliza)
    
    def __unicode__(self):
        return self.nombre
    
class Hospital(models.Model):
    nombre = models.CharField(max_length=30)
    camas = models.BigIntegerField()
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Hospitales"
    
class Medico(models.Model):
    nombre = models.CharField(max_length=30, blank=True)
    hospital = models.ForeignKey(Hospital)
    def __unicode__(self):
        return self.nombre
    
class Telefono(models.Model):
    telefono = models.CharField(max_length=9, primary_key=True)
    medico = models.ForeignKey(Medico)
    def __unicode__(self):
        return self.telefono
    
class Hospitalizacion(models.Model):
    asegurado = models.ForeignKey(Asegurado)
    hospital = models.ForeignKey(Hospital)
    medico = models.ForeignKey(Medico)
    fecha_ingreso = models.DateField()
    fecha_alta = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.asegurado.nombre + "/" + self.hospital.nombre
    
    class Meta:
        verbose_name_plural = "Hospitalizaciones"
        
    def dias_ingreso(self):
        if self.fecha_alta:
            return self.fecha_alta-self.fecha_ingreso
        else:
            return datetime.date.now()-self.fecha_ingreso
            