from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^aplicacion/$', 'aplicacion.views.index'),
   (r'^aplicacion/hospitales$', 'aplicacion.views.hospital'),
   (r'^aplicacion/polizas$', 'aplicacion.views.poliza'),
   (r'^aplicacion/medicos$', 'aplicacion.views.medico'),
   (r'^aplicacion/telfmedicos$', 'aplicacion.views.telefono'),
   (r'^aplicacion/asegurados$', 'aplicacion.views.asegurado'),
   (r'^aplicacion/hospitalizados$', 'aplicacion.views.hospitalizacion'),
    url(r'^admin/', include(admin.site.urls)),
)
