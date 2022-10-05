from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render
import random

from home.models import Persona

def crear_persona(request, nombre, apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona.save()
    
    # template = loader.get_template('crear_persona.html')
    # template_renderizado = template.render({'persona': persona})
    
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/crear_persona.html', {'persona': persona})


def ver_personas(request):
    
    personas = Persona.objects.all()
    
    # template = loader.get_template('ver_personas.html')
    # template_renderizado = template.render({'personas': personas})
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/ver_personas.html', {'personas': personas})

def index(request):
    
    return render(request, 'home/index.html')