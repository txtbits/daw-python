'''
Created on 08/06/2012

@author: Alumno
'''


from models import *
from django.contrib import admin

'''
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
''' 
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ['asegurado', 'hospital', 'dias_ingreso', 'fecha_ingreso']
    
    
admin.site.register(Hospital)
admin.site.register(Poliza)
admin.site.register(Asegurado)
admin.site.register(Medico)
admin.site.register(Telefono)
admin.site.register(Hospitalizacion, HospitalizacionAdmin)
