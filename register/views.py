from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(response):
    if response.method == "POST":
        form = RegistroForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/")
    else:
        form = RegistroForm()
    return render(response, "registro/registro.html", {"form" : form})

def login (response):
    return render (response, 'login.html')