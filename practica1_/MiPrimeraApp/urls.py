from django.urls import path
from .import views

urlpatterns = [
    path('bienvenida/',views.bienvenida, name = 'bienvenida'),
]

urlpatterns = [
    path('bienvenida1/',views.bienvenida1, name = 'bienvenida1'),
]

urlpatterns = [
    path('bienvenida2/',views.bienvenida2, name = 'bienvenida2'),
]
