# Generated by Django 5.0.3 on 2024-05-02 18:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0006_remove_catalogos_usuarios_catalogos_usuario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogos', to=settings.AUTH_USER_MODEL),
        ),
    ]
