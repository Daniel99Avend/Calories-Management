from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.



def inicio(request):

    return render(request, 'MainApp/inicio.html', {
        'Title': 'Inicio',
    })

def register_page(request):

	register_form = RegisterForm()

	if method.request == 'POST':

		register_form = RegisterForm(request.POST)

		if register_form.is_valid():

			register_form.save()

			return redirect('inicio')

	return render(request, 'users/register.html', {
        'Title': 'Registro',
        'register_form': register_form
        })
