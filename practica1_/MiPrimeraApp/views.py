from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("hola esta es la pagina de inicio de tu aplicación ")

def bienvenida1(request):
    return HttpResponse("hola esta es la pagina de algo no se de tu aplicación ")


def bienvenida2(request):
    return HttpResponse("hola esta es la pagina del final de tu aplicación ")







# Create your views here.
