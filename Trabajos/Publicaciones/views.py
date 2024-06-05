from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import formPubli
from .models import publicaciones
from django.contrib.auth.decorators import login_required

# Create your views here.

def principal(request):
    return render(request, 'home.html')

def registro(request):
    if request.method=='GET':
        return render(request, 'registro.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('publicaciones')
            except IntegrityError:
                return render(request, 'registro.html',{
                'form' : UserCreationForm,
                'error' : 'Nombre de usuario ya existe'
                })
        else:
            return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : 'Contraseñas no coinciden.'
        })
        
def ingresar(request):
    if request.method=='GET':
        return render(request,'login.html',{
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{
            'form' : AuthenticationForm,
            'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('publicaciones')

def verpegas(request):
    publicacion=publicaciones.objects.all()
    return render(request,'verpegas.html',{
        'publicaciones' : publicacion
    })

@login_required
def publicar(request):
    if request.method=='GET':
            return render(request,'publicar.html',{
            'form' : formPubli
            })
    else:
        try:
            publicacion=formPubli(request.POST)
            nueva_publi=publicacion.save(commit=False)
            nueva_publi.usuario= request.user
            nueva_publi.save()
            return redirect('publicaciones')
        except ValueError:
            return render(request,'publicar.html',{
            'form' : formPubli,
            'error' : 'Por favor complete los campos'
            })            

def detalle(request, publi_id):
    publi=get_object_or_404(publicaciones, pk=publi_id)
    return render(request, 'detalle.html',{
        'publicacion' : publi
    })

@login_required
def editar(request, publi_id):
    if request.method=='GET':
        publi=get_object_or_404(publicaciones, pk=publi_id, usuario=request.user)
        editar_publi=formPubli(instance=publi)
        return render(request, 'edicion.html',{
            'publicacion' : publi,
            'edicion' : editar_publi
        })
    else:
        try:
            publi=get_object_or_404(publicaciones, pk=publi_id, usuario=request.user)
            editar_publi=formPubli(request.POST, instance=publi)
            editar_publi.save()
            return redirect('publicaciones')
        except ValueError:
            return render(request, 'edicion.html',{
            'publicacion' : publi,
            'edicion' : editar_publi,
            'error' : 'Error al actualizar publicación'
        })

@login_required
def borrar(request, publi_id):
    if request.method=='POST':
        publi = get_object_or_404(publicaciones, pk=publi_id, usuario=request.user)
        publi.delete()
        return redirect('publicaciones')

@login_required    
def salir(request):
    logout(request)
    return redirect('home')