from rest_framework import serializers
from ..models import Juegos, ImagenesJuegos, Plataformas, Desarrolladoras, Generos


class PlataformasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataformas
        fields = "__all__"
        read_only_fields = ("id",)


class DesarrolladorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrolladoras
        fields = "__all__"
        read_only_fields = ("id",)


class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = "__all__"
        read_only_fields = ("id",)


class ImagenesJuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesJuegos
        fields = ["imagen_game", "juego"]
        read_only_fields = ("id",)


class JuegosSerializer(serializers.ModelSerializer):
    generos = serializers.SlugRelatedField(
        many=True, queryset=Generos.objects.all(), slug_field="nombre"
    )
    plataformas = serializers.SlugRelatedField(
        many=True, queryset=Plataformas.objects.all(), slug_field="nombre"
    )
    desarrolladora = serializers.SlugRelatedField(
        many=True, queryset=Desarrolladoras.objects.all(), slug_field="nombre"
    )

    class Meta:
        model = Juegos
        fields = "__all__"
        read_only_fields = ("id",)
