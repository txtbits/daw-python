# -*-coding: cp1252 -*-
 
from models import Encuesta, Opcion
from django.contrib import admin

class OpcionesEnLinea(admin.TabularInline):
    model = Opcion
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'fecha_pub', 'es_reciente']
    fieldsets = [
        (None, {'fields': ['pregunta']}),
        ('Publicacion', {'fields': ['fecha_pub'],
        'classes': ['collapse']}),
    ]
    inlines = [OpcionesEnLinea]
    list_filter = ['fecha_pub']
    search_fields = ['pregunta']
    
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Opcion)
