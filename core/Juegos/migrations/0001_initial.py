# Generated by Django 5.0.3 on 2024-03-29 20:48

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Desarrolladoras",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Generos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Plataformas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Juegos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("fecha_Lanzamiento", models.DateField()),
                ("resumen", models.TextField()),
                ("valoracion", models.FloatField()),
                ("numero_Partidas", models.IntegerField()),
                ("numero_jugadores", models.IntegerField()),
                ("comprado_no_jugado", models.IntegerField()),
                ("menciones_listas", models.IntegerField()),
                ("listas_de_deseos", models.IntegerField()),
                ("reseñas", models.IntegerField()),
                (
                    "desarrolladora",
                    models.ManyToManyField(blank=True, to="Juegos.desarrolladoras"),
                ),
                ("generos", models.ManyToManyField(blank=True, to="Juegos.generos")),
                (
                    "plataformas",
                    models.ManyToManyField(blank=True, to="Juegos.plataformas"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImagenesJuegos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagen_game",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="image_game"
                    ),
                ),
                (
                    "juego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="Juegos.juegos",
                    ),
                ),
            ],
        ),
    ]