from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  ServidorForm
from .models import Servidor


def index_view(request):
   
    servidores = Servidor.objects.all()

    # Se o método for POST, tenta realizar o login
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("lista_servidores")  
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    return render(request, "index.html", {"servidores": servidores})


def login_view(request):
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("lista_servidores")  
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "index.html")  


def lista_servidores(request):
    servidores = Servidor.objects.all()
    return render(request, "lista_servidores.html", {"servidores": servidores})


def cadastrar_servidor(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        nome = request.POST['nome']
        setor = request.POST['setor']
        email = request.POST['email']

        Servidor.objects.create(nome=nome, setor=setor, email=email)
        return redirect('lista_servidores')

    return render(request, 'cadastrar_servidor.html')



def editar_servidor(request, servidor_id):
    if not request.user.is_authenticated:
        return redirect('login')

    servidor = get_object_or_404(Servidor, id=servidor_id)

    if request.method == "POST":
        form = ServidorForm(request.POST, instance=servidor)
        if form.is_valid():
            form.save()
            return redirect('lista_servidores')
    else:
        form = ServidorForm(instance=servidor)  # Carrega os dados do servidor no formulário

    return render(request, 'editar_servidor.html', {'form': form, 'servidor': servidor})


# def deletar_servidor(request, servidor_id):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     servidor = get_object_or_404(Servidor, id=servidor_id)
#     servidor.delete()
#     return redirect('lista_servidores')


def deletar_servidor(request, servidor_id):
    if not request.user.is_authenticated:
        return redirect('login')

    servidor = get_object_or_404(Servidor, id=servidor_id)

    if request.method == "POST":
        servidor.delete()
        return redirect('lista_servidores')

    return render(request, 'deletar_servidor.html', {'servidor': servidor})


def logout_view(request):
    logout(request)
    return redirect("index")
