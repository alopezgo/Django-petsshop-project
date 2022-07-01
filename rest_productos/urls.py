from django.urls import path
from rest_productos.views import lista_productos, lista_mascotas

urlpatterns = [
    path('lista-productos', lista_productos, name="lista_productos"),
    path('lista-mascotas', lista_mascotas, name="lista_mascotas"),
]
