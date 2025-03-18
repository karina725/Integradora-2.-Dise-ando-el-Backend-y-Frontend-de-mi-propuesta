from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import registrosForm
from django.contrib.auth.decorators import login_required


from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm() 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registro')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm, 
                    "error": 'User already exists'
                })
        return render(request, 'signup.html',{
            'form': UserCreationForm, 
            "error": 'Password no coicide'
        })

   
def registro(request):
    return render(request,'registro.html')


def crear_registros(request):
    if request.method == 'GET':
        return render(request, 'crear_registros.html',{
            'form': registrosForm
        })





def signout(request):
    logout (request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'signin.html', {
                'form':AuthenticationForm,
                'error':' Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('registro')
