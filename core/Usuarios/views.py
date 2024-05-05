from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from django.core.mail import send_mail
import random
import schedule
import cloudinary.uploader

from django.shortcuts import get_object_or_404

from .Api.serializers import UsuarioCatalogoSerializer
from .Api.optimize_url import optimize_url
from .models import UsuarioCatalogo, EmailVerificationCode
from .permissions import IsOwnerOrModerator


@api_view(["POST"])
def register(request):
    try:
        serializer = UsuarioCatalogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            usuario = UsuarioCatalogo.objects.get(username=serializer.data["username"])
            usuario.set_password(serializer.data["password"])
            usuario.save()
            token = RefreshToken.for_user(usuario)
            return Response(
                {"refresh": str(token), "access": str(token.access_token)},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    usuario = get_object_or_404(UsuarioCatalogo, id=request.user.id)
    serializer = UsuarioCatalogoSerializer(usuario)
    imagen_usuario = usuario.image_profile.public_id
    imagen = optimize_url(imagen_usuario)
    return Response(
        {
            "Usuario": serializer.data["username"],
            "Nombre": serializer.data["first_name"],
            "Apellido": serializer.data["last_name"],
            "Email": serializer.data["email"],
            "Imagen": str(imagen),
        },
        status=status.HTTP_200_OK,
    )


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


# -------------------Editar usuario-------------------#


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def edit_user(request):
    try:
        usuario = get_object_or_404(UsuarioCatalogo, id=request.user.id)
        serializado = UsuarioCatalogoSerializer(
            usuario, data=request.data, partial=True
        )
        if not serializado.is_valid():
            return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        if "image_profile" in request.FILES:
            image_profile_change(request, serializado, usuario.image_profile.public_id)
        usuario.set_password(request.data["password"])
        usuario.save()
        return Response(
            {
                "Usuario": serializado.data["username"],
                "Nombre": serializado.data["first_name"],
                "Apellido": serializado.data["last_name"],
                "Email": serializado.data["email"],
                "Imagen": cloudinary.CloudinaryImage(
                    usuario.image_profile.public_id
                ).build_url(),
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def image_profile_change(
    request, serializer: UsuarioCatalogoSerializer, public_id: str
):
    usuario = get_object_or_404(UsuarioCatalogo, id=request.user.id)
    if "image_profile" not in request.FILES:
        return Response(
            {"Error": "No se ha enviado ninguna imagen"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializado = serializer
    if usuario.image_profile:
        cloudinary.uploader.destroy(public_id)
    if not serializado.is_valid():
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------Editar usuario-------------------#


# -------------------Verificar Correo-------------------#
email_codes = {}


@api_view(["POST"])
def send_verification_email_user(request):
    try:
        subject = "Código de verificación"
        code = str(random.randint(1000, 9999))
        message = "Tu código de verificación es: " + code
        to_email = request.data["to_email"]
        email_codes[to_email] = code
        send_mail(subject, message, None, [to_email])
        EmailVerificationCode.objects.create(email=to_email, code=code)
        return Response(
            {"Mensaje": "Correo enviado correctamente"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def verify_email(request):
    try:
        email = request.data["email"]
        code = request.data["code"]
        verification_code = EmailVerificationCode.objects.filter(
            email=email, code=code
        ).first()
        if verification_code:
            return Response(
                {"Mensaje": "Correo verificado correctamente"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"Error": "Código incorrecto o correo no encontrado"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def delete_old_codes():
    ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
    EmailVerificationCode.objects.filter(created_at__lt=ten_minutes_ago).delete()


schedule.every(1).minutes.do(delete_old_codes)
