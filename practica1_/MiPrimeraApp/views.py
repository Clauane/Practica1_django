from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("hola esta es la pagina de inicio de tu aplicación ")



# Create your views here.
