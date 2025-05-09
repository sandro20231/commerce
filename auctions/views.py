from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Anuncio


def index(request):

    return render(request, "auctions/index.html", {"listagemativa": Anuncio.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def inserirproduto(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        lanceinicial = request.POST['lanceinicial']
        link = request.POST['linkimagem']
        categoria = request.POST['categoria']

        registro = Anuncio(titulo=titulo, descricao=descricao,
                           lance_inicial=lanceinicial, imagem=link, categoria=categoria)
        registro.save()
    return render(request, "auctions/inseriranuncio.html")


def mostraranuncio(request, anuncio):
    registro = Anuncio.objects.filter(titulo=anuncio).first()
    return render(request, "auctions/mostraranuncio.html", {"registro": registro})
