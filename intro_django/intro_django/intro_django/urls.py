from django.conf.urls.defaults import patterns, include, url
 
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^encuestas/$', 'encuestas.views.index'),
    (r'^encuestas/(?P<encuesta_id>\d+)/$', 'encuestas.views.detalle'),
    (r'^encuestas/(?P<encuesta_id>\d+)/resultado/$', 'encuestas.views.resultado'),
    (r'^encuestas/(?P<encuesta_id>\d+)/votar/$', 'encuestas.views.votar'),
    url(r'^admin/', include(admin.site.urls)),
)