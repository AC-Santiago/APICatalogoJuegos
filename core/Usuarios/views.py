from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

import cloudinary.uploader

from django.shortcuts import get_object_or_404

from .Api.serializers import UsuarioCatalogoSerializer
from .models import UsuarioCatalogo
from .permissions import IsOwnerOrModerator


@api_view(["POST"])
def register(request):
    serializer = UsuarioCatalogoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        usuario = UsuarioCatalogo.objects.get(username=serializer.data["username"])
        usuario.save()
        token = RefreshToken.for_user(usuario)
        return Response(
            {"refresh": str(token), "access": str(token.access_token)},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    usuario = get_object_or_404(UsuarioCatalogo, id=request.user.id)
    serializer = UsuarioCatalogoSerializer(usuario)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout(request):
    return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_account(request, id_usuario):
    usuaio_delete = get_object_or_404(UsuarioCatalogo, id=id_usuario)
    verificar_permisos = IsOwnerOrModerator().has_object_permission(
        request=request,
        view=None,
        obj=usuaio_delete,
    )
    if not verificar_permisos:
        return Response(
            {"Error": "No tienes los permisos para eliminar a este usuario"},
            status=status.HTTP_403_FORBIDDEN,
        )
    image_profile = usuaio_delete.image_profile
    if image_profile:
        cloudinary.uploader.destroy(image_profile.public_id)
    usuaio_delete.delete()
    return Response(status=status.HTTP_200_OK)
