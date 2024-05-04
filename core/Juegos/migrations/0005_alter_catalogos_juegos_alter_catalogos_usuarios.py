# Generated by Django 5.0.3 on 2024-05-02 17:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0004_catalogos_alter_juegos_options_catalogosxjuegos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogos',
            name='juegos',
            field=models.ManyToManyField(blank=True, related_name='catalogos', through='Juegos.CatalogosXJuegos', to='Juegos.juegos'),
        ),
        migrations.AlterField(
            model_name='catalogos',
            name='usuarios',
            field=models.ManyToManyField(related_name='catalogos', through='Juegos.CatalogosXUsuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]