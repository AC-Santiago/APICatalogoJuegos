# Generated by Django 5.0.3 on 2024-05-03 00:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0007_alter_catalogos_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogos',
            name='Portada',
            field=cloudinary.models.CloudinaryField(blank=True, default='CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t', max_length=255, null=True, verbose_name='image_game'),
        ),
    ]
