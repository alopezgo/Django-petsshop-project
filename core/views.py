from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Fundacion, Mascota, Producto
from .forms import FormularioCliente, ProductosForm

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def index(request):
    return render(request, 'core/index.html')


def nosotros(request):
    return render(request, 'core/nosotros.html')


def contacto(request):
    return render(request, 'core/contacto.html')


def tienda(request):
    return render(request, 'core/tienda.html')


def donaciones(request):

    return render(request, 'core/donaciones.html')


def Gatos(request):
    return render(request, 'core/Gatos.html')


def Mas(request):
    return render(request, 'core/Mas...html')


def Perros(request):
    return render(request, 'core/Perros.html')


def Adopciones(request):
    mascotas = Mascota.objects.all

    datos = {
        'mascotas': mascotas
    }

    return render(request, 'core/adopciones.html', datos)


def BeBrave(request):
    fundacion = Fundacion.objects.all

    datos = {
        'fundaciones': fundacion
    }

    return render(request, 'core/adopciones.html', datos)


def form_productos(request):

    datos = {
        'form': ProductosForm()
    }

    if request.method == 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Producto agregado correctamente'

    return render(request, 'core/form_productos.html', datos)


def form_mod_productos(request, id):
    producto = Producto.objects.get(idproducto=id)

    datos = {
        'form': ProductosForm(instance=producto)
    }

    if request.method == 'PUT':
        formulario = ProductosForm(data=request.POST, instance=producto)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'

    return render(request, 'core/form_mod_productos.html', datos)


def form_del_productos(request, id):
    producto = Producto.objects.get(idproducto=id)
    producto.delete()
    if request.method == 'DELETE':
        formulario = ProductosForm(data=request.DELETE, instance=producto)

        if formulario.is_valid:
            formulario.save()

    return redirect(to="listado_productos")


def listado_productos(request):
    productos = Producto.objects.all

    datos = {
        'productos': productos
    }

    return render(request, 'core/listado_productos.html', datos)


def Adopciones(request):
    mascotas = Mascota.objects.all

    datos = {
        'mascotas': mascotas
    }

    return render(request, 'core/adopciones.html', datos)


def Form_cliente(request):
    cliente = FormularioCliente(request.POST)

    if cliente.is_valid():
        cliente.save()
        cliente = FormularioCliente()
    return render(request, "contacto.html", {"form": cliente, "mensaje": "ok"})
