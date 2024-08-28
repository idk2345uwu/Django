from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>Wola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora: </b>" + str(dt)
    return HttpResponse(s)

def formulario(request):
    txt = "<br>Formulario</br>"
    txt = "<label>Usuario</label>"
    return HttpResponse
    

# Create your views here.
