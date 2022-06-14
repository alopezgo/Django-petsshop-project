from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('tienda/', tienda, name="tienda"),
    path('donaciones/', donaciones, name="donaciones"),
    path('Gatos/', Gatos, name="Gatos"),
    path('Mas../', Mas, name="Mas"),
    path('Perros/', Perros, name="Perros"),
    path('adopciones/', Adopciones, name="adopciones"),
    path('form-productos/', form_productos, name="form_productos"),
    path('mod-productos/<int:id>', form_mod_productos, name="form_mod_productos"),
    path('del-productos/<int:id>', form_del_productos, name="form_del_productos"),
    path('listado-productos/', listado_productos, name="listado_productos"),


]
