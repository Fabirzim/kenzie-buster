from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsEmployeeOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        if request.user.is_authenticated and (
            request.user.is_employee or request.user == user
        ):
            return True
