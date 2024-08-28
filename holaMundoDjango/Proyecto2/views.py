from django.shortcuts import render
from django.http import HttpResponse 



def display(request):
    return HttpResponse("Hola desde app2 Proyecto2")


# Create your views here.
