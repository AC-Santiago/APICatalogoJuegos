from django.urls import path, include, re_path
from rest_framework import routers
from .views import (
    JuegosViewSet,
    ImagenesJuegosViewSet,
    PlataformasViewSet,
    DesarrolladorasViewSet,
    GenerosViewSet,
    get_recomendations,
    create_catalogo,
    add_juego_catalogo,
    delete_juego_catalogo,
    delete_catalogo,
    get_catalogos,
    get_catalogo,
    update_catalogo,
)

routers = routers.DefaultRouter()

routers.register(r"catalogo/Juegos", JuegosViewSet, basename="juego")
routers.register(r"catalogo/ImagenesJuegos", ImagenesJuegosViewSet)
routers.register(r"catalogo/Plataformas", PlataformasViewSet)
routers.register(r"catalogo/Desarrolladoras", DesarrolladorasViewSet)
routers.register(r"catalogo/Generos", GenerosViewSet)


urlpatterns = [
    path("", include(routers.urls)),
    re_path(
        r"^catalogo/Juegos/recomendations/(?P<titulo>.+)/$",
        get_recomendations,
        name="recomendations",
    ),
    re_path(
        r"^catalogo/Catalogos/create/$",
        create_catalogo,
        name="create_catalogo",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/add_juego/(?P<id>\d+)/$",
        add_juego_catalogo,
        name="add_juego_catalogo",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/delete_juego/(?P<id>\d+)/(?P<juego_id>\d+)/$",
        delete_juego_catalogo,
        name="delete_juego_catalogo",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/delete/(?P<id>\d+)/$",
        delete_catalogo,
        name="delete_catalogo",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/$",
        get_catalogos,
        name="get_catalogos",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/(?P<id>\d+)/$",
        get_catalogo,
        name="get_catalogo",
    ),
    re_path(
        r"^catalogo/Catalogos/usuario/update/(?P<id>\d+)/$",
        update_catalogo,
        name="update_catalogo",
    ),
]
