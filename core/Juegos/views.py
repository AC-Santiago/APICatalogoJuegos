from django.shortcuts import render
from rest_framework import viewsets, permissions, parsers, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Juegos, ImagenesJuegos, Plataformas, Desarrolladoras, Generos
from .Api.serializers import (
    JuegosSerializer,
    ImagenesJuegosSerializer,
    PlataformasSerializer,
    DesarrolladorasSerializer,
    GenerosSerializer,
)


# Create your views here.
class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GenerosSerializer


class DesarrolladorasViewSet(viewsets.ModelViewSet):
    queryset = Desarrolladoras.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DesarrolladorasSerializer


class PlataformasViewSet(viewsets.ModelViewSet):
    queryset = Plataformas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlataformasSerializer


class ImagenesJuegosViewSet(viewsets.ModelViewSet):
    queryset = ImagenesJuegos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagenesJuegosSerializer
    parser_classes = [parsers.MultiPartParser]


class JuegosViewSet(viewsets.ModelViewSet):
    queryset = Juegos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JuegosSerializer
    parser_classes = [parsers.MultiPartParser]

    def create(self, request, *args, **kwargs):
        data = request.data
        print(f"Data: {data}, Archivos: {request.FILES}")
        # Crear el juego
        juego_serializer = JuegosSerializer(data=data)
        juego_serializer.is_valid(raise_exception=True)
        juego = juego_serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
