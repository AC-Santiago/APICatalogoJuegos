# Generated by Django 5.0.3 on 2024-05-04 17:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0008_alter_catalogos_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesjuegos',
            name='imagen_game',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='imagen_game'),
        ),
    ]
