from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import Movie


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_employee


class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Movie) -> bool:
        return obj.user.is_superuser or obj.user == request.user
