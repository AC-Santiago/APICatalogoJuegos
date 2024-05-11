# Generated by Django 5.0.3 on 2024-05-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_usuariocatalogo_is_moderator'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]