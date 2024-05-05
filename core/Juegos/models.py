from django.db import models
from cloudinary import models as cloudinary_models


# Create your models here.
class Plataformas(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "Plataformas"

    def __str__(self) -> str:
        return self.nombre


class Desarrolladoras(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = "Desarrolladoras"

    def __str__(self) -> str:
        return self.nombre


class Generos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "Generos"

    def __str__(self) -> str:
        return self.nombre


class JuegosXDesarrolladora(models.Model):
    juego = models.ForeignKey("Juegos", on_delete=models.CASCADE)
    desarrolladora = models.ForeignKey("Desarrolladoras", on_delete=models.CASCADE)

    class Meta:
        db_table = "JuegosXDesarrolladora"


class JuegosXPlataforma(models.Model):
    juego = models.ForeignKey("Juegos", on_delete=models.CASCADE)
    plataforma = models.ForeignKey("Plataformas", on_delete=models.CASCADE)

    class Meta:
        db_table = "JuegosXPlataforma"


class JuegosXGenero(models.Model):
    juego = models.ForeignKey("Juegos", on_delete=models.CASCADE)
    genero = models.ForeignKey("Generos", on_delete=models.CASCADE)

    class Meta:
        db_table = "JuegosXGenero"


class Juegos(models.Model):
    titulo = models.CharField(max_length=300)
    fecha_Lanzamiento = models.DateField(blank=True, null=True)
    resumen = models.TextField()
    valoracion = models.FloatField()
    numero_Partidas = models.IntegerField()
    numero_jugadores = models.IntegerField()
    comprado_no_jugado = models.IntegerField()
    menciones_listas = models.IntegerField()
    listas_de_deseos = models.IntegerField()
    reseñas = models.IntegerField()
    desarrolladora = models.ManyToManyField(
        Desarrolladoras,
        blank=True,
        related_name="juegos_desarrolladora",
        through="JuegosXDesarrolladora",
    )
    plataformas = models.ManyToManyField(
        Plataformas,
        blank=True,
        related_name="juegos_plataformas",
        through="JuegosXPlataforma",
    )
    generos = models.ManyToManyField(
        Generos, blank=True, related_name="juegos_generos", through="JuegosXGenero"
    )

    class Meta:
        db_table = "Juegos"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.titulo


class ImagenesJuegos(models.Model):
    imagen_game = models.URLField(null=True, blank=True)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE, related_name="images")

    class Meta:
        db_table = "ImagenesJuegos"
        ordering = ["id"]


class Catalogos(models.Model):
    Nombre = models.CharField(max_length=100)
    Portada = cloudinary_models.CloudinaryField(
        "image_game",
        null=True,
        blank=True,
        folder="/CatalogoJuegos/Portadas/",
        default="CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
    )
    juegos = models.ManyToManyField(
        Juegos, blank=True, related_name="catalogos", through="CatalogosXJuegos"
    )
    usuario = models.ForeignKey(
        "Usuarios.UsuarioCatalogo",
        on_delete=models.CASCADE,
        related_name="catalogos",
    )

    class Meta:
        db_table = "Catalogos"


class CatalogosXJuegos(models.Model):
    catalogo = models.ForeignKey(Catalogos, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)

    class Meta:
        db_table = "CatalogosXJuegos"
