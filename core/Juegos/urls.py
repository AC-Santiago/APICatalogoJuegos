from rest_framework import routers
from .Api.viewsets import JuegosViewSet

routers = routers.DefaultRouter()

routers.register(r"catalogo/Juegos", JuegosViewSet)

urlpatterns = routers.urls
