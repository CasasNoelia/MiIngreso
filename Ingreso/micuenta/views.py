from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' tu cuenta fue creada con exito')
            return redirect('login')

    context = {'form': form}
    return render(request, 'micuenta/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'su usuario o contraseña son incorrectos')

    context = {}
    return render(request, 'micuenta/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def Home(request):
    return render(request, 'micuenta/dashboard.html')


def Recibo(request):
    return render(request, 'micuenta/recibo.html')


def Usuario_Registro(request):
    return render(request, 'usuario_registro.html')


def Empleo_Registro(request):
    return render(request, 'empleo_registro.html')


