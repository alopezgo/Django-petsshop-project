from django.urls import path
from rest_productos.views import lista_productos, lista_mascotas, lista_fundaciones
from rest_productos.viewsLogin import login

urlpatterns = [
    path('lista-productos', lista_productos, name="lista_productos"),
    path('lista-mascotas', lista_mascotas, name="lista_mascotas"),
    path('lista-fundaciones', lista_fundaciones, name="lista_fundaciones"),
    path('login', login, name="login")
]
