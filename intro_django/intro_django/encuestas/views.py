# -*-coding: cp1252 -*-

from django.http import HttpResponse, HttpResponseRedirect
from encuestas.models import Encuesta, Opcion
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    listado_ultimas = Encuesta.objects.all().order_by('-fecha_pub')[:5]
    return render_to_response('encuestas/index.html',
        {'listado_ultimas': listado_ultimas,})
 
def detalle(request, encuesta_id):
    enc = get_object_or_404(Encuesta, pk=encuesta_id)
    return render_to_response('encuestas/detalle.html',
        {'encuesta': enc},
        context_instance=RequestContext(request))
 
def resultado(request, encuesta_id):
    enc = get_object_or_404(Encuesta, pk=encuesta_id)
    return render_to_response('encuestas/resultado.html', {'encuesta': enc})
 
def votar(request, encuesta_id):
    enc = get_object_or_404(Encuesta, pk=encuesta_id)
    try:
        opcion_seleccionada = enc.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Vuelve a mostrar el formulario de votacion
        return render_to_response('encuestas/detalle.html', {
            'encuesta': enc,
            'mensaje_error': "No has seleccionado ninguna opcion.",
        }, context_instance=RequestContext(request))
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        # Siempre devuelve un HttpResponseRedirect despues de tratar con exito
        # un formulario POST. Asi se evita enviar dos veces la informacion cuando
        # el usuario pulsa el boton retroceder.
        return HttpResponseRedirect(reverse('encuestas.views.resultado', args=(enc.id,)))
    return HttpResponse(u"Estas votando la encuesta %s." % encuesta_id)