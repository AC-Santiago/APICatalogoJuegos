from django.db import models
from cloudinary import models as cloudinary_models


# Create your models here.
class Plataformas(models.Model):
    nombre = models.CharField(max_length=100)


class Desarrolladoras(models.Model):
    nombre = models.CharField(max_length=100)


class Generos(models.Model):
    nombre = models.CharField(max_length=100)


class Juegos(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_Lanzamiento = models.DateField()
    resumen = models.TextField()
    valoracion = models.FloatField()
    numero_Partidas = models.IntegerField()
    numero_jugadores = models.IntegerField()
    comprado_no_jugado = models.IntegerField()
    menciones_listas = models.IntegerField()
    listas_de_deseos = models.IntegerField()
    reseñas = models.IntegerField()
    desarrolladora = models.ManyToManyField(Desarrolladoras, blank=True)
    plataformas = models.ManyToManyField(Plataformas, blank=True)
    generos = models.ManyToManyField(Generos, blank=True)


class ImagenesJuegos(models.Model):
    imagen_game = cloudinary_models.CloudinaryField(
        "image_game",
        null=True,
        blank=True,
        folder="/CatalogoJuegos/Juegos/",
    )
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE, related_name="images")
