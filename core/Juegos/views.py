from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, parsers, status, serializers
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
import copy
from .models import (
    Juegos,
    ImagenesJuegos,
    Plataformas,
    Desarrolladoras,
    Generos,
    Catalogos,
)
from .Api.serializers import (
    JuegosSerializer,
    ImagenesJuegosSerializer,
    PlataformasSerializer,
    DesarrolladorasSerializer,
    GenerosSerializer,
    CatalogoSerializar,
    CatalogoSerializarRegister,
)
from .permissions import IsModeratorOrReadOnly, IsOwnerOrModerator
from .Recomendacion import Recomendacion
from .Api.filter import JuegosFilter
import cloudinary.uploader


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
    try:
        recomendaciones = recomendacion.get_recommendations_serializable(titulo)
        return Response(recomendaciones, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# -----------------Catalogos-----------------#


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_catalogo(request):
    try:
        data = copy.deepcopy(request.data)
        usuario_id = request.user.id
        data["usuario"] = usuario_id
        catalogo_serializer = CatalogoSerializarRegister(data=data)
        catalogo_serializer.is_valid(raise_exception=True)
        catalogo_serializer.save()
        return Response(catalogo_serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
@permission_classes([IsOwnerOrModerator])
def update_catalogo(request, id: int):
    try:
        catalogo = Catalogos.objects.get(id=id)
        if catalogo.usuario.id != request.user.id:
            raise ValidationError("No tienes permisos para editar este catalogo")
        data = copy.deepcopy(request.data)
        catalogo_serializer = CatalogoSerializarRegister(catalogo, data=data, partial=True)
        catalogo_serializer.is_valid(raise_exception=True)
        catalogo_serializer.save()
        return Response(catalogo_serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_catalogo(request, id: int):
    catalogo = Catalogos.objects.get(id=id)
    if catalogo.usuario.id != request.user.id:
        raise ValidationError("No tienes permisos para eliminar este catalogo")
    if catalogo.Portada.public_id != "CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t":
        cloudinary.uploader.destroy(catalogo.Portada.public_id)
    catalogo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_catalogos(request):
    catalogos = Catalogos.objects.filter(usuario=request.user)
    serializer = CatalogoSerializar(catalogos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_catalogo(request, id: int):
    catalogo = Catalogos.objects.get(id=id)
    serializer = CatalogoSerializar(catalogo)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsOwnerOrModerator])
def add_juego_catalogo(request, id: int):
    try:
        juegos_ids = request.data.get("juego_id", [])
        catalogo = Catalogos.objects.get(id=id)
        for juego_id in juegos_ids:
            juego = Juegos.objects.get(id=int(juego_id))
            catalogo.juegos.add(juego)
        serializers = CatalogoSerializar(catalogo)
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsOwnerOrModerator])
def delete_juego_catalogo(request, id: int, juego_id: int):
    try:
        catalogo = Catalogos.objects.get(id=id)
        juego = Juegos.objects.get(id=juego_id)
        catalogo.juegos.remove(juego)
        return Response(status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# -----------------Catalogos-----------------#
