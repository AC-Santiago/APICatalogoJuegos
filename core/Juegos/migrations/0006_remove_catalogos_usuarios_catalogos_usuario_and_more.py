# Generated by Django 5.0.3 on 2024-05-02 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0005_alter_catalogos_juegos_alter_catalogos_usuarios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogos',
            name='usuarios',
        ),
        migrations.AddField(
            model_name='catalogos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='catalogos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CatalogosXUsuarios',
        ),
    ]
