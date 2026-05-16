from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Admin → puede crear, editar, eliminar.
    Viewer → solo puede listar y ver.
    SAFE_METHODS = GET, HEAD, OPTIONS (solo lectura).
    """

    def has_permission(self, request, view) -> bool:
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_admin()