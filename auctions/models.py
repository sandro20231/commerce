from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Anuncio(models.Model):
    titulo = models.CharField(max_length=64)
    descricao = models.CharField(max_length=1000)
    lance_inicial = models.FloatField()
    imagem = models.URLField()
    categoria = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.titulo}/{self.categoria} Lançe inicial: {self.lance_inicial}, Descrição {self.descricao}"


class Lance(models.Model):
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    tituloescolhido = models.ForeignKey(
        Anuncio, on_delete=models.CASCADE, related_name="tituloescolhido")
    lance = models.FloatField()
    comentario = models.CharField(max_length=1000)

    def __str__(self):
        return f"Anúncio: {self.tituloescolhido}, eu {self.nome} {self.sobrenome}, dou um lance de: {self.lance}"


class Comentarios(models.Model):
    nome = models.CharField(max_length=64)
    tituloacomentar = models.ForeignKey(
        Anuncio, on_delete=models.CASCADE, related_name="tituloacomentar")
    data = models.DateField()
    comentario = models.CharField(max_length=1000)

    def __str__(self):
        return f"Nome: {self.nome},{self.tituloacomentar} Data: {self.data}, comentario: {self.comentario}"
