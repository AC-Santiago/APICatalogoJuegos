from django.contrib import admin
from .models import UsuarioCatalogo


# Register your models here.
class UsuarioCatalogoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "image_profile")
    search_fields = ("username", "email")
    list_filter = ("username", "email")


admin.site.register(UsuarioCatalogo, UsuarioCatalogoAdmin)
