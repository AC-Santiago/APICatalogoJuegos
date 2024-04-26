from django.db import models
from django.contrib.auth.models import AbstractUser

from cloudinary import models as cloudinary_models


# Create your models here.
class UsuarioCatalogo(AbstractUser):
    image_profile = cloudinary_models.CloudinaryField(
        "image_profile",
        null=True,
        blank=True,
        folder="/CatalogoJuegos/Usuarios/",
    )
    is_moderator = models.BooleanField(default=False)

    class Meta:
        db_table = "UsuarioCatalogo"

    def __str__(self) -> str:
        return self.username
