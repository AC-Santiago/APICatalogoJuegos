from rest_framework import serializers
from ..models import (
    Juegos,
    ImagenesJuegos,
    Plataformas,
    Desarrolladoras,
    Generos,
    Catalogos,
)
from core.Usuarios.models import UsuarioCatalogo
from .optimize_url import optimize_url


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
    juego = serializers.SlugRelatedField(queryset=Juegos.objects.all(), slug_field="id")

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
    images = serializers.SerializerMethodField()

    class Meta:
        model = Juegos
        fields = [
            "id",
            "titulo",
            "fecha_Lanzamiento",
            "resumen",
            "valoracion",
            "numero_Partidas",
            "numero_jugadores",
            "comprado_no_jugado",
            "menciones_listas",
            "listas_de_deseos",
            "images",
            "reseñas",
            "generos",
            "plataformas",
            "desarrolladora",
        ]
        read_only_fields = ("id",)

    def get_images(self, obj):
        return [img.imagen_game for img in obj.images.all()]


class CatalogoSerializar(serializers.ModelSerializer):
    juegos = JuegosSerializer(many=True)
    Portada = serializers.SerializerMethodField()

    class Meta:
        model = Catalogos
        fields = ["id", "Nombre", "Portada", "usuario", "juegos"]
        read_only_fields = ("id",)

    def get_Portada(self, obj):
        if obj.Portada:
            return optimize_url(obj.Portada.public_id)
        return None


class CatalogoSerializarRegister(serializers.ModelSerializer):
    juegos = serializers.SlugRelatedField(
        many=True, queryset=Juegos.objects.all(), slug_field="id"
    )

    class Meta:
        model = Catalogos
        fields = ["id", "Nombre", "Portada", "usuario", "juegos"]
        read_only_fields = ("id",)
