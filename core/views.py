from django.shortcuts import render

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





