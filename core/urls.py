from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name="index"),
    path('home/', index, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('tienda/', tienda, name="tienda"),
    path('donaciones/', donaciones, name="donaciones"),
    path('Gatos/', Gatos, name="Gatos"),
    path('Mas../', Mas, name="Mas"),
    path('Perros/', Perros, name="Perros"),
]
