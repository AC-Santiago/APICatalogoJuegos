# Generated by Django 5.0.3 on 2024-05-05 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_emailverificationcode'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='emailverificationcode',
            table='EmailVerificationCode',
        ),
    ]
