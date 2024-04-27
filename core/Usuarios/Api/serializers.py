from rest_framework import serializers
from ..models import UsuarioCatalogo


class UsuarioCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCatalogo
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "image_profile",
        ]
        read_only_fields = ("id",)

    def validate_password(self, password: str) -> str:
        if len(password) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres."
            )
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos un número."
            )
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos una letra."
            )
        return password
