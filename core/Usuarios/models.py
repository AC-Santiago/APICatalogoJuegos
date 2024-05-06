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
        default="CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
    )
    is_moderator = models.BooleanField(default=False)

    class Meta:
        db_table = "UsuarioCatalogo"

    def __str__(self) -> str:
        return self.username


class EmailVerificationCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "EmailVerificationCode"
