from rest_framework.permissions import BasePermission


class notAuthenticated(BasePermission):
    message = "You already have an account."
    def has_permission(self, request, view):
        return not request.user.is_authenticated

