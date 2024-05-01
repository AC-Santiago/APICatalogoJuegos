import django_filters as filters

from core.Juegos.models import Juegos


class JuegosFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr="icontains")
    generos = filters.CharFilter(field_name="generos__nombre", lookup_expr="icontains")
    desarrolladora = filters.CharFilter(
        field_name="desarrolladora__nombre", lookup_expr="icontains"
    )
    plataformas = filters.CharFilter(
        field_name="plataformas__nombre", lookup_expr="icontains"
    )

    class Meta:
        model = Juegos
        fields = ["titulo", "generos", "desarrolladora", "plataformas"]
