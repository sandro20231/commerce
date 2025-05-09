from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("inserirproduto", views.inserirproduto, name="inserirproduto"),
    path("anuncio/<str:anuncio>", views.mostraranuncio, name="mostraranuncio")
]
