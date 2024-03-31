from django.contrib import admin
from .models import Juegos, Desarrolladoras, Generos, Plataformas

# Register your models here.
admin.site.register(Juegos)
admin.site.register(Plataformas)
admin.site.register(Desarrolladoras)
admin.site.register(Generos)
