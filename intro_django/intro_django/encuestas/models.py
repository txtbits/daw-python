# -*- coding: cp1252 -*-

from django.db import models
from django.utils import timezone
import datetime
 
# Create your models here.
class Encuesta(models.Model):
    pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicacion')
 
    def __unicode__(self):
        return self.pregunta
    
    def es_reciente(self):
        return self.fecha_pub <= timezone.now() - datetime.timedelta(days=1)
    es_reciente.boolean = True
    es_reciente.short_description = "Reciente?"
    es_reciente.admin_order_field = True
 
class Opcion(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    opcion = models.CharField(max_length=200)    
    votos = models.IntegerField()
 
    def __unicode__(self):
        return self.opcion
    
    class Meta:
        verbose_name_plural = "Opciones"