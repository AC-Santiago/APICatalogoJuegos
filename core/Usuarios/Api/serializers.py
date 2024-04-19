from rest_framework import serializers
from ..models import UsuarioCatalogo


class UsuarioCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCatalogo
        fields = ["id", "username", "email", "password", "image_profile"]
        read_only_fields = ("id",)
