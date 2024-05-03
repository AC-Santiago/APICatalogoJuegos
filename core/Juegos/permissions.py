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


class IsOwner(permissions.BasePermission):
    """
    Permite a los usuarios realizar cualquier acción en el objeto.
    """

    def has_permission(self, request, view):
        """
        Determina si el usuario puede realizar la acción solicitada.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated


class IsOwnerOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_moderator
