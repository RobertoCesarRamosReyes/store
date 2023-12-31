from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm

def index(request):
    return render(request,'index.html',{
        'message':'Listado de productos',
        'title':'Productos',
        'products':[
            {'title':'Playera','price':5,'stock':True},
            {'title':'Camisa','price':7,'stock':True},
            {'title':'Mochila','price':20,'stock':False},
            {'title':'Laptop','price':200,'stock':True},
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')
    return render(request,'users/login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request,'Sesión finalizada exitosamente')
    return redirect('login')

def register(request):
    form=RegisterForm()
    return render(request,'users/register.html',{
        'form':form
    })