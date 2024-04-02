from rest_framework import routers
from .views import (
    JuegosViewSet,
    ImagenesJuegosViewSet,
    PlataformasViewSet,
    DesarrolladorasViewSet,
    GenerosViewSet,
)

routers = routers.DefaultRouter()

routers.register(r"catalogo/Juegos", JuegosViewSet, basename="juego")
routers.register(r"catalogo/ImagenesJuegos", ImagenesJuegosViewSet)
routers.register(r"catalogo/Plataformas", PlataformasViewSet)
routers.register(r"catalogo/Desarrolladoras", DesarrolladorasViewSet)
routers.register(r"catalogo/Generos", GenerosViewSet)


urlpatterns = routers.urls
