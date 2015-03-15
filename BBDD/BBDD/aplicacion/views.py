# Create your views here.
from aplicacion.models import Hospital, Poliza, Asegurado, Medico, Telefono, Hospitalizacion
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('aplicacion/index.html',
        {})

def hospital(request):
    listado_hos = Hospital.objects.all()
    return render_to_response('aplicacion/hospital.html',
        {'listado_hospitales': listado_hos})
    
def poliza(request):
    listado_pol = Poliza.objects.all()
    return render_to_response('aplicacion/poliza.html',
        {'listado_polizas': listado_pol})
    
def asegurado(request):
    listado_ase = Asegurado.objects.all()
    return render_to_response('aplicacion/asegurado.html',
        {'listado_asegurados': listado_ase})

def medico(request):
    listado_med = Medico.objects.all()
    return render_to_response('aplicacion/medico.html',
        {'listado_medicos': listado_med})

def telefono(request):
    listado_tel = Telefono.objects.all()
    return render_to_response('aplicacion/telfmedico.html',
        {'listado_telefonos': listado_tel})

def hospitalizacion(request):
    listado_hospitalizacion = Hospitalizacion.objects.all()
    return render_to_response('aplicacion/hospitalizado.html',
        {'listado_hospitalizaciones': listado_hospitalizacion})
