from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from django.shortcuts import render, HttpResponse, redirect


def login(request):
    #Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    # Añadimos los datos recibidos al formulario
    form = AuthenticationForm(data=request.POST)
    # Si el formulario es válido...
    if form.is_valid():
        # Recuperamos las credenciales validadas
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Verificamos las credenciales del usuario
        user = authenticate(username=username, password=password)

        # Si existe un usuario con ese nombre y contraseña
        if user is not None:
            # Hacemos el login manualmente
            do_login(request,user)
            # Y le redireccionamos a la portada
            return redirect('login')

    # Si llegamos al final renderizamos el formulario
    return render(request, "DeportesUY/entrenador.html", {'form': form})


def logout(request):
    auth.logout(request)

def ninos(request):
    login(request)
    return render(request,"DeportesUY/ninos.html")

def juveniles(request):
    login(request)
    return render(request,"DeportesUY/juveniles.html")

def varones(request):
    login(request)
    return render(request, "DeportesUY/varones.html")

def mujeres(request):
    login(request)
    return render(request, "DeportesUY/mujeres.html")

def adultos(request):
    login(request)
    return render(request, "DeportesUY/adultos.html")

def mayores(request):
    login(request)
    return render(request, "DeportesUY/mayores.html")