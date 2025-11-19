from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def index(request):

    if request.user.is_authenticated:
        return redirect("clubes/dashboard/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/clubes/dashboard/") 
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "core/index.html")


def sair(request):
    logout(request)
    return redirect("/")
