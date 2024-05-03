# Generated by Django 5.0.3 on 2024-05-02 17:11

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0003_alter_juegos_fecha_lanzamiento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Portada', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_game')),
            ],
            options={
                'db_table': 'Catalogos',
            },
        ),
        migrations.AlterModelOptions(
            name='juegos',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='CatalogosXJuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.catalogos')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.juegos')),
            ],
            options={
                'db_table': 'CatalogosXJuegos',
            },
        ),
        migrations.AddField(
            model_name='catalogos',
            name='juegos',
            field=models.ManyToManyField(blank=True, through='Juegos.CatalogosXJuegos', to='Juegos.juegos'),
        ),
        migrations.CreateModel(
            name='CatalogosXUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.catalogos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CatalogosXUsuarios',
            },
        ),
        migrations.AddField(
            model_name='catalogos',
            name='usuarios',
            field=models.ManyToManyField(through='Juegos.CatalogosXUsuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]
