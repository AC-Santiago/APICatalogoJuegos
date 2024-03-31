from rest_framework import viewsets, permissions
from ..models import Juegos
from ..Api.serializers import JuegosSerializer


class JuegosViewSet(viewsets.ModelViewSet):
    queryset = Juegos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JuegosSerializer
