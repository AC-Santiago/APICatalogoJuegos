from rest_framework import permissions


class IsModeratorOrReadOnly(permissions.BasePermission):
    """
    Permite a los moderadores realizar cualquier acción en el objeto.
    Solo permite a los usuarios autenticados realizar acciones de escritura.
    """

    def has_permission(self, request, view):
        """
        Determina si el usuario puede realizar la acción solicitada.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_moderator
