from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.


def inicio(request):

    return render(request, 'MainApp/inicio.html', {
        'Title': 'Inicio',
    })


def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':

        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            register_form.save()
            messages.succes(request,'Te has registrado correctamente')

            return redirect('inicio')

    return render(request, 'MainApp/registro.html', {
        'Title': 'Registro',
        'register_form': register_form
    })

def login_page(request):

    if request.method == 'POST':
        username= request.POST.get('username') 
        password= request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('inicio')
        else:
            messages.warning(request,'Usuario y/o Ccontraseña invalido')