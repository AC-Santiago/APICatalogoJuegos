# Generated by Django 5.0.3 on 2024-05-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Usuarios", "0005_alter_usuariocatalogo_image_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuariocatalogo",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
