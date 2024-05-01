from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, parsers, status, serializers
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Juegos, ImagenesJuegos, Plataformas, Desarrolladoras, Generos
from .Api.serializers import (
    JuegosSerializer,
    ImagenesJuegosSerializer,
    PlataformasSerializer,
    DesarrolladorasSerializer,
    GenerosSerializer,
)
from .permissions import IsModeratorOrReadOnly
from .Recomendacion import Recomendacion, JuegoGeneroPlataforma
from .Api.filter import JuegosFilter

# Create your views here.
recomendacion = Recomendacion()


class GenerosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModeratorOrReadOnly]
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer


class DesarrolladorasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModeratorOrReadOnly]
    queryset = Desarrolladoras.objects.all()
    serializer_class = DesarrolladorasSerializer


class PlataformasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModeratorOrReadOnly]
    queryset = Plataformas.objects.all()
    serializer_class = PlataformasSerializer


class ImagenesJuegosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModeratorOrReadOnly]
    queryset = ImagenesJuegos.objects.all()
    serializer_class = ImagenesJuegosSerializer
    parser_classes = [parsers.MultiPartParser]


class JuegosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModeratorOrReadOnly]
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer
    parser_classes = [parsers.MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JuegosFilter

    def create(self, request, *args, **kwargs):
        data = request.data
        juego_serializer = JuegosSerializer(data=data)
        juego_serializer.is_valid(raise_exception=True)
        juego_serializer.save()
        return Response(juego_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def get_recomendations(request, titulo: str):
    recomendaciones = recomendacion.get_recommendations_serializable(titulo)
    return Response(recomendaciones, status=status.HTTP_202_ACCEPTED)
