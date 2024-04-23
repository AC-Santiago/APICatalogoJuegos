from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

import cloudinary.uploader

from django.shortcuts import get_object_or_404

from .Api.serializers import UsuarioCatalogoSerializer
from .models import UsuarioCatalogo


# Create your views here.
@api_view(["POST"])
def login(request):

    usuario = get_object_or_404(UsuarioCatalogo, username=request.data["username"])
    if not usuario.check_password(request.data["password"]):
        return Response(
            {"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST
        )

    token = Token.objects.get(user=usuario)
    return Response({"token": token.key}, status=status.HTTP_200_OK)


@api_view(["POST"])
def register(request):
    serializer = UsuarioCatalogoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        usuario = UsuarioCatalogo.objects.get(username=serializer.data["username"])
        usuario.set_password(serializer.data["password"])
        usuario.save()

        token = Token.objects.create(user=usuario)

        return Response(
            {"token": token.key, "usuario": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def profile(request):
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def logout(request):
    return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_account(request, id_usuario):
    usuaio_delete = get_object_or_404(UsuarioCatalogo, id=id_usuario)
    image_profile = usuaio_delete.image_profile
    if image_profile:
        cloudinary.uploader.destroy(image_profile.public_id)
    usuaio_delete.delete()
    return Response(status=status.HTTP_200_OK)
